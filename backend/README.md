# Stimulus Collective Backend

FastAPI backend with DSPy AI workers for experience content generation.

## Setup

### 1. Create Virtual Environment

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Create `.env` file (copy from `.env.example`):

```bash
cp .env.example .env
```

Edit `.env` and add your Groq API key:

```
GROQ_API_KEY=your-actual-groq-api-key-here
```

## Test the AI Copywriter

```bash
python test_copywriter.py
```

This will:
- Connect to Groq API
- Generate AI content for Wine Tour
- Display tagline, description, highlights, scores
- Save full output to `generated_content_sample.json`

## Run the API Server

```bash
uvicorn api.main:app --reload
```

Or:

```bash
python api/main.py
```

Visit:
- **API Docs:** http://localhost:8000/docs
- **Health Check:** http://localhost:8000/
- **List Experiences:** http://localhost:8000/api/experiences
- **Get Experience:** http://localhost:8000/api/experiences/wine-cheese-basel

## API Endpoints

### `GET /`
Health check. Returns API status and configuration.

### `GET /api/experiences`
List all experiences (basic info only, no AI generation).

**Response:**
```json
[
  {
    "slug": "wine-cheese-basel",
    "title": "Wine, Cheese & History Tour",
    "price": 65,
    "category": "tours",
    "duration": "2.5 hours",
    "hero_image": "/images/wine-tour.jpg"
  }
]
```

### `GET /api/experiences/{slug}`
Get full experience with AI-generated content.

**Example:** `/api/experiences/wine-cheese-basel`

**Response:**
```json
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
  "key_elements": [...],
  "tagline": "AI-generated tagline",
  "description": "AI-generated description...",
  "highlights": ["...", "..."],
  "stimulus_scores": {
    "taste": 10,
    "sight": 9,
    "sound": 7,
    "thought": 9,
    "connect": 10
  },
  "whatsapp_url": "https://wa.me/..."
}
```

## Project Structure

```
backend/
├── api/
│   ├── __init__.py
│   └── main.py              # FastAPI app
├── workers/
│   ├── __init__.py
│   ├── signatures.py        # DSPy signatures
│   └── copywriter.py        # AI Copywriter worker
├── data/
│   ├── experiences.json     # Experience data
│   └── training/            # Future: training examples
├── config.py                # Configuration
├── requirements.txt         # Python dependencies
├── test_copywriter.py       # Test script
└── README.md               # This file
```

## Configuration

Edit `config.py` to change:
- **GROQ_MODEL:** Which Groq model to use (default: llama-3.3-70b-versatile)
- Add more configuration as needed

## Development

### Adding New Experiences

Edit `data/experiences.json`:

```json
{
  "slug": "new-experience",
  "title": "New Experience Title",
  "category": "tours|gastronomy|art",
  "duration": "2 hours",
  "price": 50,
  "group_size": "Max 8 people",
  "languages": ["EN"],
  "location": "Basel",
  "hero_image": "/images/new-experience.jpg",
  "key_elements": [
    "What's included...",
    "Another element..."
  ]
}
```

No code changes needed! AI will generate content automatically.

### Customizing AI Output

Edit `workers/signatures.py` to adjust:
- Output length
- Brand voice instructions
- Scoring criteria

### Caching AI Content

For production, cache generated content to avoid regenerating on every request:

```python
# In api/main.py
CONTENT_CACHE = {}

@app.get("/api/experiences/{slug}")
def get_experience(slug: str):
    if slug in CONTENT_CACHE:
        return CONTENT_CACHE[slug]

    # Generate content...
    result = {...}
    CONTENT_CACHE[slug] = result
    return result
```

## Troubleshooting

### "Module not found" errors
Make sure virtual environment is activated:
```bash
source venv/bin/activate
```

### "API key not found"
Check `.env` file exists and contains valid GROQ_API_KEY

### Slow AI generation
Normal for first request (cold start). Subsequent requests faster. Consider caching in production.

### CORS errors from frontend
CORS is configured to allow all origins in development. For production, restrict in `api/main.py`.

## Next Steps

1. Test AI content quality
2. Build frontend (Astro)
3. Add TextGrad optimization
4. Deploy to production

See `/docs/04-IMPLEMENTATION/phase-1-mvp.md` for full guide.
