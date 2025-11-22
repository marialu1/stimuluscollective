# Stimulus Collective 🍷🍫🎨

> **"The Spotify of Experiences"**
>
> We don't just offer tours. We curate sensorial awakenings through AI-powered taste matching.

**Founded:** 2023 | **Location:** Basel, Switzerland | **Team:** Alex, Mark & Misha

---

## 🎯 What Makes Us Different

This isn't another tour company. It's an AI-powered experience platform that:

- **Learns Taste** - Every booking trains our recommendation engine
- **Composes Experiences** - Custom experiences, not fixed tours
- **Scales Humanity** - AI workers amplify expertise, not replace it
- **Gets Smarter** - TextGrad optimization loop continuously improves

> "You're not building a 'better tour company'—you're building 'the future of experience curation.'"

---

## 🧠 The AI Vision

### Stimulus Scores™
Every experience rated on 5 sensory dimensions:

```
TASTE    █████████░ 9/10  (gustatory stimulation)
SIGHT    ████████░░ 8/10  (visual beauty)
SOUND    ███████░░░ 7/10  (auditory richness)
THOUGHT  █████████░ 9/10  (cognitive challenge)
CONNECT  ██████████ 10/10 (human connection)
```

Customers filter by preferences. AI learns patterns. Better matches = higher conversion.

---

## 📚 Documentation

> **Everything from our conversations is preserved in `/docs/`**

### For Understanding the Vision
- [`docs/00-CONVERSATIONS/01-vision-and-philosophy.md`](docs/00-CONVERSATIONS/01-vision-and-philosophy.md) - The "insanely great" vision
- [`docs/00-CONVERSATIONS/02-ai-workers-concept.md`](docs/00-CONVERSATIONS/02-ai-workers-concept.md) - Complete AI worker system
- [`DECISIONS.md`](DECISIONS.md) - Why we chose each technology

### For Building
- **[`docs/04-IMPLEMENTATION/phase-1-mvp.md`](docs/04-IMPLEMENTATION/phase-1-mvp.md) - START HERE** (3.5 hour build guide)
- [`docs/01-ARCHITECTURE/`](docs/01-ARCHITECTURE/) - Technical architecture
- [`docs/03-AI-WORKERS/`](docs/03-AI-WORKERS/) - DSPy implementation details

### For Design
- [`docs/02-DESIGN-SYSTEM/`](docs/02-DESIGN-SYSTEM/) - Scrapbook aesthetic components

---

## 🏗️ Architecture

```
stimuluscollective/
├── backend/                    # FastAPI + DSPy AI workers
│   ├── workers/
│   │   ├── copywriter.py       # AI copywriter (Phase 1)
│   │   ├── researcher.py       # (Future)
│   │   └── designer.py         # (Future)
│   ├── api/main.py             # FastAPI endpoints
│   └── data/experiences.json   # Experience data
│
├── frontend/                   # Astro site
│   ├── src/pages/
│   │   ├── index.astro         # Homepage
│   │   └── experiences/[slug].astro
│   └── src/components/         # Scrapbook UI
│
└── docs/                       # Complete documentation
    ├── 00-CONVERSATIONS/       # Vision & philosophy
    ├── 01-ARCHITECTURE/        # Technical specs
    ├── 02-DESIGN-SYSTEM/       # UI components
    ├── 03-AI-WORKERS/          # DSPy implementation
    └── 04-IMPLEMENTATION/      # Build guides
```

---

## 🤖 AI Workers

### Phase 1: Copywriter (NOW) ⭐
Generates all content for experience pages:
- Compelling descriptions (200-250 words)
- Benefit-focused highlights
- Stimulus Scores (5 dimensions)
- SEO metadata

**Tech:** DSPy ChainOfThought + Groq gpt-oss-120b

### Future Workers:
- **Researcher** - Web search, competitor analysis, cultural insights
- **Designer** - Layout suggestions, color palettes, component specs
- **Strategist** - Market positioning, pricing, content strategy
- **SEO** - Keywords, schema markup, optimization
- **Insights** - Customer behavior analysis, continuous improvement

---

## 🎨 Design: "Digital Scrapbook"

Handcrafted aesthetic with digital magic:

- **Paper textures** - Craft backgrounds, torn edges
- **Polaroid cards** - Tilted photos with tape
- **Handwritten touches** - Custom underlines, annotations
- **Hover effects** - Elements "peel" like paper
- **Scrapbook layouts** - Asymmetric, collage-style

See `docs/02-DESIGN-SYSTEM/` for CSS examples and components.

---

## 🚀 Quick Start

### 1. Clone & Install

```bash
cd /home/marilu/proj/stimuluscollective

# Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Frontend
cd ../frontend
npm install
```

### 2. Configure

Create `backend/.env`:
```
GROQ_API_KEY=your-key-here
```

### 3. Run

```bash
# Terminal 1: Backend
cd backend
uvicorn api.main:app --reload

# Terminal 2: Frontend
cd frontend
npm run dev
```

Visit `http://localhost:4321` 🎉

**Detailed Guide:** [`docs/04-IMPLEMENTATION/phase-1-mvp.md`](docs/04-IMPLEMENTATION/phase-1-mvp.md)

---

## 🗺️ Roadmap

### ✅ Phase 1: MVP (Complete)
- [x] Documentation structure
- [x] Vision & philosophy captured
- [x] AI workers architecture designed
- [x] Technical decisions documented
- [x] Phase 1 implementation guide

### 🔨 Next: Build (3.5 hours)
- [ ] DSPy Copywriter worker
- [ ] FastAPI backend
- [ ] Astro frontend (minimal)
- [ ] WhatsApp booking flow

### 🟡 Phase 2: Validation (Week 1-2)
- [ ] Deploy to Netlify
- [ ] Add scrapbook aesthetic
- [ ] First real customer
- [ ] Feedback from Alex & Mark

### ⏳ Phase 3: Optimization (Week 3-4)
- [ ] TextGrad optimization loop
- [ ] Add Researcher worker
- [ ] A/B test variants
- [ ] Track conversion metrics

---

## 🧪 Philosophy

**Levels.io:** "Make it work, make it right, make it fast"
- Week 1: Prove AI can write good copy
- Week 2: Get first paying customer
- Week 3: Optimize based on data

**Steve Jobs:** "Insanely great or nothing"
- AI that learns taste > generic booking
- Bespoke experiences > fixed tours
- Human connection at scale > automation

**Our Synthesis:**
- Function before beauty (but make it beautiful)
- Ship fast, learn faster
- One perfect customer > 100 mediocre ones

---

## 🤝 Team

- **Alex** - 7 languages, Swiss/Spanish, Experience curator
- **Mark** - Chef, Gastronomy expert, Vendor relationships
- **Misha** - Technical co-founder, AI implementation

**The Unfair Advantage:** Tourism knowledge + Technical skills + Creative vision

---

## 📝 Key Decisions

See [`DECISIONS.md`](DECISIONS.md) for full rationale:

| Decision | Why |
|----------|-----|
| **Astro** (not Next.js) | Content-first, faster |
| **WhatsApp** (not booking system) | Personal touch, validates demand |
| **DSPy** (not manual prompts) | Self-improving, metric-driven |
| **JSON** (not database yet) | Faster prototype, easy migration |
| **Scrapbook design** (not minimal) | Memorable, differentiating |
| **AI-first** (not manual) | Scalable from Day 1 |

---

## 📞 Booking

**WhatsApp:** +41 XX XXX XX XX (coming soon)

---

## 🙏 Built With

Insights from:
- **Levels.io** - Ship fast methodology
- **Steve Jobs** - "Insanely great" philosophy
- **Omar Khattab (DSPy)** - Programming LLMs
- **James Zou (TextGrad)** - Text-based optimization

---

**Made with ♥ in Basel 🇨🇭**

> "Every interaction makes us smarter. Every booking teaches the AI. Every customer gets a better experience than the last."
