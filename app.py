import argparse, json
from npc_generation.story import StoryIndex
from npc_generation.qa import answer_question
from npc_generation.generator import generate_charactre, list_roster

BANNER = "AI NPC Generation System (Python) ver. 1.0 - Type 'help' for commands."

def repl(index: StoryIndex):
    print(BANNER)
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break
        if not line:
            continue
        if line in ("quit", "exit"):
            print("Bye!")
            break
        if line == "help":
            print("Commands:")
            print("  ask <question>.        - ask about the story")
            print("  gen <request>          - generae=te a character JSON")
            print("  roster                 - list saved characters")
            print("  help                   - show this help")
            print("  quit                   - exit")
            continue
        if line.startswith("ask "):
            q = line[4:].strip()
            ans = answer_question(index, q)
            print(ans)
            continue
        if line.startswith("gen "):
            r = line[4:].strip()
            data = generate_charactre(index, r)
            print(json.dumps(data, ensure_ascii=False, indent=2))
            continue
        if line == "roaster":
            print(json.dumps(list_roster(), ensure_ascii=False, indent=2))
            continue
        print("Unknown command. Type 'help'.")

def main():
    ap = argparse.ArgumentParser(description="NPC Generation System")
    ap.add_argument("--story", required=True, help="Path to story file (e.g., fantasy.md)")
    args = ap.parse_args()
    index = StoryIndex(args.story)
    repl(index)
    
if __name__ == "__main__":
    main()