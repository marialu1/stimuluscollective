"""
Run all AI workers to analyze the current Stimulus Collective site.
Generates a comprehensive report with recommendations.
"""

import dspy
import json
from datetime import datetime
from config import GROQ_API_KEY, DSPY_LM_MODEL

# Import workers
from workers.ux_designer import UXDesignerWorker
from workers.visual_designer import VisualDesignerWorker
from workers.tech_architect import TechArchitectWorker

# Configure DSPy
print(f"📡 Connecting to {DSPY_LM_MODEL}...")
lm = dspy.LM(DSPY_LM_MODEL, api_key=GROQ_API_KEY)
dspy.configure(lm=lm)
print("✅ DSPy configured\n")

# Initialize workers
print("🤖 Initializing AI Workers...")
ux_worker = UXDesignerWorker()
visual_worker = VisualDesignerWorker()
tech_worker = TechArchitectWorker()
print("✅ All workers ready\n")

print("=" * 80)
print("STIMULUS COLLECTIVE - AI DESIGN AUDIT")
print("=" * 80)
print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Analyzing: http://100.118.170.68:4322")
print("=" * 80)
print()

# ============================================================================
# 1. UX/UI DESIGNER ANALYSIS
# ============================================================================
print("\n" + "━" * 80)
print("🎨 UX/UI DESIGNER ANALYSIS")
print("━" * 80)

current_homepage_layout = """
CURRENT HOMEPAGE LAYOUT:

Header/Hero (Grid 2 columns):
- Left: Logo as red stamp circle with "Stimulus Collective" in Caveat cursive
  - Headline: "Basel, but not the usual tour" (Basel has hand-drawn red underline)
  - Tagline: "Wine. Chocolate. Art. The kind of afternoons that stick with you."
  - CTA button: "See what we do →" (red, irregular edges, tape decoration)

- Right: 3 Polaroid cards stacked vertically, floating animation
  - Each has: photo, handwritten caption, masking tape on top
  - Cards tilted at different angles (-5deg, 3deg, -2deg)
  - Hover: straightens and lifts up

Torn paper divider (jagged clip-path polygon)

Experience Cards Section:
- Title: "What we offer" in Caveat cursive (3rem)
- 3 cards in grid layout
  - Each card: cream background, irregular edges (clip-path), paper clip decoration top-right
  - Contains: category tag, title, duration, price, "Details →" button
  - Hover: lifts up and rotates slightly

Footer: "Made in Basel 🇨🇭" + WhatsApp link

DESIGN ELEMENTS USED:
- Paper texture overlay (repeating linear gradients)
- Caveat font (Google Fonts cursive) for handwritten feel
- Clip-path polygons for irregular "hand-cut" edges
- Drop-shadow filters for paper lift effects
- Masking tape decorations (rgba semi-transparent yellow)
- Paper clips (CSS borders, rounded)
- F8F4F0 cream background
- E53935 red accent color
"""

ux_result = ux_worker(
    page_type="homepage",
    current_layout=current_homepage_layout,
    user_behavior_data="No data yet - new site launch",
    device_breakdown="Estimated: mobile 60%, desktop 35%, tablet 5%"
)

print("\n🔍 ISSUES FOUND:")
for i, issue in enumerate(ux_result.issues_found, 1):
    print(f"{i}. {issue}")

print("\n💡 RECOMMENDATIONS:")
for i, rec in enumerate(ux_result.recommendations, 1):
    print(f"{i}. {rec}")

print("\n📱 MOBILE-SPECIFIC FIXES:")
for i, fix in enumerate(ux_result.mobile_specific_fixes, 1):
    print(f"{i}. {fix}")

print("\n♿ ACCESSIBILITY ISSUES:")
for i, issue in enumerate(ux_result.accessibility_issues, 1):
    print(f"{i}. {issue}")

print(f"\n⚠️  PRIORITY SCORE: {ux_result.priority_score}/10")

# ============================================================================
# 2. VISUAL DESIGNER ANALYSIS
# ============================================================================
print("\n" + "━" * 80)
print("👁️  VISUAL DESIGNER ANALYSIS")
print("━" * 80)

visual_description = """
CURRENT VISUAL DESIGN:

TYPOGRAPHY:
- Headings: Caveat cursive (Google Fonts) - handwritten style
- Body: Inter (system fallback)
- Logo: Caveat 2.5rem
- Main headline: Inter 3rem, 800 weight
- Section title: Caveat 3rem
- Tagline: Inter 1.25rem

COLORS:
- Background: #F8F4F0 (cream/beige)
- Accent: #E53935 (red)
- Text: #2D2A26 (dark brown)
- Secondary text: #666 (gray)
- Card background: #FFFAF8 (off-white)
- Category tag background: #FFF3F0 (light pink)
- Borders: #E8E8E8 (light gray)

DECORATIVE ELEMENTS:
- Paper texture overlay (subtle grid pattern, 0.5 opacity)
- Torn paper divider (complex clip-path polygon with 100+ points)
- Masking tape (rgba(255, 235, 200, 0.7), rotated ±5deg)
- Paper clips (CSS borders, 30x50px, #999, rotated 5deg, 0.6 opacity)
- Irregular edges via clip-path on buttons and cards
- Drop-shadow filters for lift effects
- Polaroid frames (12px padding, 40px bottom padding)
- Red circle stamp border around logo (4px, rotated -5deg, 0.6 opacity)
- Hand-drawn underline (SVG path, red, 0.8 opacity)

LAYOUT:
- Max-width: 1200px
- Grid: 2 columns (hero), auto-fit minmax(300px, 1fr) for cards
- Padding: 2rem container, 4rem section vertical
- Gaps: 4rem hero, 2rem cards
- Animations: floating polaroids (6s infinite), fadeInUp for cards

IMAGERY:
- Polaroids: 200x200px, filter: saturate(1.1) contrast(1.05)
- Placeholder images (not real photos)
"""

brand_guidelines = """
STIMULUS COLLECTIVE BRAND:
- Industry: Premium experience tours in Basel
- Target: Sophisticated travelers, locals seeking quality, corporate teams
- Tone: Authentic, intelligent, Basel insider (not tourist-trap)
- Feeling: Trustworthy, professional, memorable
- NOT: Crafty, gimmicky, DIY, scrapbooking, childish

DESIRED AESTHETIC:
- Clean, modern, confident
- Emphasis on photography and experiences
- Swiss design principles (precision, clarity, functionality)
- Subtle warmth without being kitschy
- Professional enough for corporate bookings
"""

visual_result = visual_worker(
    page_screenshot_description=visual_description,
    brand_guidelines=brand_guidelines,
    competitor_references=[
        "Airbnb Experiences - clean, photo-first, professional",
        "GetYourGuide - trustworthy, clear, European aesthetic",
        "Viator - simple, conversion-focused, credible"
    ]
)

print("\n🔍 HIERARCHY ISSUES:")
for i, issue in enumerate(visual_result.hierarchy_issues, 1):
    print(f"{i}. {issue}")

print("\n❌ BRAND DEVIATIONS:")
for i, dev in enumerate(visual_result.brand_deviations, 1):
    print(f"{i}. {dev}")

print("\n✨ DESIGN RECOMMENDATIONS:")
for i, rec in enumerate(visual_result.design_recommendations, 1):
    print(f"{i}. {rec}")

print("\n🎨 COLOR IMPROVEMENTS:")
for i, imp in enumerate(visual_result.color_improvements, 1):
    print(f"{i}. {imp}")

print("\n📝 TYPOGRAPHY FIXES:")
for i, fix in enumerate(visual_result.typography_fixes, 1):
    print(f"{i}. {fix}")

# ============================================================================
# 3. TECH ARCHITECT ANALYSIS
# ============================================================================
print("\n" + "━" * 80)
print("⚙️  TECH ARCHITECT ANALYSIS")
print("━" * 80)

tech_result = tech_worker(
    page_url="http://100.118.170.68:4322",
    current_stack="Astro 5.16.0, static build, dev server on Hetzner, port 4322",
    lighthouse_report="Not run yet - in development",
    bundle_analysis="Astro default - minimal JS, Web Fonts (Caveat + Inter from Google)"
)

print("\n⚠️  PERFORMANCE ISSUES:")
for i, issue in enumerate(tech_result.performance_issues, 1):
    print(f"{i}. {issue}")

print("\n🔧 CODE FIXES:")
for i, fix in enumerate(tech_result.code_fixes, 1):
    print(f"{i}. {fix}")

print("\n🔍 SEO RECOMMENDATIONS:")
for i, rec in enumerate(tech_result.seo_recommendations, 1):
    print(f"{i}. {rec}")

print("\n⚡ CORE WEB VITALS FIXES:")
for metric, fix in tech_result.core_web_vitals_fixes.items():
    print(f"  {metric}: {fix}")

print(f"\n📊 ESTIMATED SCORE IMPROVEMENT: {tech_result.estimated_score_improvement}")

# ============================================================================
# SAVE REPORT
# ============================================================================
print("\n" + "=" * 80)
print("📄 SAVING FULL REPORT")
print("=" * 80)

report = {
    "timestamp": datetime.now().isoformat(),
    "site_url": "http://100.118.170.68:4322",
    "ux_analysis": {
        "issues_found": ux_result.issues_found,
        "recommendations": ux_result.recommendations,
        "mobile_fixes": ux_result.mobile_specific_fixes,
        "accessibility_issues": ux_result.accessibility_issues,
        "priority_score": ux_result.priority_score
    },
    "visual_analysis": {
        "hierarchy_issues": visual_result.hierarchy_issues,
        "brand_deviations": visual_result.brand_deviations,
        "design_recommendations": visual_result.design_recommendations,
        "color_improvements": visual_result.color_improvements,
        "typography_fixes": visual_result.typography_fixes
    },
    "tech_analysis": {
        "performance_issues": tech_result.performance_issues,
        "code_fixes": tech_result.code_fixes,
        "seo_recommendations": tech_result.seo_recommendations,
        "core_web_vitals_fixes": tech_result.core_web_vitals_fixes,
        "estimated_improvement": tech_result.estimated_score_improvement
    }
}

with open("site_analysis_report.json", "w") as f:
    json.dump(report, f, indent=2)

print("\n✅ Report saved to: site_analysis_report.json")
print("\n🎯 NEXT STEPS:")
print("1. Review UX recommendations (Priority: {}/10)".format(ux_result.priority_score))
print("2. Implement visual simplifications (remove craft elements)")
print("3. Apply performance optimizations")
print("4. Re-run analysis after changes")
print("\n" + "=" * 80)
