import json
import os

NOTES_PATH = os.path.join("data", "notes.json")
EXPORT_PATH = os.path.join("DSA_Tracker_Export.md")

def load_notes():
    if not os.path.exists(NOTES_PATH):
        print("❌ notes.json not found.")
        return {}
    with open(NOTES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def export_to_markdown(notes):
    with open(EXPORT_PATH, "w", encoding="utf-8") as f:
        f.write("# 📘 DSA Diagnosis Tracker - Export Log\n\n")

        problem_list = []
        for problem, entries in notes.items():
            for entry in entries:
                number = entry.get("problem_number", "?")
                f.write(f"## {number}. {problem}\n")
                f.write(f"- 🔢 Problem #: {number}\n")
                f.write(f"- 📅 Date: {entry.get('date')}\n")
                f.write(f"- 🌐 Platform: {entry.get('platform')}\n")
                f.write(f"- 📍 Status: {entry.get('status')}\n")
                f.write(f"- ⚠️ Mistake: {entry.get('mistake_highlight')[0]}\n")
                f.write(f"- 🛠 Fix: {entry.get('fix_summary')}\n")
                f.write(f"- 💡 Flash Tip: {entry.get('flash_tip')}\n")
                f.write("---\n\n")

    print(f"✅ Export complete! Markdown file created at:\n{EXPORT_PATH}")

if __name__ == "__main__":
    notes = load_notes()
    if notes:
        export_to_markdown(notes)
