import json
import os
from datetime import datetime

NOTES_PATH = os.path.join("data", "notes.json")

def load_notes():
    if not os.path.exists(NOTES_PATH):
        print("❌ notes.json not found.")
        return {}
    with open(NOTES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def print_entry(problem, entry):
    print(f"\n🔢 Problem #{entry.get('problem_number', '?')}: {problem} ({entry['date']})")
    print(f"📌 Platform   : {entry['platform']}")
    print(f"📍 Status     : {entry['status']}")
    print(f"⚠️  Mistake    : {entry['mistake_highlight'][0]}")
    print(f"🛠 Fix        : {entry['fix_summary']}")
    print(f"💡 Flash Tip  : {entry['flash_tip']}")
    print("-" * 60)

def show_all(notes):
    count = 0
    for problem, entries in notes.items():
        for entry in entries:
            print_entry(problem, entry)
            count += 1
    if count == 0:
        print("📭 No logs found.")

def filter_by_keyword(notes):
    keyword = input("🔑 Enter keyword to search: ").strip().lower()
    found = False
    for problem, entries in notes.items():
        for entry in entries:
            combined = (
                problem + " " +
                entry.get("code", "") + " " +
                " ".join(entry.get("mistake_highlight", [])) + " " +
                entry.get("fix_summary", "") + " " +
                entry.get("flash_tip", "")
            ).lower()
            if keyword in combined:
                print_entry(problem, entry)
                found = True
    if not found:
        print(f"❌ No entries found for keyword: '{keyword}'")

def filter_by_date(notes):
    date_str = input("📅 Enter date (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        found = False
        for problem, entries in notes.items():
            for entry in entries:
                if entry.get("date") == date_str:
                    print_entry(problem, entry)
                    found = True
        if not found:
            print(f"❌ No logs found on {date_str}")
    except ValueError:
        print("❌ Invalid date format. Use YYYY-MM-DD.")

def filter_by_problem_number(notes):
    number = input("🔢 Enter Problem Number (e.g., 1): ").strip()
    found = False
    for problem, entries in notes.items():
        for entry in entries:
            if entry.get("problem_number") == number:
                print_entry(problem, entry)
                found = True
    if not found:
        print(f"❌ No logs found for problem number {number}")

def show_latest_only(notes):
    for problem, entries in notes.items():
        latest_entry = sorted(entries, key=lambda e: e['date'], reverse=True)[0]
        print_entry(problem, latest_entry)

def menu():
    notes = load_notes()
    if not notes:
        return

    while True:
        print("\n📘 DSA Diagnosis Tracker - What would you like to do?")
        print("1️⃣  Show All Logs")
        print("2️⃣  Filter by Keyword")
        print("3️⃣  Filter by Date")
        print("4️⃣  Show Latest Entry per Problem")
        print("5️⃣  🔢 Filter by Problem Number")
        print("0️⃣  Exit")

        choice = input("🧭 Choose an option (0-5): ").strip()

        if choice == "1":
            show_all(notes)
        elif choice == "2":
            filter_by_keyword(notes)
        elif choice == "3":
            filter_by_date(notes)
        elif choice == "4":
            show_latest_only(notes)
        elif choice == "5":
            filter_by_problem_number(notes)
        elif choice == "0":
            print("👋 Goodbye, keep solving like a pro dev!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 0 to 5.")

if __name__ == "__main__":
    menu()
