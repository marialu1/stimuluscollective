# Phase 1: MVP Implementation Guide

**Goal:** Working prototype with AI-generated content in 3.5 hours
**Outcome:** Wine Tour page with compelling AI copy + WhatsApp booking

---

## Prerequisites

- Python 3.10+ installed
- Node.js 18+ installed
- Groq API key (for gpt-oss-120b)
- Text editor (VS Code recommended)
- Terminal access

---

## Timeline Overview

```
TOTAL TIME: ~3.5 hours

Step 1: Backend Setup           (30 min)
Step 2: Copywriter Worker        (1 hour)
Step 3: API Endpoints            (30 min)
Step 4: Frontend                 (1 hour)
Step 5: End-to-End Test          (30 min)
```

---

## Step 1: Backend Setup (30 minutes)

### 1.1 Create Backend Structure

```bash
cd /home/marilu/proj/stimuluscollective
mkdir -p backend/{workers,api,data/training}
cd backend
```

### 1.2 Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 1.3 Install Dependencies

Create `requirements.txt`:
```txt
fastapi==0.109.0
uvicorn[standard]==0.27.0
dspy-ai==2.5.0
pydantic==2.5.0
python-dotenv==1.0.0
groq==0.4.0
```

Install:
```bash
pip install -r requirements.txt
```

### 1.4 Configure Environment

Create `.env`:
```bash
GROQ_API_KEY=your-groq-api-key-here
```

Create `backend/config.py`:
```python
import os
from dotenv import load_dotenv

load_dotenv()

# Groq configuration (using gpt-oss-120b as per .claude config)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "groq/llama-3.3-70b-versatile"  # Or gpt-oss-120b if available

# DSPy configuration
DSPY_LM_MODEL = GROQ_MODEL
```

### 1.5 Test DSPy Works

Create `backend/test_dspy.py`:
```python
import dspy
from config import GROQ_API_KEY, DSPY_LM_MODEL

# Configure DSPy with Groq
lm = dspy.LM(DSPY_LM_MODEL, api_key=GROQ_API_KEY)
dspy.configure(lm=lm)

# Simple test
class SimpleQA(dspy.Signature):
    """Answer questions."""
    question: str = dspy.InputField()
    answer: str = dspy.OutputField()

qa = dspy.ChainOfThought(SimpleQA)
response = qa(question="What is 2+2?")
print(f"Answer: {response.answer}")
```

Run test:
```bash
python test_dspy.py
```

Expected output: `Answer: 4` (or similar)

✅ **Checkpoint:** DSPy is working with Groq API

---

## Step 2: Copywriter Worker (1 hour)

### 2.1 Create DSPy Signature

Create `backend/workers/signatures.py`:
```python
import dspy

class GenerateExperienceContent(dspy.Signature):
    """Generate compelling content for a Stimulus Collective experience.

    Brand voice:
    - Sensorial: Appeal to senses (taste, sight, sound, touch, thought)
    - Human-driven: Emphasize personal connection, guides, small groups
    - Creative: Unique angles, not generic tour descriptions
    - Excellence: High quality, attention to detail

    Goal: Make someone FEEL the experience and want to book immediately.
    """

    # Inputs
    title: str = dspy.InputField(desc="Experience title")
    category: str = dspy.InputField(desc="Category: tours, gastronomy, or art")
    duration: str = dspy.InputField(desc="Duration (e.g., '2.5 hours')")
    price: int = dspy.InputField(desc="Price in EUR per person")
    group_size: str = dspy.InputField(desc="Max group size")
    location: str = dspy.InputField(desc="Location (e.g., 'Basel')")
    key_elements: list[str] = dspy.InputField(desc="Key elements included")

    # Outputs
    tagline: str = dspy.OutputField(desc="Short tagline (10 words max)")
    description: str = dspy.OutputField(desc="Compelling description (200-250 words, sensory language)")
    highlights: list[str] = dspy.OutputField(desc="5-7 key highlights, benefit-focused")

    taste_score: int = dspy.OutputField(desc="Taste stimulation score (1-10)")
    sight_score: int = dspy.OutputField(desc="Visual beauty score (1-10)")
    sound_score: int = dspy.OutputField(desc="Auditory richness score (1-10)")
    thought_score: int = dspy.OutputField(desc="Cognitive challenge score (1-10)")
    connect_score: int = dspy.OutputField(desc="Human connection score (1-10)")
```

### 2.2 Create Copywriter Module

Create `backend/workers/copywriter.py`:
```python
import dspy
from .signatures import GenerateExperienceContent

class ExperienceCopywriter(dspy.Module):
    """AI worker that generates compelling experience content."""

    def __init__(self):
        super().__init__()
        self.generate = dspy.ChainOfThought(GenerateExperienceContent)

    def forward(self, **kwargs):
        """Generate content for an experience."""
        result = self.generate(**kwargs)

        # Format output
        return {
            "tagline": result.tagline,
            "description": result.description,
            "highlights": result.highlights,
            "stimulus_scores": {
                "taste": result.taste_score,
                "sight": result.sight_score,
                "sound": result.sound_score,
                "thought": result.thought_score,
                "connect": result.connect_score,
            }
        }
```

### 2.3 Test Copywriter

Create `backend/test_copywriter.py`:
```python
import dspy
from workers.copywriter import ExperienceCopywriter
from config import GROQ_API_KEY, DSPY_LM_MODEL
import json

# Configure DSPy
lm = dspy.LM(DSPY_LM_MODEL, api_key=GROQ_API_KEY)
dspy.configure(lm=lm)

# Test with Wine Tour
copywriter = ExperienceCopywriter()

content = copywriter.forward(
    title="Wine, Cheese & History Tour",
    category="tours",
    duration="2.5 hours",
    price=65,
    group_size="Max 10 people",
    location="Basel",
    key_elements=[
        "3 wine tastings (Swiss, Alsatian, German)",
        "Artisan cheese pairings",
        "Historical walking tour through Old Town",
        "Expert sommelier guide with 15+ years experience"
    ]
)

print(json.dumps(content, indent=2))
```

Run:
```bash
python test_copywriter.py
```

Expected: See generated tagline, description, highlights, and scores.

✅ **Checkpoint:** Copywriter generates compelling content

---

## Step 3: API Endpoints (30 minutes)

### 3.1 Create Experience Data

Create `backend/data/experiences.json`:
```json
[
  {
    "slug": "wine-cheese-basel",
    "title": "Wine, Cheese & History Tour",
    "category": "tours",
    "duration": "2.5 hours",
    "price": 65,
    "group_size": "Max 10 people",
    "languages": ["EN", "ES", "DE"],
    "location": "Basel",
    "hero_image": "/images/wine-tour.jpg",
    "key_elements": [
      "3 wine tastings (Swiss, Alsatian, German)",
      "Artisan cheese pairings",
      "Historical walking tour through Old Town",
      "Expert sommelier guide with 15+ years experience"
    ]
  }
]
```

### 3.2 Create FastAPI App

Create `backend/api/main.py`:
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import dspy
from workers.copywriter import ExperienceCopywriter
from config import GROQ_API_KEY, DSPY_LM_MODEL

app = FastAPI(title="Stimulus Collective API")

# CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure DSPy
lm = dspy.LM(DSPY_LM_MODEL, api_key=GROQ_API_KEY)
dspy.configure(lm=lm)

# Load experiences data
with open("data/experiences.json") as f:
    EXPERIENCES = json.load(f)

# Initialize AI worker
copywriter = ExperienceCopywriter()

@app.get("/")
def health():
    return {"status": "ok", "message": "Stimulus Collective API"}

@app.get("/api/experiences")
def list_experiences():
    """List all experiences (basic info only)."""
    return [
        {
            "slug": exp["slug"],
            "title": exp["title"],
            "price": exp["price"],
            "category": exp["category"],
            "hero_image": exp["hero_image"]
        }
        for exp in EXPERIENCES
    ]

@app.get("/api/experiences/{slug}")
def get_experience(slug: str):
    """Get full experience with AI-generated content."""

    # Find experience
    exp = next((e for e in EXPERIENCES if e["slug"] == slug), None)
    if not exp:
        return {"error": "Not found"}, 404

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

    # Merge and return
    return {
        **exp,
        **ai_content,
        "whatsapp_url": f"https://wa.me/41XXXXXXXXX?text=Hi!%20I'm%20interested%20in%20the%20{exp['title'].replace(' ', '%20')}"
    }
```

### 3.3 Start Backend

```bash
cd backend
uvicorn api.main:app --reload
```

Visit `http://localhost:8000/docs` to see API docs.

Test: `http://localhost:8000/api/experiences/wine-cheese-basel`

✅ **Checkpoint:** API returns AI-generated content

---

## Step 4: Frontend (1 hour)

### 4.1 Create Astro Project

```bash
cd /home/marilu/proj/stimuluscollective
npm create astro@latest frontend
# Choose: Empty, Yes to TypeScript, No to strict, Yes to install deps
```

### 4.2 Create Homepage

Create `frontend/src/pages/index.astro`:
```astro
---
const response = await fetch('http://localhost:8000/api/experiences');
const experiences = await response.json();
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stimulus Collective - Basel Experiences</title>
    <style>
        body { font-family: Inter, sans-serif; max-width: 1200px; margin: 0 auto; padding: 2rem; }
        h1 { font-size: 2.5rem; }
        .experiences { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 2rem; }
        .card { border: 1px solid #ddd; padding: 1rem; border-radius: 8px; }
        .card h2 { margin-top: 0; }
        .card a { display: inline-block; margin-top: 1rem; background: #E53935; color: white; padding: 0.5rem 1rem; text-decoration: none; border-radius: 4px; }
    </style>
</head>
<body>
    <h1>Taste Basel Like Never Before</h1>
    <p>Sensory experiences that become lasting memories</p>

    <div class="experiences">
        {experiences.map(exp => (
            <div class="card">
                <h2>{exp.title}</h2>
                <p>From €{exp.price}</p>
                <a href={`/experiences/${exp.slug}`}>See More →</a>
            </div>
        ))}
    </div>
</body>
</html>
```

### 4.3 Create Experience Page

Create `frontend/src/pages/experiences/[slug].astro`:
```astro
---
export async function getStaticPaths() {
  const response = await fetch('http://localhost:8000/api/experiences');
  const experiences = await response.json();

  return experiences.map(exp => ({
    params: { slug: exp.slug }
  }));
}

const { slug } = Astro.params;
const response = await fetch(`http://localhost:8000/api/experiences/${slug}`);
const exp = await response.json();
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{exp.title} - Stimulus Collective</title>
    <style>
        body { font-family: Inter, sans-serif; max-width: 800px; margin: 0 auto; padding: 2rem; }
        h1 { font-size: 2.5rem; margin-bottom: 0.5rem; }
        .tagline { font-size: 1.25rem; color: #666; margin-bottom: 1rem; }
        .meta { display: flex; gap: 1rem; margin-bottom: 2rem; color: #666; }
        .scores { display: grid; grid-template-columns: repeat(5, 1fr); gap: 1rem; margin: 2rem 0; }
        .score { text-align: center; }
        .score-bar { height: 100px; background: #f0f0f0; position: relative; }
        .score-fill { background: #E53935; position: absolute; bottom: 0; width: 100%; }
        .description { line-height: 1.6; margin: 2rem 0; }
        .highlights { list-style: none; padding: 0; }
        .highlights li { padding: 0.5rem 0; padding-left: 1.5rem; position: relative; }
        .highlights li:before { content: "✓"; position: absolute; left: 0; color: #E53935; font-weight: bold; }
        .cta { display: inline-block; background: #E53935; color: white; padding: 1rem 2rem; text-decoration: none; border-radius: 4px; font-size: 1.25rem; margin-top: 2rem; }
    </style>
</head>
<body>
    <h1>{exp.title}</h1>
    <p class="tagline">{exp.tagline}</p>

    <div class="meta">
        <span>€{exp.price} per person</span>
        <span>|</span>
        <span>{exp.duration}</span>
        <span>|</span>
        <span>{exp.group_size}</span>
    </div>

    <div class="scores">
        <div class="score">
            <div class="score-bar">
                <div class="score-fill" style={`height: ${exp.stimulus_scores.taste * 10}%`}></div>
            </div>
            <p>Taste {exp.stimulus_scores.taste}/10</p>
        </div>
        <div class="score">
            <div class="score-bar">
                <div class="score-fill" style={`height: ${exp.stimulus_scores.sight * 10}%`}></div>
            </div>
            <p>Sight {exp.stimulus_scores.sight}/10</p>
        </div>
        <div class="score">
            <div class="score-bar">
                <div class="score-fill" style={`height: ${exp.stimulus_scores.sound * 10}%`}></div>
            </div>
            <p>Sound {exp.stimulus_scores.sound}/10</p>
        </div>
        <div class="score">
            <div class="score-bar">
                <div class="score-fill" style={`height: ${exp.stimulus_scores.thought * 10}%`}></div>
            </div>
            <p>Thought {exp.stimulus_scores.thought}/10</p>
        </div>
        <div class="score">
            <div class="score-bar">
                <div class="score-fill" style={`height: ${exp.stimulus_scores.connect * 10}%`}></div>
            </div>
            <p>Connect {exp.stimulus_scores.connect}/10</p>
        </div>
    </div>

    <div class="description">
        {exp.description}
    </div>

    <ul class="highlights">
        {exp.highlights.map(h => <li>{h}</li>)}
    </ul>

    <a href={exp.whatsapp_url} class="cta">Book This Experience →</a>
</body>
</html>
```

### 4.4 Start Frontend

```bash
cd frontend
npm run dev
```

Visit `http://localhost:4321`

✅ **Checkpoint:** Frontend displays AI-generated content

---

## Step 5: End-to-End Test (30 minutes)

### 5.1 Manual Testing Checklist

- [ ] Backend running on port 8000
- [ ] Frontend running on port 4321
- [ ] Homepage loads and shows Wine Tour
- [ ] Click "See More" navigates to experience page
- [ ] Experience page shows AI-generated tagline
- [ ] Experience page shows AI-generated description (200-250 words)
- [ ] Experience page shows 5-7 highlights
- [ ] Stimulus scores display correctly
- [ ] WhatsApp link works (opens WhatsApp with pre-filled message)

### 5.2 Quality Check

**Is the AI content good?**
- [ ] Tagline is evocative (makes you want to read more)
- [ ] Description uses sensory language
- [ ] Description mentions unique aspects (not generic)
- [ ] Highlights are benefit-focused (not just features)
- [ ] Stimulus scores make sense for the experience

**If not:**
- Review the DSPy signature (adjust instructions)
- Try running copywriter again (LLMs are stochastic)
- Consider adding few-shot examples

### 5.3 Performance Check

**Is it fast enough?**
- [ ] Experience page loads in <3 seconds
- [ ] AI generation happens in <5 seconds

**If slow:**
- Cache AI-generated content (don't regenerate on every request)
- Pre-generate content and store in JSON
- Consider faster Groq model

---

## Success Criteria

✅ **MVP is successful if:**
1. AI generates compelling content (subjectively good)
2. Page loads fast (<3 seconds)
3. WhatsApp booking flow works
4. Can add new experience in <10 minutes
5. Alex says "Wow, this is actually good"

---

## Next Steps After MVP

1. **Show to Alex** - Get his feedback on AI content quality
2. **Add 2 more experiences** - Chocolate Tour, Art Basel
3. **Improve design** - Add scrapbook aesthetic (from design docs)
4. **Set up TextGrad** - Start optimization loop
5. **Deploy** - Push to Netlify/Vercel
6. **First real booking** - Test with a friend

---

## Troubleshooting

### DSPy not generating good content
- Check Groq API key is valid
- Try different model (e.g., llama-3.3-70b-versatile)
- Adjust signature instructions
- Add few-shot examples

### Frontend build fails
- Check Node version (18+)
- Delete `node_modules` and reinstall
- Check Astro version compatibility

### CORS errors
- Ensure backend has CORSMiddleware configured
- Check frontend is fetching from correct URL

### AI generation is slow
- Normal for first request (model cold start)
- Cache results after first generation
- Consider pre-generating content

---

## Time Tracking

| Step | Estimated | Actual | Notes |
|------|-----------|--------|-------|
| Backend setup | 30 min | | |
| Copywriter worker | 1 hour | | |
| API endpoints | 30 min | | |
| Frontend | 1 hour | | |
| Testing | 30 min | | |
| **Total** | **3.5 hours** | | |

---

**Ready to build? Start with Step 1!** 🚀
