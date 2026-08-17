import os

from agents import set_default_openai_key
from dotenv import load_dotenv


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is not set.")

set_default_openai_key(OPENAI_API_KEY)