import json, os, re, uuid
from typing import Dict, List, Any
from config import settings


SYSTEM_GEN = (
    "You are an NPC character generator. Create unique, lore-consistent names and details "
    "based ONLY on the STORY context. Always return strict JSON that validates."
)

def _load_roster() -> List[Dict[str, Any]]:
    path = settings.SAVE_PATH
    if not os.path.exists(path):
        return []
    
    roster: List[Dict[str, Any]] = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    roster.append(json.load(line))
                except json.JSONDecodeError:
                    continue
    except OSError:
        # if file can't be opened/read treat as empty
        return []
    
    return roster

def _save_to_roster(entry: Dict[str, Any]):
    path = settings.SAVE_PATH
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        
def _exisitng_names_lower() -> set:
    return {e.get("name","").lower() for e in _load_roster()}