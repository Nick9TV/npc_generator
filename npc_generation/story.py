import json, os, re
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class StoryChunk:
    id: int
    text: str
    
class StoryIndex:
    def __init__(self, story_path: str):
        self.story_path = story_path
        self.text = self._load_story(story_path)
        self.chunks = self._chunk_text(self.text)
        self._save_index()
        
    def _load_story(self, path:str) -> str:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Story file not found: {path}")
        with open(path, "r", encoding="utf-8") as f:
            txt = f.read()
        # normalize whitespace
        txt = re.sub(r"\s+"," ", txt).strip()
        return txt
    