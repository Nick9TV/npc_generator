# NPC Generation System (Python) ver 1.0

This is a **Python** implementation of an interactive NPC generator that:
- **Understands a story** (`fantasy.md`) and answers questions about factions, cultures, and history
- **Generates unique, lore-appropriate characters** on demand
- **Returns structured JSON** with character details (faction, profession, traits, hooks, etc.)

## Features
- Simple story ingestion and chunking
- Q&A grounded in your story
- Character generator with **name uniqueness** check and JSON output
- Persistent **roster** saved to `data/roster.jsonl`
- Works with any story file you provide (swap in a new `fantasy.md`)

## Tech
- Python 3.10+
- OpenAI API (set `OPENAI_API_KEY`)
- Models: chat (`gpt-4o-mini`)

## Setup

1. **Unzip** this archive or clone the repo.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your API key in .env file:
   ```bash
   export OPENAI_API_KEY=sk-...   # Windows PowerShell: setx OPENAI_API_KEY "sk-..."
   ```

## Usage

Prepare your story file, e.g. `data/fantasy.md` (a small sample is included).

Run the interactive CLI:
```bash
python app.py --story data/fantasy.md
```
### Commands (REPL)

- `help`  
  Show available commands.

- `ask <question>`  
  Ask lore questions about the loaded story.  
  _Example:_ `ask What are the main factions?`

- `gen <request>`  
  Generate a lore-appropriate NPC as JSON (auto-saved to the roster).  
  _Example:_ `gen A stealthy courier from the cloud-silk traders, witty but guarded.`

- `roster`  
  Print all saved NPCs from `data/roster.jsonl`.

- `quit` / `exit`  
  Leave the interactive session.
  

Example generator output:
```json
{
  "name": "Aldric Stormwind",
  "faction": "Ironbound Guild",
  "culture": "Northreach",
  "profession": "Blacksmith",
  "background": "Forged in the mountain city of Bramblegate...",
  "personality_traits": ["stoic","loyal","perceptive"],
  "age": 38,
  "gender": "male",
  "hooks": ["Seeks rare ore", "Owes a favor to the captain"]
}
```
## Project Structure
```
npc_generator/
  npc_generation/
    __init__.py
    config.py
    llm.py
    story.py
    qa.py
    generator.py
  data/
    fantasy.md (sample)
    (auto-created at runtime) roster.jsonl, index.json
  .env
  app.py
  README.md
  requirements.txt
```

## Extending
- Swap providers: set `LLM_PROVIDER` and implement other providers in `llm.py`.
- Add web UI (FastAPI + simple chat page).
- Add embeddings for retrieval; cache chunk vectors to `data/`.

## Testing
- Add unit tests under `tests/`.
- Mock LLM responses for offline tests.