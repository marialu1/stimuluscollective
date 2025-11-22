# AI Workers Concept

**Date:** 2024-11-22
**Context:** Designing the complete AI worker system for Stimulus Collective

---

## The Core Idea

> "I want the best workers for me to tell what I want for them to build."

You're not asking for code to be written.
You're asking for an **AI creative agency as a product**.

You want to say:
> "I want a tour page for Wine & Cheese experience in Basel"

And the AI workers:
- **Research** Basel wine culture
- **Write** compelling copy
- **Design** the layout
- **Generate** images/visuals
- **Optimize** for SEO
- **Create** the entire page

---

## The Complete AI Worker System

### Worker Architecture

```
YOUR COMMAND: "Create a new Paella Masterclass experience"

┌─────────────────────────────────────────────────────────────┐
│  ORCHESTRATOR AI                                            │
│  (Coordinates all workers)                                  │
└─────────────────────────────────────────────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│ STRATEGIST  │   │ RESEARCHER  │   │ CUSTOMER    │
│             │   │             │   │ INSIGHT     │
│ • Audience  │   │ • Paella    │   │             │
│ • Position  │   │   history   │   │ • Past Q&A  │
│ • Pricing   │   │ • Competitor│   │ • Patterns  │
└──────┬──────┘   └──────┬──────┘   └──────┬──────┘
       │                 │                 │
       └────────┬────────┴────────┬────────┘
                │                 │
                ▼                 ▼
        ┌─────────────┐   ┌─────────────┐
        │ COPYWRITER  │   │  DESIGNER   │
        │             │   │             │
        │ • Write     │   │ • Layout    │
        │   copy      │   │ • Colors    │
        │ • SEO meta  │   │ • Images    │
        └──────┬──────┘   └──────┬──────┘
               │                 │
               └────────┬────────┘
                        │
                        ▼
                ┌─────────────┐
                │ DEVELOPER   │
                │             │
                │ • Generate  │
                │   code      │
                │ • Deploy    │
                └──────┬──────┘
                       │
                       ▼
              📄 paella-masterclass.astro
              ✅ LIVE IN 10 MINUTES
```

---

## The 7 AI Workers

### 1. STRATEGIST WORKER (The Brain)

**Role:** Analyzes market and defines positioning

```python
class StrategistWorker(dspy.Module):
    """
    You tell it: "I want to create a chocolate tour experience"

    It outputs:
    - Target audience analysis
    - Competitive positioning
    - Pricing recommendation
    - Key differentiators
    - Content strategy
    - Marketing angles
    """
```

**Example Interaction:**
```
You: "Create new experience: Chocolate Tour Basel"

Strategist AI:
├─ Audience: Tourists 25-45, families, sweet lovers
├─ Positioning: "Sensory journey through Swiss chocolate"
├─ Price: €45-55 (competitor analysis)
├─ Differentiators:
│  ├─ Small groups (max 8)
│  ├─ Hidden artisan shops (not tourist traps)
│  └─ Taste-matching (pair chocolate to preferences)
├─ Content angle: "Educational + indulgent"
└─ SEO keywords: [chocolate tour basel, swiss chocolate...]
```

---

### 2. RESEARCHER WORKER (The Investigator)

**Role:** Gathers information to inform content creation

```python
class ResearcherWorker(dspy.Module):
    """
    Gathers information to inform content creation.

    Tools:
    - Web search (Basel tourism info)
    - Competitor analysis (what others offer)
    - Cultural research (local history, traditions)
    - Customer sentiment (reviews of similar tours)
    """
```

**Example:**
```
You: "Research for Wine & Cheese tour"

Researcher AI → Uses tools to find:
├─ Basel wine regions (nearby Alsace, German Pfalz)
├─ Local cheese traditions (Emmentaler, Gruyère)
├─ Historical wine trade routes in Basel
├─ Customer reviews of competitor wine tours
├─ Best photo spots for Instagram
└─ Seasonal considerations (harvest times, festivals)

Outputs: Research brief for Copywriter
```

---

### 3. COPYWRITER WORKER (The Wordsmith) ⭐

**Role:** Writes all content that converts

**Priority: THIS IS THE FIRST WORKER TO BUILD**

```python
class CopywriterWorker(dspy.Module):
    """
    Writes all content that converts.

    Trained on:
    - High-converting tour descriptions
    - Your brand voice ("sensorial stimulation")
    - Persuasion frameworks (AIDA, PAS)
    - SEO best practices

    Optimized by TextGrad based on:
    - Click-through rates
    - Time on page
    - Booking conversion
    """
```

**Example Output:**
```
Input: Wine & Cheese tour, Basel, 2.5h, €65

Copywriter AI generates:

TITLE: "Wine, Cheese & Hidden Stories: A Basel Sensory Journey"

DESCRIPTION:
"Step into Basel's secret wine culture, where Swiss precision meets
French passion. Over 2.5 hours, your expert sommelier guides you
through cobblestone alleys to tucked-away wine bars locals cherish.

Taste three exceptional wines paired with artisan cheeses while
uncovering the medieval trade routes that made Basel a wine hub.
This isn't a generic tasting—it's a conversation about terroir,
tradition, and the stories behind each sip.

Perfect for curious palates who want to taste Basel like a local."

HIGHLIGHTS:
- 3 wine tastings (Swiss, Alsatian, German varietals)
- Artisan cheese pairings from local affiniers
- Historical walking tour through Old Town
- Small groups (max 10 people) for intimate experience
- Expert sommelier with 15+ years tasting experience

STIMULUS SCORES:
TASTE    ██████████  10/10  Rich wine + cheese pairings
SIGHT    █████████░   9/10  Picturesque Old Town Basel
SOUND    ███████░░░   7/10  Ambient cafés, street sounds
THOUGHT  █████████░   9/10  Wine education, history deep-dive
CONNECT  ██████████  10/10  Intimate group, guide expertise

SEO META:
Title: "Wine & Cheese Tour Basel | Small Group Tasting Experience"
Description: "Discover Basel's wine culture on this intimate 2.5h
tour. Taste Swiss & French wines with artisan cheese pairings.
Small groups, expert guides. Book your sensory journey."
```

**Self-Improvement:**
- Sees customers click but not book → adjusts tone
- Sees certain words convert better → uses them more
- Sees questions in WhatsApp → adds FAQ preemptively

---

### 4. DESIGNER WORKER (The Visual Thinker)

**Role:** Suggests visual direction and generates layout specs

```python
class DesignerWorker(dspy.Module):
    """
    Suggests visual direction and generates layout specs.

    Cannot create images (yet) but can:
    - Recommend image types needed
    - Suggest color palettes
    - Design page layouts
    - Create component specs
    - Generate CSS for custom elements
    """
```

**Example:**
```
Input: Wine & Cheese tour page

Designer AI outputs:

VISUAL DIRECTION:
├─ Color palette: Burgundy (#722F37), Cream (#F8F4E3), Gold (#D4AF37)
├─ Imagery needed:
│  ├─ Hero: Close-up of wine swirl in glass (warm light)
│  ├─ Gallery:
│  │  ├─ Cheese board arrangement (top-down)
│  │  ├─ Basel cobblestone street
│  │  ├─ Sommelier pouring wine
│  │  └─ Group laughing at outdoor table
│  └─ Icon set: Wine bottle, cheese wheel, map, clock
│
├─ Layout suggestion:
│  [Hero image - full width]
│  [Title + Stimulus Scores - centered]
│  [Description - 2 column on desktop]
│  [Photo gallery - asymmetric grid]
│  [CTA - WhatsApp button, burgundy]
│
└─ Typography:
   ├─ Headings: Playfair Display (elegant serif)
   └─ Body: Inter (readable sans-serif)

COMPONENTS NEEDED:
1. HeroSection (image + overlay text)
2. StimulusScoreBar (animated bars)
3. HighlightGrid (3-column on desktop)
4. PhotoGallery (masonry layout)
5. WhatsAppCTA (sticky on scroll)

CSS SPECS:
[Generates actual CSS for burgundy paper-texture button]
```

---

### 5. DEVELOPER WORKER (The Builder)

**Role:** Generates actual code (Astro components, pages)

```python
class DeveloperWorker(dspy.Module):
    """
    Generates actual code (Astro components, pages).

    Takes:
    - Content from Copywriter
    - Design specs from Designer
    - Strategy from Strategist

    Outputs:
    - Complete .astro files
    - Styled components
    - Optimized for performance
    - Accessible markup
    """
```

**Example:**
```
Input: All outputs from above workers

Developer AI generates:

📄 src/pages/experiences/wine-cheese-basel.astro
📄 src/components/StimulusScoreBar.astro
📄 src/components/WhatsAppCTA.astro
📄 public/wine-cheese-hero.jpg (placeholder)
📄 src/styles/wine-tour.css

Ready to deploy. Just git commit.
```

---

### 6. SEO OPTIMIZER WORKER (The Ranker)

**Role:** Ensures every page ranks

```python
class SEOOptimizerWorker(dspy.Module):
    """
    Ensures every page ranks.

    - Keyword research
    - Meta tag generation
    - Schema markup
    - Internal linking suggestions
    - Content optimization for search intent
    """
```

---

### 7. CUSTOMER INSIGHT WORKER (The Listener)

**Role:** Analyzes customer interactions to improve everything

```python
class CustomerInsightWorker(dspy.Module):
    """
    Analyzes customer interactions to improve everything.

    Sources:
    - WhatsApp conversations
    - Booking patterns
    - Time on page
    - Scroll depth
    - Questions asked

    Outputs:
    - What customers care about most
    - Which copy resonates
    - What's missing from pages
    - Opportunities for new experiences
    """
```

**Example:**
```
Customer Insight AI analyzes 50 WhatsApp conversations:

FINDINGS:
├─ 70% ask "Is this good for non-drinkers?"
│  → Action: Add FAQ + non-alcoholic option
│
├─ 40% mention "Instagram spots"
│  → Action: Copywriter emphasizes photo opportunities
│
├─ 25% ask about weather/rain
│  → Action: Add "rain or shine" policy
│
└─ 15% ask about private groups
   → Action: Designer creates "Private Tour" CTA

OPTIMIZATION TRIGGERS:
- Trigger TextGrad to improve FAQ section
- Update Copywriter prompts to mention photos early
- Designer adds weather icons to page
```

---

## Implementation Strategy

### Phase 1: Copywriter Only (NOW)

**Why start here:**
- Highest value (content is king)
- Fastest to validate (works in isolation)
- Shows TextGrad optimization clearly
- Alex can see AI writing better than him
- Once proven, expand to other workers

**Timeline:** 1 day to working prototype

**Success Metric:** AI-generated description converts better than manual

---

### Phase 2: Add Researcher + Designer (Week 2-3)

**Why these next:**
- Researcher feeds Copywriter better data
- Designer ensures visual consistency
- Still manageable scope

**Timeline:** 1 week

**Success Metric:** New experience page created in 10 minutes (vs. 2 hours manual)

---

### Phase 3: Full System (Month 2-3)

**Add remaining workers:**
- Strategist (for positioning new experiences)
- Developer (for code generation)
- SEO (for ranking)
- Insights (for continuous improvement)

**Timeline:** 1 month

**Success Metric:** Fully automated experience creation pipeline

---

## The TextGrad Optimization Loop

After each page is live, TextGrad continuously improves it:

```
WEEK 1: Page goes live with AI-generated content
  ↓
  Collect data:
  - 100 visitors
  - 5% click WhatsApp
  - 2% actually book
  ↓
TEXTGRAD ANALYZES:
  "Why aren't more people booking?"
  ↓
  Hypothesis: Description too long, buries CTA
  ↓
  Generates improved version:
  - Shorter intro
  - CTA earlier
  - More urgency
  ↓
A/B TEST: Old vs New
  ↓
  New version: 8% click, 4% book
  ↓
KEEP NEW VERSION, continue optimizing
```

**This is the REAL moat:** Every experience gets better over time, automatically.

---

## Why This Works

### Traditional Approach:
```
You write description manually       (2 hours)
  ↓
It's okay but not great
  ↓
You're too busy to improve it
  ↓
It stays mediocre forever
```

### AI Worker Approach:
```
AI generates description             (2 minutes)
  ↓
You review and approve
  ↓
It goes live
  ↓
TextGrad optimizes based on data
  ↓
Description gets better every week
  ↓
Conversion rate increases
  ↓
More bookings with same traffic
```

---

## Key Takeaways

1. **Start with Copywriter** - Highest ROI, fastest validation
2. **Add workers incrementally** - Don't build all 7 at once
3. **TextGrad is the secret sauce** - Continuous improvement is the moat
4. **Measure everything** - Workers optimize based on metrics
5. **Your expertise trains the AI** - You're scaling yourself, not replacing

---

## Next Steps

1. Read `03-design-scrapbook-aesthetic.md` - The visual direction
2. Read `/03-AI-WORKERS/copywriter-worker.md` - Detailed implementation
3. Go to `/04-IMPLEMENTATION/phase-1-mvp.md` - Start building

---

**Remember:** The AI workers don't replace you. They scale you.
