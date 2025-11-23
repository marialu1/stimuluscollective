"""
Visual Designer Worker - Enhanced with brand examples and multi-step design process
"""

import dspy
from typing import List, Dict

class VisualAuditStep1(dspy.Signature):
    """First step: Visual inventory and brand alignment check.

    Brand Identity - Stimulus Collective:
    - Colors: Baby pink (#FFB3C6) background, wine red (#B71C1C) accents
    - Typography: Playfair Display (elegant serif), Caveat (handwritten warmth), Inter (body)
    - Aesthetic: Artisanal but sophisticated (NOT crafty/DIY)
    - Elements: Ripped paper effects, handwritten underlines, WhatsApp message prints
    - Inspiration: Basel's Swiss precision + warmth of handmade experiences
    - Tone: Confident, warm, unpretentious

    Good Examples We've Approved:
    - Handwritten Caveat titles with subtle underlines
    - Ripped paper clip-path on CTA buttons (not overdone)
    - WhatsApp carousel with realistic message bubbles
    - Playfair Display for main headlines (72px, bold)
    - Clean white cards on pink background

    What to Avoid:
    - Generic corporate blues/greys
    - Too many decorative elements competing for attention
    - Overly literal scrapbook aesthetics
    - Sacrificing readability for style
    """

    page_screenshot_description: str = dspy.InputField()
    brand_guidelines: str = dspy.InputField()
    competitor_references: List[str] = dspy.InputField()

    # Visual inventory
    color_usage: Dict[str, str] = dspy.OutputField(
        desc="Dict of color purposes: {'primary': 'where used', 'accent': 'where used'}. Check consistency."
    )
    typography_breakdown: Dict[str, str] = dspy.OutputField(
        desc="Font usage: {'headings': 'font + size', 'body': 'font + size'}. Too many fonts?"
    )
    visual_weight_distribution: List[str] = dspy.OutputField(
        desc="What elements dominate attention? Is it intentional?"
    )
    brand_alignment_score: float = dspy.OutputField(
        desc="1-10 how well design matches Stimulus Collective identity"
    )

class VisualAuditStep2(dspy.Signature):
    """Second step: Problem identification with specific fixes."""

    visual_inventory: str = dspy.InputField(desc="Results from step 1")

    # Specific problems + solutions
    hierarchy_problems: List[Dict[str, str]] = dspy.OutputField(
        desc="List of dicts: {'issue': 'what's wrong', 'fix': 'specific CSS change', 'why': 'rationale'}"
    )
    color_issues: List[Dict[str, str]] = dspy.OutputField(
        desc="Color problems: {'issue': 'e.g. low contrast', 'current': '#HEX', 'suggested': '#HEX', 'wcag_ratio': '4.5:1'}"
    )
    typography_improvements: List[Dict[str, str]] = dspy.OutputField(
        desc="Font fixes: {'element': 'h1', 'current': 'font details', 'better': 'improved specs', 'reason': 'why'}"
    )
    spacing_refinements: List[Dict[str, str]] = dspy.OutputField(
        desc="White space issues: {'location': 'where', 'current': 'px value', 'better': 'px value'}"
    )

class VisualAuditStep3(dspy.Signature):
    """Third step: Comprehensive design recommendations with code snippets."""

    problems: str = dspy.InputField(desc="Results from step 2")

    # Actionable recommendations
    quick_css_fixes: List[str] = dspy.OutputField(
        desc="Copy-paste CSS snippets that improve design immediately"
    )
    major_redesign_ideas: List[Dict[str, str]] = dspy.OutputField(
        desc="Bigger changes: {'component': 'what', 'current_approach': 'desc', 'better_approach': 'desc', 'example_site': 'reference'}"
    )
    before_after_mockup_descriptions: List[Dict[str, str]] = dspy.OutputField(
        desc="Visual descriptions: {'element': 'what', 'before': 'current state', 'after': 'improved state'}"
    )
    do_not_change: List[str] = dspy.OutputField(
        desc="Elements that are working well - preserve these!"
    )

class VisualDesignerWorker(dspy.Module):
    """Enhanced Visual Designer with multi-step audit and code-ready outputs."""

    def __init__(self):
        super().__init__()
        self.step1 = dspy.ChainOfThought(VisualAuditStep1)
        self.step2 = dspy.ChainOfThought(VisualAuditStep2)
        self.step3 = dspy.ChainOfThought(VisualAuditStep3)

    def forward(self, page_screenshot_description: str, brand_guidelines: str,
                competitor_references: list = None):

        if competitor_references is None:
            competitor_references = [
                "Airbnb Experiences - photo-first, clean, minimal chrome",
                "Kinfolk Magazine - artisanal aesthetic done right",
                "Ace Hotel - boutique warmth + professional polish"
            ]

        # Step 1: Visual inventory
        inventory = self.step1(
            page_screenshot_description=page_screenshot_description,
            brand_guidelines=brand_guidelines,
            competitor_references=competitor_references
        )

        # Step 2: Problem diagnosis
        inventory_summary = f"""
        Color usage: {inventory.color_usage}
        Typography: {inventory.typography_breakdown}
        Visual weight: {inventory.visual_weight_distribution}
        Brand alignment: {inventory.brand_alignment_score}/10
        """

        problems = self.step2(visual_inventory=inventory_summary)

        # Step 3: Solutions with code
        problems_summary = f"""
        Hierarchy problems: {problems.hierarchy_problems}
        Color issues: {problems.color_issues}
        Typography improvements: {problems.typography_improvements}
        Spacing refinements: {problems.spacing_refinements}
        """

        recommendations = self.step3(problems=problems_summary)

        # Combine all results
        return {
            "inventory": inventory,
            "problems": problems,
            "recommendations": recommendations
        }
