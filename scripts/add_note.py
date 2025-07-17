import json
import os
from datetime import datetime

NOTES_PATH = os.path.join("data", "notes.json")

def load_notes():
    if not os.path.exists(NOTES_PATH):
        return {}
    with open(NOTES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_notes(notes):
    with open(NOTES_PATH, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=4)

def add_note():
    print("📝 Add a new DSA Debug Log")

    # ✅ Add this line for problem number
    problem_number = input("🔢 Enter Problem Number (e.g. 1): ").strip()
    problem_name = input("📌 Enter Problem Name: ").strip()
    platform = input("🌐 Platform (e.g. LeetCode, GFG): ").strip()
    status = input("📍 Status (e.g. Solved, Stuck - Logic, Brute only): ").strip()
    code = input("📄 Paste Code (or summary): ").strip()
    mistake = input("⚠️ What went wrong (confusion, bug, edge case)? ").strip()
    fix = input("🛠 How did you fix it? ").strip()
    tip = input("💡 Flash Tip (1 - liner)? ").strip()

    note_entry = {
        "problem_number": problem_number,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "platform": platform,
        "status": status,
        "code": code,
        "mistake_highlight": [mistake],
        "fix_summary": fix,
        "flash_tip": tip
    }

    notes = load_notes()

    if problem_name in notes:
        notes[problem_name].append(note_entry)
    else:
        notes[problem_name] = [note_entry]

    save_notes(notes)
    print(f"\n✅ Log saved for: {problem_name} on {note_entry['date']}")

if __name__ == "__main__":
    add_note()
