"""
Tech Architect Worker
Audits technical performance and generates optimization plan.
"""

import dspy
from typing import List, Dict

class TechAudit(dspy.Signature):
    """Audit technical performance and generate optimization plan.

    Best Practices Integrated:
    - Core Web Vitals optimization (LCP < 2.5s, FID < 100ms, CLS < 0.1)
    - Astro/JAMstack architecture (zero-JS by default)
    - Image optimization (WebP, AVIF, lazy loading)
    - Schema.org structured data for rich snippets
    - CDN edge deployment
    - Lighthouse Performance 90+

    Philosophy: Fast is a feature. Every 100ms delay = 1% drop in conversions.
    """

    page_url: str = dspy.InputField(
        desc="URL being analyzed"
    )
    current_stack: str = dspy.InputField(
        desc="Current tech stack: framework, hosting, integrations"
    )
    lighthouse_report: str = dspy.InputField(
        desc="Lighthouse audit results: performance, accessibility, best practices, SEO scores. Or 'Not run yet' for planning."
    )
    bundle_analysis: str = dspy.InputField(
        desc="JavaScript bundle size and composition. Or 'Not analyzed yet'."
    )

    performance_issues: List[str] = dspy.OutputField(
        desc="Specific performance bottlenecks with metrics. Reference Core Web Vitals."
    )
    code_fixes: List[str] = dspy.OutputField(
        desc="Concrete code changes needed with examples. Be specific: file names, line numbers if possible, actual code snippets."
    )
    seo_recommendations: List[str] = dspy.OutputField(
        desc="Technical SEO improvements: schema markup, meta tags, sitemap, robots.txt"
    )
    core_web_vitals_fixes: Dict[str, str] = dspy.OutputField(
        desc="Specific fixes for LCP (Largest Contentful Paint), FID (First Input Delay), CLS (Cumulative Layout Shift)"
    )
    estimated_score_improvement: int = dspy.OutputField(
        desc="Expected Lighthouse performance score improvement after fixes (current → target)"
    )


class TechArchitectWorker(dspy.Module):
    """Tech Architect AI Worker for performance optimization."""

    def __init__(self):
        super().__init__()
        self.audit = dspy.ChainOfThought(TechAudit)

    def forward(self, page_url: str, current_stack: str,
                lighthouse_report: str = "Not run yet",
                bundle_analysis: str = "Not analyzed yet"):
        result = self.audit(
            page_url=page_url,
            current_stack=current_stack,
            lighthouse_report=lighthouse_report,
            bundle_analysis=bundle_analysis
        )
        return result
