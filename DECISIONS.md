# Key Technical Decisions

**Project:** Stimulus Collective
**Updated:** 2024-11-22

---

## Core Architecture Decisions

### Decision: Astro for Frontend ✅
**Date:** 2024-11-22
**Rationale:**
- Content-focused (perfect for experience pages)
- Fast by default (static generation)
- SEO-ready out of the box
- Simple to deploy (Netlify/Vercel)
- Component-based (reusable design system)

**Alternative Considered:** Next.js
**Why Not:** Too heavy for MVP, more complex than needed, want content-first not app-first

---

### Decision: WhatsApp-First Booking ✅
**Date:** 2024-11-22
**Rationale:**
- Fastest validation path
- Personal touch (matches brand)
- No complex calendar system needed
- Can gauge interest before building infrastructure
- Common in European tourism

**Alternative Considered:** Cal.com, Regiondo, custom booking
**Why Not:** Premature for MVP, need to validate demand first, can add later

---

### Decision: DSPy for AI Workers ✅
**Date:** 2024-11-22
**Rationale:**
- Self-improving (GEPA optimizer)
- Metric-driven optimization (not guesswork)
- Programmatic (define what you want, not how)
- Composable modules (build complex from simple)
- TextGrad integration for continuous improvement

**Alternative Considered:** Manual prompts, LangChain
**Why Not:**
- Manual prompts don't scale or improve
- LangChain is more complex, less focused on optimization

---

### Decision: JSON Database (MVP) ✅
**Date:** 2024-11-22
**Rationale:**
- Fast to prototype (no schema setup)
- Easy to edit manually (JSON files)
- Version controllable (git)
- Easy migration path to PostgreSQL later
- Perfect for 3-10 experiences

**Alternative Considered:** PostgreSQL, SQLite
**Why Not:** Overkill for 3 experiences, adds setup complexity, can migrate when proven

**Migration Trigger:** When we have >20 experiences OR need user accounts OR have complex queries

---

### Decision: Groq API (gpt-oss-120b) ✅
**Date:** 2024-11-22
**Rationale:**
- Specified in user's `.claude` config
- Fast inference
- Cost-effective for prototyping
- Good quality for content generation

**Alternative Considered:** OpenAI GPT-4, Anthropic Claude
**Why Not:** User preference already set, want to start with known config

**Note:** Can A/B test other models later with DSPy (it's model-agnostic)

---

### Decision: Scrapbook Aesthetic ✅
**Date:** 2024-11-22
**Rationale:**
- Matches brand ("sensorial", "handmade", "human-driven")
- Differentiates from generic tour sites
- Memorable (people remember unique design)
- Allows creative expression
- Fits the "experiences are memories" narrative

**Alternative Considered:** Minimal/clean design, dark mode, Airbnb-style
**Why Not:**
- Minimal feels too generic
- Want to stand out, not blend in
- Scrapbook aesthetic tells a story

**Constraint:** Must not sacrifice function for beauty (function first)

---

## Implementation Strategy Decisions

### Decision: Start with Copywriter Worker Only ✅
**Date:** 2024-11-22
**Rationale:**
- Highest value (content is king)
- Fastest to validate (works in isolation)
- Proves AI concept before building full system
- Can test TextGrad optimization loop
- Alex can see quality immediately

**Alternative Considered:** Build all 7 workers at once
**Why Not:** Too complex, can't validate each piece, risk building wrong thing

**Next Workers:** Researcher (Week 2), Designer (Week 3), then reassess

---

### Decision: Function Over Beauty ✅
**Date:** 2024-11-22
**Rationale:**
- Working AI > pretty site that doesn't work
- Need to validate demand first
- Can improve design after validation
- Avoid premature optimization

**What This Means:**
- Build working copywriter first
- Add basic Astro pages (not perfect)
- Test with real customer
- Then refine design

**Quote:** "Almost don't forget that is most important the actually things to work, than a beautiful thing that doesn't work"

---

### Decision: Bootstrap Budget (€0-500) ✅
**Date:** 2024-11-22
**Rationale:**
- Need to prove concept before spending
- Forces focus on essentials
- Free/cheap tools exist for MVP
- Can upgrade when revenue validates

**Budget Allocation:**
- Hosting: €0 (Netlify free tier)
- Domain: €15/year (.ch domain)
- Groq API: Pay-as-you-go (minimal for MVP)
- Design: €0 (handcraft components)
- **Total Month 1:** ~€20

**Upgrade Triggers:**
- Revenue >€1,000/month → Invest in paid tools
- >50 bookings/month → Consider Regiondo
- Team grows → Invest in collaboration tools

---

## Design System Decisions

### Decision: Handcrafted Components (No Tailwind/UI Library) ✅
**Date:** 2024-11-22
**Rationale:**
- Scrapbook aesthetic needs custom CSS
- Want unique look (not Bootstrap/Tailwind generic)
- Full control over interactions
- Smaller bundle size (only what we use)
- Learning opportunity

**Alternative Considered:** Tailwind CSS, shadcn/ui, DaisyUI
**Why Not:**
- Generic components don't fit scrapbook aesthetic
- Want torn edges, polaroids, handwritten touches
- These need custom CSS anyway

**Constraint:** Keep it simple, don't over-engineer

---

### Decision: Build Mobile-First ✅
**Date:** 2024-11-22
**Rationale:**
- 70% of tourism searches are mobile
- WhatsApp is mobile-native
- Forces simplicity
- Desktop is easier to enhance from mobile base

**Implementation:**
- Design for 375px width first
- Add tablet (768px) refinements
- Add desktop (1024px+) enhancements

---

## Content Strategy Decisions

### Decision: AI-Generated Descriptions, Human-Reviewed ✅
**Date:** 2024-11-22
**Rationale:**
- AI writes faster than humans
- But needs quality control initially
- Humans approve/edit before publishing
- Over time, approval becomes rarer (AI improves)

**Workflow:**
```
1. AI generates description
2. Misha/Alex reviews
3. Edit if needed
4. Approve
5. Publish
6. TextGrad learns from performance
7. AI improves for next time
```

---

### Decision: English-First, Multilingual Later ✅
**Date:** 2024-11-22
**Rationale:**
- English reaches most tourists
- Alex speaks 7 languages (can translate later)
- Don't want to build i18n before validation
- Can add German/Spanish/French after MVP proven

**Trigger for Multilingual:** When >20% of inquiries are in non-English languages

---

## Data & Analytics Decisions

### Decision: Simple Analytics (Google Analytics) ✅
**Date:** 2024-11-22
**Rationale:**
- Free
- Standard tooling
- Enough for MVP metrics
- Can upgrade to Plausible/Fathom later (privacy-focused)

**Key Metrics to Track:**
- Page views per experience
- Time on page
- Click-through rate to WhatsApp
- Bounce rate
- Traffic sources

---

### Decision: Manual Booking Tracking (Spreadsheet) ✅
**Date:** 2024-11-22
**Rationale:**
- No database yet
- Need to track conversions manually
- Simple Google Sheet works for <50 bookings
- Can migrate to CRM later

**Spreadsheet Columns:**
- Date
- Customer name
- Experience booked
- Source (how they found us)
- Revenue
- Notes

**Upgrade Trigger:** >50 bookings OR need automated reporting

---

## Security & Privacy Decisions

### Decision: No User Accounts (MVP) ✅
**Date:** 2024-11-22
**Rationale:**
- Don't need to store user data
- WhatsApp handles communication
- Reduces liability (GDPR compliance)
- Faster development

**When to Add Accounts:** If/when we build membership program

---

### Decision: Environment Variables for Secrets ✅
**Date:** 2024-11-22
**Rationale:**
- Standard practice
- Keep API keys out of git
- Easy to rotate
- Netlify/Vercel support natively

**Required Secrets:**
- `GROQ_API_KEY`
- (Future) `STRIPE_SECRET_KEY`
- (Future) `WHATSAPP_BUSINESS_TOKEN`

---

## Deployment Decisions

### Decision: Netlify for Hosting ✅
**Date:** 2024-11-22
**Rationale:**
- Free tier sufficient for MVP
- Astro first-class support
- Easy deploys (git push)
- Good performance (CDN)
- Can upgrade seamlessly

**Alternative Considered:** Vercel, Cloudflare Pages
**Why Not:** Netlify is simpler, generous free tier

---

## Future Decisions (To Be Made)

### When to Add Booking Calendar?
**Current:** WhatsApp-first
**Consider When:** >20 bookings/month AND manual scheduling becomes painful
**Options:** Cal.com (free), Regiondo (€49/month), custom build

---

### When to Add Payment Processing?
**Current:** Manual Stripe payment links
**Consider When:** >50 bookings/month
**Options:** Stripe Checkout embedded, Stripe Payment Links (current), custom checkout

---

### When to Migrate to Database?
**Current:** JSON files
**Consider When:** >20 experiences OR need complex queries OR user accounts
**Options:** PostgreSQL (Supabase free tier), SQLite (simple), keep JSON (if it works)

---

### When to Add Membership Program?
**Current:** No membership
**Consider When:** >100 customers AND >30% repeat rate AND customers asking for it
**Options:** Custom build with Stripe subscriptions, Memberful, Patreon

---

## Decision-Making Framework

When evaluating new features/technologies:

### Questions to Ask:
1. **Does this help us get the first 10 bookings?**
   - If no → defer
   - If yes → consider

2. **Can we validate without building it?**
   - If yes → validate first (talk to customers, manual process)
   - If no → build minimum version

3. **What's the cheapest way to test this?**
   - Manual > Free tool > Paid tool > Custom build

4. **Does this align with "insanely great" vision?**
   - If yes → prioritize
   - If no → question if needed

5. **Can AI workers do this better?**
   - If yes → build AI worker
   - If no → manual process or simple automation

---

## Revision History

- **2024-11-22:** Initial decisions documented
- **Future:** Update as we validate assumptions and make new decisions

---

**Remember:** Decisions aren't permanent. We're optimizing for learning speed, not perfect planning.
