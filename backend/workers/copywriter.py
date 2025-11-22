import dspy
from .signatures import GenerateExperienceContent

class ExperienceCopywriter(dspy.Module):
    """AI worker that generates compelling experience content.

    Uses DSPy ChainOfThought to reason about the best way to present
    each experience based on its unique characteristics.
    """

    def __init__(self):
        super().__init__()
        self.generate = dspy.ChainOfThought(GenerateExperienceContent)

    def forward(self, **kwargs):
        """Generate content for an experience.

        Args:
            title: Experience title
            category: Category (tours/gastronomy/art)
            duration: Duration string
            price: Price in EUR
            group_size: Max group size
            location: Location
            key_elements: List of what's included

        Returns:
            dict with tagline, description, highlights, stimulus_scores
        """
        result = self.generate(**kwargs)

        # Format output
        return {
            "tagline": result.tagline,
            "description": result.description,
            "highlights": result.highlights,
            "stimulus_scores": {
                "taste": result.taste_score,
                "sight": result.sight_score,
                "sound": result.sound_score,
                "thought": result.thought_score,
                "connect": result.connect_score,
            }
        }
