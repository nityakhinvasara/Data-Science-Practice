"""Checks that Python, the libraries, the data and the exercises are all in place."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ok = True


def line(good, text):
    global ok
    ok = ok and good
    print(("  OK   " if good else "  FIX  ") + text)


print("Python:", sys.version.split()[0], "at", sys.executable)
line(".venv" in sys.executable, "using this folder's .venv Python")

for lib in ["numpy", "pandas", "sklearn", "matplotlib", "ipykernel"]:
    try:
        mod = __import__(lib)
        line(True, f"{lib} {getattr(mod, '__version__', '')}")
    except ImportError:
        line(False, f"{lib} is missing: see 'If something goes wrong' in SETUP.md")

for f in ["swimmers.csv", "swim_results.csv", "customers.csv", "transactions.csv", "student_marks.csv"]:
    line((ROOT / "data" / f).exists(), f"data/{f}")

for folder in ["1-python-warmup", "2-numpy", "3-pandas", "4-scikit-learn"]:
    for f in ["guide.md", "exercises.ipynb"]:
        line((ROOT / folder / f).exists(), f"{folder}/{f}")

print("\nALL GOOD: open DAILY-PLAN.md" if ok else "\nSomething needs fixing (lines marked FIX).")
