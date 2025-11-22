"""Test the DSPy copywriter worker."""

import dspy
from workers.copywriter import ExperienceCopywriter
from config import GROQ_API_KEY, DSPY_LM_MODEL
import json

def main():
    print("🚀 Testing Stimulus Collective AI Copywriter\n")

    # Configure DSPy
    print(f"📡 Connecting to {DSPY_LM_MODEL}...")
    lm = dspy.LM(DSPY_LM_MODEL, api_key=GROQ_API_KEY)
    dspy.configure(lm=lm)
    print("✅ DSPy configured\n")

    # Initialize copywriter
    print("🤖 Initializing AI Copywriter...")
    copywriter = ExperienceCopywriter()
    print("✅ Copywriter ready\n")

    # Test with Wine Tour
    print("📝 Generating content for Wine & Cheese Tour...")
    print("-" * 60)

    content = copywriter.forward(
        title="Wine, Cheese & History Tour",
        category="tours",
        duration="2.5 hours",
        price=65,
        group_size="Max 10 people",
        location="Basel",
        key_elements=[
            "3 wine tastings (Swiss, Alsatian, German varietals)",
            "Artisan cheese pairings from local affiniers",
            "Historical walking tour through Old Town Basel",
            "Expert sommelier guide with 15+ years experience",
            "Small intimate groups for personal attention"
        ]
    )

    print("\n✅ Content generated!\n")
    print("=" * 60)
    print("TAGLINE:")
    print(f'"{content["tagline"]}"')
    print("\n" + "=" * 60)
    print("DESCRIPTION:")
    print(content["description"])
    print("\n" + "=" * 60)
    print("HIGHLIGHTS:")
    for i, highlight in enumerate(content["highlights"], 1):
        print(f"{i}. {highlight}")
    print("\n" + "=" * 60)
    print("STIMULUS SCORES:")
    for dimension, score in content["stimulus_scores"].items():
        bar = "█" * score + "░" * (10 - score)
        print(f"{dimension.upper():8} {bar} {score}/10")
    print("=" * 60)

    # Save to file for inspection
    with open("generated_content_sample.json", "w") as f:
        json.dump(content, f, indent=2)
    print("\n💾 Full content saved to: generated_content_sample.json")

if __name__ == "__main__":
    main()
