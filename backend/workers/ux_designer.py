"""
UX/UI Designer Worker
Analyzes user experience and generates improvement recommendations.
"""

import dspy
from typing import List, Dict

class UXAnalysis(dspy.Signature):
    """Analyze user experience and generate improvement recommendations for travel/experience websites.

    Best Practices Integrated:
    - Mobile-first design (58.67% of traffic is mobile)
    - Visual hierarchy using F/Z patterns
    - Simplified navigation with clear CTAs
    - 3-click booking principle
    - WCAG accessibility compliance
    - Nielsen Norman Group principles
    - Don't Make Me Think (Steve Krug)

    Focus: Authentic, professional design - NOT crafty/gimmicky.
    """

    page_type: str = dspy.InputField(
        desc="Type of page: homepage, experience_detail, booking, corporate, about"
    )
    current_layout: str = dspy.InputField(
        desc="Description of current page structure, elements, and user flow"
    )
    user_behavior_data: str = dspy.InputField(
        desc="Analytics data: heatmaps, scroll depth, click patterns, drop-off points (or 'No data yet' for new sites)"
    )
    device_breakdown: str = dspy.InputField(
        desc="Traffic by device type: mobile %, desktop %, tablet %"
    )

    issues_found: List[str] = dspy.OutputField(
        desc="List of specific UX problems identified with evidence. Be critical but constructive. Point out things that feel amateurish, gimmicky, or try-hard."
    )
    recommendations: List[str] = dspy.OutputField(
        desc="Actionable improvements with rationale and expected impact. Focus on professional, clean design. Reference real examples from successful experience/travel sites (Airbnb Experiences, GetYourGuide, Viator)."
    )
    mobile_specific_fixes: List[str] = dspy.OutputField(
        desc="Mobile-first optimizations needed. Be specific about touch targets, thumb zones, load times."
    )
    accessibility_issues: List[str] = dspy.OutputField(
        desc="WCAG compliance problems and fixes. Check contrast ratios, keyboard navigation, screen reader compatibility."
    )
    priority_score: float = dspy.OutputField(
        desc="Overall priority score 1-10 based on user impact (1=low, 10=critical)"
    )


class UXDesignerWorker(dspy.Module):
    """UX/UI Designer AI Worker using Chain of Thought reasoning."""

    def __init__(self):
        super().__init__()
        self.analyze = dspy.ChainOfThought(UXAnalysis)

    def forward(self, page_type: str, current_layout: str,
                user_behavior_data: str = "No data yet",
                device_breakdown: str = "mobile: 60%, desktop: 35%, tablet: 5%"):
        result = self.analyze(
            page_type=page_type,
            current_layout=current_layout,
            user_behavior_data=user_behavior_data,
            device_breakdown=device_breakdown
        )
        return result
