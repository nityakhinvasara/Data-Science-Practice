"""Shared code for the exercise files. You never need to open this.

Exercise source files live in tools/source/<lesson>.ktx and look like this:

    < q1
    The question text (markdown).
    < h1
    The hint.
    < a1
    import numpy as np
    print(np.__version__)

q = question, h = hint, a = answer (Python code). Numbers must run 1, 2, 3 ... with no gaps.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "tools" / "source"

# lesson key -> (folder, title, (easy_last, medium_last))
LESSONS = {
    "python": ("1-python-warmup", "Python warm-up: 30 exercises", (12, 24)),
    "numpy": ("2-numpy", "NumPy: 100 exercises", (40, 75)),
    "pandas": ("3-pandas", "pandas: 100 exercises", (40, 75)),
    "sklearn": ("4-scikit-learn", "scikit-learn: 100 exercises", (40, 75)),
}

LEVEL_NAMES = {1: "Level 1: Easy", 2: "Level 2: Medium", 3: "Level 3: Hard"}
STARS = {1: "★☆☆", 2: "★★☆", 3: "★★★"}


def level(lesson, n):
    easy, medium = LESSONS[lesson][2]
    return 1 if n <= easy else 2 if n <= medium else 3


def load(lesson):
    """Return {n: {'q': str, 'h': str, 'a': str}}."""
    text = (SOURCE / f"{lesson}.ktx").read_text(encoding="utf-8")
    items, key, buf = {}, None, []

    def flush():
        if key:
            kind, n = key
            items.setdefault(n, {})[kind] = "\n".join(buf).strip("\n")

    for line in text.splitlines():
        m = re.match(r"^< ([qha])(\d+)\s*$", line)
        if m:
            flush()
            key, buf = (m.group(1), int(m.group(2))), []
        else:
            buf.append(line)
    flush()
    nums = sorted(items)
    if nums != list(range(1, len(nums) + 1)):
        raise ValueError(f"{lesson}: exercise numbers are not 1..N without gaps")
    for n, it in items.items():
        missing = {"q", "h", "a"} - set(it)
        if missing:
            raise ValueError(f"{lesson} #{n}: missing {missing}")
    return items
