"""Create an Epilogue Life plan folder from the repo templates.

Usage:  python setup-plan-folder.py [target-dir] [--template-dir DIR]
Default target: ~/epilogue-life
"""
import argparse, json, pathlib, shutil, sys

AREAS = [
    ("01-end-of-life-planning.md", "End-of-Life Planning"),
    ("02-legal-and-financial.md", "Legal & Financial"),
    ("03-healthcare-decisions.md", "Healthcare Decisions"),
    ("04-relationships-and-legacy.md", "Relationships & Legacy"),
    ("05-personal-fulfilment.md", "Personal Fulfilment"),
    ("06-final-arrangements.md", "Final Arrangements"),
    ("07-digital-and-personal-assets.md", "Digital & Personal Assets"),
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target", nargs="?", default=str(pathlib.Path.home() / "epilogue-life"))
    ap.add_argument("--template-dir", default=str(pathlib.Path(__file__).resolve().parent.parent / "shared"))
    args = ap.parse_args()

    target = pathlib.Path(args.target).expanduser()
    tmpl = pathlib.Path(args.template_dir).expanduser()
    (target / "answers").mkdir(parents=True, exist_ok=True)
    (target / "answers" / "archive").mkdir(exist_ok=True)
    (target / "plan" / "letters").mkdir(parents=True, exist_ok=True)

    def seed(src_name, dest_name):
        src, dest = tmpl / src_name, target / dest_name
        if src.exists() and not dest.exists():
            shutil.copyfile(src, dest)
            print("  wrote", dest)
        elif dest.exists():
            print("  kept existing", dest)

    seed("profile-template.md", "profile.md")
    seed("loved-ones-template.md", "loved-ones.md")
    if (tmpl / "question-bank.md").exists():
        shutil.copyfile(tmpl / "question-bank.md", target / "question-bank.md")
        print("  wrote", target / "question-bank.md")
    if (tmpl / "question-bank.json").exists():
        shutil.copyfile(tmpl / "question-bank.json", target / "question-bank.json")

    for fname, area in AREAS:
        f = target / "answers" / fname
        if not f.exists():
            f.write_text("# Answers: %s\n\n*One entry per question: the question, your words, the date.\nSkipped questions stay listed as skipped; they are never answered by anyone else.*\n" % area, encoding="utf-8")
            print("  wrote", f)

    prog = target / "answers" / "progress.json"
    if not prog.exists():
        prog.write_text(json.dumps({"answered": [], "skipped": [], "deferred": [], "prefs": {"per_day": 2}}, indent=2), encoding="utf-8")
        print("  wrote", prog)

    print("\nPlan folder ready at:", target)
    print("Next: open your chat and say \"Let's begin my Epilogue Life plan.\"")

if __name__ == "__main__":
    sys.exit(main())
