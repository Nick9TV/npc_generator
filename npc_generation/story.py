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