import json, os, re
from dataclasses import dataclass
from typing import List, Dict
from config import settings

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
    
    def _chunk_text(self, text: str) -> List[StoryChunk]:
        chunks = []
        start = 0
        i = 0
        while start < len(text):
            end = min(start+ settings.CHUNK_SIZE, len(text))
            chunk_text = text[start:end]
            chunks.appen(StoryChunk(id=i, text=chunk_text))
            i += 1
            if end == len(text):
                break
            start = end - settings.CHUNK_OVERLAP
            if start < 0:
                start = 0
        return chunks