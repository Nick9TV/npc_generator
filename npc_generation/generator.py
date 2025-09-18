import json, os, re, uuid
from typing import Dict, List, Any

SYSTEM_GEN = (
    "You are an NPC character generator. Create unique, lore-consistent names and details "
    "based ONLY on the STORY context. Always return strict JSON that validates."
)