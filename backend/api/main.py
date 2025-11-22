from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
import dspy
from pathlib import Path

# Import workers
import sys
sys.path.append(str(Path(__file__).parent.parent))
from workers.copywriter import ExperienceCopywriter
from config import GROQ_API_KEY, DSPY_LM_MODEL

app = FastAPI(
    title="Stimulus Collective API",
    description="AI-powered experience content generation",
    version="0.1.0"
)

# CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure DSPy with Groq
try:
    lm = dspy.LM(DSPY_LM_MODEL, api_key=GROQ_API_KEY)
    dspy.configure(lm=lm)
    print(f"✅ DSPy configured with {DSPY_LM_MODEL}")
except Exception as e:
    print(f"❌ Error configuring DSPy: {e}")
    raise

# Load experiences data
data_path = Path(__file__).parent.parent / "data" / "experiences.json"
with open(data_path) as f:
    EXPERIENCES = json.load(f)

print(f"✅ Loaded {len(EXPERIENCES)} experiences")

# Initialize AI worker
copywriter = ExperienceCopywriter()
print("✅ AI Copywriter initialized")

@app.get("/")
def health():
    """Health check endpoint."""
    return {
        "status": "ok",
        "message": "Stimulus Collective API",
        "ai_model": DSPY_LM_MODEL,
        "experiences_loaded": len(EXPERIENCES)
    }

@app.get("/api/experiences")
def list_experiences():
    """List all experiences (basic info only)."""
    return [
        {
            "slug": exp["slug"],
            "title": exp["title"],
            "price": exp["price"],
            "category": exp["category"],
            "duration": exp["duration"],
            "hero_image": exp["hero_image"]
        }
        for exp in EXPERIENCES
    ]

@app.get("/api/experiences/{slug}")
def get_experience(slug: str):
    """Get full experience with AI-generated content.

    This endpoint:
    1. Finds the experience by slug
    2. Generates AI content (tagline, description, highlights, scores)
    3. Returns combined data

    Note: In production, cache AI-generated content to avoid regenerating.
    """

    # Find experience
    exp = next((e for e in EXPERIENCES if e["slug"] == slug), None)
    if not exp:
        raise HTTPException(status_code=404, detail="Experience not found")

    print(f"📝 Generating AI content for: {exp['title']}")

    try:
        # Generate AI content
        ai_content = copywriter.forward(
            title=exp["title"],
            category=exp["category"],
            duration=exp["duration"],
            price=exp["price"],
            group_size=exp["group_size"],
            location=exp["location"],
            key_elements=exp["key_elements"]
        )

        print(f"✅ AI content generated successfully")

        # Create WhatsApp URL
        whatsapp_message = f"Hi! I'm interested in the {exp['title']} experience."
        whatsapp_url = f"https://wa.me/41XXXXXXXXX?text={whatsapp_message.replace(' ', '%20')}"

        # Merge and return
        return {
            **exp,
            **ai_content,
            "whatsapp_url": whatsapp_url
        }

    except Exception as e:
        print(f"❌ Error generating AI content: {e}")
        raise HTTPException(status_code=500, detail=f"Error generating content: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
