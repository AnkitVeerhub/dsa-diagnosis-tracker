# 🧠 DSA Diagnosis Tracker

Track your DSA problem-solving journey, log mistakes, fixes, and pro tips — and turn them into a powerful revision and interview prep tool.

---

## 📌 Project Purpose

This is a **CLI-based DSA mistake tracker** where you:
- Log every problem you practice or revise
- Highlight what went wrong (bugs, confusion, edge cases)
- Record how you fixed it
- Export everything to Markdown for clean reviews or GitHub display

> Designed to build **debugging discipline**, **self-awareness**, and become an **SDE-ready problem solver**.

---

## ⚙️ Features

✅ Add logs with:
- Problem number and name  
- Platform (LeetCode, GFG, etc.)  
- Code snippet or summary  
- Mistake highlight  
- Fix summary  
- Flash tip (1-liner)  

✅ Search & Filter logs:
- By keyword  
- By date  
- By problem number  

✅ Export:
- One-click export to clean Markdown for GitHub or personal review

---

## 📁 Project Structure

dsa-diagnosis-tracker/
│
├── data/
│ └── notes.json ← All log data stored here
│
├── scripts/
│ ├── add_note.py ← Add a new problem log
│ ├── menu.py ← Interactive viewer / filter
│ ├── search_notes.py ← (Optional) Quick keyword search
│ └── export_md.py ← Exports logs to Markdown
│
├── DSA_Tracker_Export.md ← Markdown export of all logs
├── README.md ← You're reading this
└── .gitignore ← (Optional) Ignore temp/IDE files

🧪 Example Markdown Export
## 1. Longest Consecutive Sequence
- 🔢 Problem #: 1
- 📅 Date      : 2025-07-18
- 🌐 Platform  : LeetCode
- 📍 Status    : ⚠️ Stuck - Brute Force Confusion
- ⚠️ Mistake    : Confused between two for loops vs for + while
- 🛠 Fix        : Used correct outer loop + inner while structure
- 💡 Flash Tip  : Brute = outer + inner while
---

💡 Why Use This?
✅ Helps with:

Interview prep & debugging memory

Identifying repeated weak spots

Turning daily practice into a long-term asset


✨ Future Ideas
Add topic & difficulty tags

Topic-wise markdown exports

Web dashboard using Streamlit or React

Sync with LeetCode API or GitHub Gists

🧑‍💻 Author
Ankit Kumar
🔗 GitHub
🔗 LinkedIn