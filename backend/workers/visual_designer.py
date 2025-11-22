"""
Visual Designer Worker
Audits visual design for brand consistency and professional hierarchy.
"""

import dspy
from typing import List

class VisualAudit(dspy.Signature):
    """Audit visual design for brand consistency and hierarchy.

    Best Practices Integrated:
    - Visual hierarchy principles (size, contrast, color, spacing)
    - F/Z pattern layout optimization
    - White space and breathing room
    - High-quality aspirational imagery
    - Brand consistency (67% of decisions affected by familiarity)
    - Swiss Design principles (Basel is in Switzerland!)
    - Less is more - eliminate unnecessary decorative elements

    Critical Eye: Point out when design feels amateurish, cluttered, or trying too hard.
    Reference: Airbnb, Stripe, Linear, Vercel - clean, professional, confident.
    """

    page_screenshot_description: str = dspy.InputField(
        desc="Detailed description of page visual elements and layout. Be specific about colors, fonts, spacing, decorative elements."
    )
    brand_guidelines: str = dspy.InputField(
        desc="Brand colors, typography, imagery style, tone. What feeling should the design evoke?"
    )
    competitor_references: List[str] = dspy.InputField(
        desc="Reference designs from competitors or inspirations (URLs or descriptions)"
    )

    hierarchy_issues: List[str] = dspy.OutputField(
        desc="Visual hierarchy problems affecting user attention. What fights for attention? What's buried?"
    )
    brand_deviations: List[str] = dspy.OutputField(
        desc="Inconsistencies with brand guidelines or professional standards"
    )
    design_recommendations: List[str] = dspy.OutputField(
        desc="Specific visual improvements with rationale. Focus on REMOVING clutter, not adding decoration. Simplify, don't complexify."
    )
    color_improvements: List[str] = dspy.OutputField(
        desc="Color contrast and palette recommendations. Check WCAG AA compliance (4.5:1 for text)."
    )
    typography_fixes: List[str] = dspy.OutputField(
        desc="Font, sizing, and readability improvements. Avoid using too many fonts (max 2-3 families)."
    )


class VisualDesignerWorker(dspy.Module):
    """Visual Designer AI Worker for brand consistency."""

    def __init__(self):
        super().__init__()
        self.audit = dspy.ChainOfThought(VisualAudit)

    def forward(self, page_screenshot_description: str, brand_guidelines: str,
                competitor_references: list = None):
        if competitor_references is None:
            competitor_references = [
                "Airbnb Experiences - clean, photo-first, minimal UI",
                "GetYourGuide - professional, trustworthy, clear hierarchy"
            ]

        result = self.audit(
            page_screenshot_description=page_screenshot_description,
            brand_guidelines=brand_guidelines,
            competitor_references=competitor_references
        )
        return result
