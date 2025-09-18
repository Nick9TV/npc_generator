import json, os, re, uuid
from typing import Dict, List, Any
from config import settings
from .story import StoryIndex
from .llm import LLM

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

def generate_charactre(index: StoryIndex, request: str, ensure_unique: bool=True, save: bool=True) -> Dict[str, Any]:
    llm = LLM
    story = index.contex()
    
    # uniqueness promt hint
    existing = list(_exisitng_names_lower())
    
    user_prompt = f"""STORY:
    {story}
    
    USER REQUEST:
    {request}
    
    REQUIREMENTS:
    - Output MUST be valid JSON, with keys:
      name, faction, culture, profession, background, personality_traits, age, gender, hooks
    - personality_traits: an array of 3-6 concise adjectives
    - hooks: 2-4 one-sentence quest or relationship hooks
    - All fields MUST be consistent with the STORY.
    - Name must look native to the STORY's cultures/factions.
    - Keep total under 120 words (excluding JSON syntax).
    - Do NOT include markdown or explanation, JSON only.
    - Avoid any of these existing names (case-insensitive): {existing[:50]}
    """
    
    raw = llm.chat(system=SYSTEM_GEN, user=user_prompt)
    
    try:
        raw = raw.strip()
        if raw.startswith("```"):
            raw = re.sub(r"^```[a-zA-Z]*\n|```$", "", raw,
                         flags=re.MULTILINE).strip()
        data = json.loads(raw)
    except Exception:
        data = {"error": "Model did not retrun valid JSON", "raw": raw}
    
    if "name" in data and ensure_unique:
        names = _exisitng_names_lower()
        original = data["name"]
        if original and original.lower() in names:
            data["name"] = original + f" of {uuid.uuid4().hex[:4]}"
    data ["_id"] = uuid.uuid4().hex
    
    if save and "error" not in data:
        _save_to_roster(data)
    
    return data

def list_roster() -> List[Dict[str, Any]]:
    return _load_roster()