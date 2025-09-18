import os
from dotenv import load_dotenv

# importing data from .env file
load_dotenv()

class settings:
    # OpenAI config
    OPEN_API_KEY = os.getenv("OPEN_API_KEY") # paste your Api key
    
    # Provider selection
    PROVIDER = os.getenv("PROVIDER").lower() # openai
    
    # Chunking
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE")) # 1200
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP")) # 200
    
    # Storage
    INDEX_PATH = os.getenv("INDEX_PATH") # data/index.json
    
    # Model choices
    CHAT_MODEL = os.getenv("CHAT_MODEL")  # gpt-4o-mini
    
    # Generation defaults
    TEMPERATURE = float(os.getenv("TEMPERATURE")) # 0.7
    MAX_TOKENS = int(os.getenv("MAX_TOKENS")) # 600