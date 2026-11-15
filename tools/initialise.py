"""Loaded by the first cell of every exercises notebook:

    %run ../tools/initialise.py numpy

After that you can type, in any cell:
    hint(5)      -> shows the hint for exercise 5
    answer(5)    -> shows one possible answer for exercise 5
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from practice import LESSONS, load  # noqa: E402

_lesson = sys.argv[1] if len(sys.argv) > 1 else "numpy"
_QA = load(_lesson)


def hint(n):
    """Show the hint for exercise n."""
    if n not in _QA:
        print(f"There is no exercise {n}. Pick 1 to {len(_QA)}.")
        return
    print(f"Exercise {n}: {_QA[n]['q']}\n\nHINT: {_QA[n]['h']}")


def answer(n):
    """Show one possible answer for exercise n. Try for 10+ minutes before using this!"""
    if n not in _QA:
        print(f"There is no exercise {n}. Pick 1 to {len(_QA)}.")
        return
    print(f"Exercise {n}: {_QA[n]['q']}\n\n# ---- one possible answer ----\n{_QA[n]['a']}")


print(f"Ready: {LESSONS[_lesson][1]}. Use hint(n) or answer(n) when you are stuck.")
