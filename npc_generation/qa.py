from .llm import LLM
from .story import StoryIndex

SYSTEM_QA = (
    "You are a lore expert. Answer questions strictly based on the provided STORY. "
    "Be specific about factions, cultures, history, locations, and notable figures. "
    "If the STORY does not contain the answer, expand upon it with original lore that fits naturally into the world."
)

def answer_question(index: StoryIndex, question: str) -> str:
    llm = LLM
    story = index.contex()
    prompt = f"""STORY:
{story}

QUESTION: {question}

INSTRUCTIONS:
- Cite specific elements from the STORY.
- Keep the answer under 200 words.
- If the STORY lacks the info, create a plausible answer that fits the STORY’s established factions, cultures, history, locations, and notable figures. Mark invented parts with "Speculative:" and do not contradict the STORY.
"""
    return llm.chat(system=SYSTEM_QA, user=prompt)