"""
UX/UI Designer Worker - Enhanced with brand context and multi-step reasoning
"""

import dspy
from typing import List, Dict

class UXAnalysisStep1(dspy.Signature):
    """First step: Deep analysis of current state with brand context.

    Brand Context - Stimulus Collective:
    - Boutique experience company in Basel, Switzerland
    - Handmade, artisanal aesthetic (baby pink #FFB3C6, wine red #B71C1C)
    - Small groups (max 8 people), expert guides
    - Wine, chocolate, and art tours
    - Target: sophisticated travelers who value authenticity over tourist traps
    - Voice: warm, confident, unpretentious
    - NOT crafty/DIY - tasteful artisanal

    Design Philosophy:
    - Clean + personality (not clinical, not cluttered)
    - Handwritten accents (Caveat font) + elegant serif (Playfair Display)
    - Ripped paper effects (subtle, not overdone)
    - WhatsApp-first booking (European convenience)
    """

    page_type: str = dspy.InputField()
    current_layout: str = dspy.InputField()
    user_behavior_data: str = dspy.InputField()
    device_breakdown: str = dspy.InputField()

    # Deep analysis outputs
    what_works: List[str] = dspy.OutputField(
        desc="What's already good and aligns with brand. Be specific."
    )
    critical_issues: List[str] = dspy.OutputField(
        desc="Deal-breakers that hurt conversions or trust. Evidence-based."
    )
    brand_misalignments: List[str] = dspy.OutputField(
        desc="Elements that contradict the artisanal-but-sophisticated positioning"
    )
    missed_opportunities: List[str] = dspy.OutputField(
        desc="Low-hanging fruit we're not leveraging"
    )

class UXAnalysisStep2(dspy.Signature):
    """Second step: Solution brainstorming with specific examples."""

    analysis: str = dspy.InputField(desc="Results from step 1")

    # Solution generation
    quick_wins: List[Dict[str, str]] = dspy.OutputField(
        desc="List of dicts with 'change' and 'impact' keys. Changes that take <1 hour but move the needle."
    )
    major_improvements: List[Dict[str, str]] = dspy.OutputField(
        desc="Bigger changes with high ROI. Include 'change', 'why', 'example' (reference real sites)"
    )
    mobile_optimizations: List[Dict[str, str]] = dspy.OutputField(
        desc="Mobile-specific fixes with 'issue', 'fix', 'metric_impact'"
    )
    accessibility_fixes: List[Dict[str, str]] = dspy.OutputField(
        desc="WCAG issues with 'problem', 'solution', 'compliance_level' (A/AA/AAA)"
    )

class UXAnalysisStep3(dspy.Signature):
    """Third step: Prioritization and action plan."""

    solutions: str = dspy.InputField(desc="Results from step 2")

    # Prioritized action plan
    do_now: List[str] = dspy.OutputField(
        desc="Top 3 changes to implement immediately (high impact, low effort)"
    )
    do_next: List[str] = dspy.OutputField(
        desc="Next 5 improvements for the roadmap"
    )
    do_later: List[str] = dspy.OutputField(
        desc="Nice-to-haves for future iterations"
    )
    avoid: List[str] = dspy.OutputField(
        desc="Common mistakes to avoid (over-decoration, feature creep, etc.)"
    )
    priority_score: float = dspy.OutputField(
        desc="Overall urgency 1-10 (1=polish, 10=broken)"
    )

class UXDesignerWorker(dspy.Module):
    """Enhanced UX Designer with multi-step reasoning and brand awareness."""

    def __init__(self):
        super().__init__()
        self.step1 = dspy.ChainOfThought(UXAnalysisStep1)
        self.step2 = dspy.ChainOfThought(UXAnalysisStep2)
        self.step3 = dspy.ChainOfThought(UXAnalysisStep3)

    def forward(self, page_type: str, current_layout: str,
                user_behavior_data: str = "No data yet",
                device_breakdown: str = "mobile: 60%, desktop: 35%, tablet: 5%"):

        # Step 1: Deep analysis
        analysis = self.step1(
            page_type=page_type,
            current_layout=current_layout,
            user_behavior_data=user_behavior_data,
            device_breakdown=device_breakdown
        )

        # Step 2: Solution generation
        analysis_summary = f"""
        What works: {analysis.what_works}
        Critical issues: {analysis.critical_issues}
        Brand misalignments: {analysis.brand_misalignments}
        Missed opportunities: {analysis.missed_opportunities}
        """

        solutions = self.step2(analysis=analysis_summary)

        # Step 3: Prioritization
        solutions_summary = f"""
        Quick wins: {solutions.quick_wins}
        Major improvements: {solutions.major_improvements}
        Mobile optimizations: {solutions.mobile_optimizations}
        Accessibility fixes: {solutions.accessibility_fixes}
        """

        action_plan = self.step3(solutions=solutions_summary)

        # Combine all results
        return {
            "analysis": analysis,
            "solutions": solutions,
            "action_plan": action_plan
        }
