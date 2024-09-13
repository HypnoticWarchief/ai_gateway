import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Fetch environment variables with fallback defaults
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "default_model")
DEFAULT_MAX_TOKENS = int(os.getenv("DEFAULT_MAX_TOKENS", 100))  # Cast to int
DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", 0.7))  # Cast to float
GUARDRAILS = os.getenv("GUARDRAILS",False)

