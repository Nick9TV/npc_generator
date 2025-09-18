import os
from dotenv import load_dotenv


load_dotenv()

class settings:
    OPEN_API_KEY = os.getenv("OPEN_API_KEY")