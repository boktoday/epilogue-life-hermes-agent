"""Pick the next N questions from the bank for the daily schedule.

Usage: python next_questions.py <plan-folder> [--count 2]
Reads question-bank.json + answers/progress.json, prints the chosen questions
with their category and help text, ready for the agent to ask warmly.
"""
import argparse, json, pathlib, sys

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--count", type=int, default=2)
    args = ap.parse_args()

    folder = pathlib.Path(args.folder).expanduser()
    bank_f = folder / "question-bank.json"
    prog_f = folder / "answers" / "progress.json"
    if not bank_f.exists():
        print("NO_BANK: question-bank.json missing in", folder)
        return 0
    bank = json.loads(bank_f.read_text(encoding="utf-8"))
    prog = json.loads(prog_f.read_text(encoding="utf-8")) if prog_f.exists() else {}
    answered = set(prog.get("answered", [])); skipped = set(prog.get("skipped", [])); deferred = set(prog.get("deferred", []))
    count = prog.get("prefs", {}).get("per_day", args.count)
    pool = [q for q in bank["questions"] if q["id"] not in answered and q["id"] not in skipped]
    pool.sort(key=lambda q: (0 if q["id"] in deferred else 1))
    chosen = pool[:count]
    if not chosen:
        print("ALL_DONE: every question is answered or skipped. Just the monthly review remains.")
        return 0
    for q in chosen:
        print("QID:", q["id"])
        print("AREA:", q["category"])
        print("QUESTION:", q["title"])
        if q.get("description"):
            print("CONTEXT:", q["description"])
        if q.get("help"):
            print("HELP:", q["help"])
        print("---")
    return 0

if __name__ == "__main__":
    sys.exit(main())
