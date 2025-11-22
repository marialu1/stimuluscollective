import dspy

class GenerateExperienceContent(dspy.Signature):
    """Generate unforgettable content for a Stimulus Collective experience.

    Brand voice - AUTHENTIC & SUBTLE:
    - Sensorial but not overwrought: "the scent of aged cheese" not "intoxicating aromas filling your senses"
    - Human without being sappy: Show warmth through specificity, not adjectives
    - Intelligent casualness: Confident but never pretentious
    - Unexpected details: The cobblestone sound, the sommelier's laugh, the 15-year cask

    AVOID:
    - Tourism clichés ("hidden gem", "off the beaten path", "like a local")
    - Overwrought sensory language ("intoxicating", "mesmerizing", "unforgettable")
    - Desperate urgency ("don't miss", "once in a lifetime")
    - Generic superlatives ("best", "unique", "amazing")

    EMBRACE:
    - Specific, concrete details that paint a scene
    - Moments of quiet observation
    - Letting the experience speak for itself
    - Subtle wit and intelligence
    - Respect for the reader's taste

    Tone: Like a Basel insider sharing a secret with a friend who appreciates good things.
    Not trying to impress - just genuinely enthusiastic about what Basel offers.
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
    tagline: str = dspy.OutputField(desc="Subtle, intelligent tagline (5-8 words). Avoid clichés. Be specific to Basel/this experience. Example: 'Three wines, one afternoon, zero pretense' not 'Discover Basel's Wine Scene'")
    description: str = dspy.OutputField(desc="Evocative description (180-220 words). CRITICAL: Write like Hemingway, not a brochure. Short sentences OK. Concrete nouns, active verbs. Start mid-scene. NO words like: curated, journey, tapestry, treasure, gem, discover, indulge, savor (as verb). YES to: specific wine names, actual street names, real details. Example opening: 'The 2019 Chasselas is colder than it should be.' not 'As we embark on a journey...' Be direct. Be specific. Be real.")
    highlights: list[str] = dspy.OutputField(desc="5-7 specific highlights. Focus on *what actually happens* not benefits. Example: 'Taste a 2019 Pinot from a family vineyard in Riehen' not 'Enjoy exclusive wine tastings'. Be concrete.")

    taste_score: int = dspy.OutputField(desc="Taste/gustatory stimulation score 1-10 (food/drink richness)")
    sight_score: int = dspy.OutputField(desc="Visual beauty score 1-10 (scenic views, aesthetics)")
    sound_score: int = dspy.OutputField(desc="Auditory richness score 1-10 (ambient sounds, music, silence)")
    thought_score: int = dspy.OutputField(desc="Cognitive challenge score 1-10 (learning, deep conversations)")
    connect_score: int = dspy.OutputField(desc="Human connection score 1-10 (intimacy, personal interaction)")
