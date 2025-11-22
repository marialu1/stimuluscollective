import dspy

class GenerateExperienceContent(dspy.Signature):
    """Generate compelling content for a Stimulus Collective experience.

    Brand voice:
    - Sensorial: Appeal to senses (taste, sight, sound, touch, thought)
    - Human-driven: Emphasize personal connection, guides, small groups
    - Creative: Unique angles, not generic tour descriptions
    - Excellence: High quality, attention to detail

    Goal: Make someone FEEL the experience and want to book immediately.
    Write in an evocative, immersive style that transports the reader.
    """

    # Inputs
    title: str = dspy.InputField(desc="Experience title")
    category: str = dspy.InputField(desc="Category: tours, gastronomy, or art")
    duration: str = dspy.InputField(desc="Duration (e.g., '2.5 hours')")
    price: int = dspy.InputField(desc="Price in EUR per person")
    group_size: str = dspy.InputField(desc="Max group size")
    location: str = dspy.InputField(desc="Location (e.g., 'Basel')")
    key_elements: list[str] = dspy.InputField(desc="Key elements included in the experience")

    # Outputs
    tagline: str = dspy.OutputField(desc="Evocative tagline (max 10 words, creates desire)")
    description: str = dspy.OutputField(desc="Compelling description (200-250 words). Use sensory language. Paint a vivid picture. Make them feel like they're already there. End with emotional hook.")
    highlights: list[str] = dspy.OutputField(desc="5-7 benefit-focused highlights (not just features - explain WHY it matters)")

    taste_score: int = dspy.OutputField(desc="Taste/gustatory stimulation score 1-10 (food/drink richness)")
    sight_score: int = dspy.OutputField(desc="Visual beauty score 1-10 (scenic views, aesthetics)")
    sound_score: int = dspy.OutputField(desc="Auditory richness score 1-10 (ambient sounds, music, silence)")
    thought_score: int = dspy.OutputField(desc="Cognitive challenge score 1-10 (learning, deep conversations)")
    connect_score: int = dspy.OutputField(desc="Human connection score 1-10 (intimacy, personal interaction)")
