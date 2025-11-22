import os
from dotenv import load_dotenv

load_dotenv()

# Groq configuration (using llama-3.3-70b as per your .claude config preference for groq)
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL = "groq/llama-3.3-70b-versatile"

# DSPy configuration
DSPY_LM_MODEL = GROQ_MODEL
