import json
import os

NOTES_PATH = os.path.join("data", "notes.json")

def search_notes(keyword: str):
    if not os.path.exists(NOTES_PATH):
        print("❌ notes.json not found.")
        return

    with open(NOTES_PATH, "r", encoding="utf-8") as f:
        notes = json.load(f)

    found = False
    for problem, entries in notes.items():
        for entry in entries:
            combined_text = (
                problem + " " +
                entry.get("code", "") + " " +
                " ".join(entry.get("mistake_highlight", [])) + " " +
                entry.get("fix_summary", "") + " " +
                entry.get("flash_tip", "")
            ).lower()

            if keyword.lower() in combined_text:
                found = True
                print(f"\n🔎 Match in: {problem} ({entry['date']})")
                print(f"📌 Platform: {entry['platform']}")
                print(f"📍 Status: {entry['status']}")
                print(f"⚠️ Mistake: {entry['mistake_highlight'][0]}")
                print(f"🛠 Fix: {entry['fix_summary']}")
                print(f"💡 Flash Tip: {entry['flash_tip']}")
                print("-" * 60)

    if not found:
        print(f"\n❌ No entries found for keyword: '{keyword}'")

if __name__ == "__main__":
    keyword = input("🔍 Enter keyword to search (e.g. brute, hashset, consecutive): ")
    search_notes(keyword)
