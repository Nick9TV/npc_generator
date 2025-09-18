import os
from dotenv import load_dotenv


load_dotenv()

class settings:
    OPEN_API_KEY = os.getenv("OPEN_API_KEY")
    
    CHUNK_SIZE = os.getenv("CHUNK_SIZE")
    
    CHUNK_OVERLAP = os.getenv("CHUNK_OVERLAP")
    
    INDEX_PATH = os.getenv("INDEX_PATH")