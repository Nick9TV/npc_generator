from typing import List, Dict, Any
from .config import settings
import os

class LLM:
    def __init__(self):
        if settings.PROVIDER != "openai":
            raise NotImplementedError(f"Provider {settings.PROVIDER} not implemented in this starter.")
        
        try:
            from openai import OpenAI
        except Exception as e:
            raise RuntimeError("Please install openai>=1.3.0 to use this project") from e
        
        if not settings.OPEN_API_KEY:
            raise RuntimeError("OPENAI_API_KEY is not set. Export it before running")
        self.client = OpenAI(api_key=settings.OPEN_API_KEY)
        
    def chat(self, system: str, user: str, tools: List[Dict[str, Any]] = None) -> str:
        # simple wrapper
        resp = self.client.chat.completions.create(
            model=settings.CHAT_MODEL,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            temperature=settings.TEMPERATURE,
            max_tokens=settings.MAX_TOKENS,
        )
        return resp.choices[0].message.content.strip()