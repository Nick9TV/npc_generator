import json, os, re
from dataclasses import dataclass
from typing import List, Dict
from .config import settings

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
    
    def _save_index(self):
        os.makedirs(os.path.dirname(settings.INDEX_PATH), exist_ok=True)
        data = {"story_path": self.story_path, "num_chunks": len(self.chunks)}
        with open(settings.INDEX_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    def contex(self) -> str:
        # for simplicity import full story because its short
        return self.text
        
    def short_context(self) -> str:
        # use frist fiew chunks to keep prompt smaller
        first_chunks = " ".join(c.text for c in self.chunks[:3])
        return first_chunks