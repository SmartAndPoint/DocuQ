import os


class Config:
    BOT_ID = os.environ.get("TELEGRAM_BOT_ID")
    OPENAI_KEY = os.environ.get("OPENAI_API_KEY")
    PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
    ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
