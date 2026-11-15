"""Builds the exercise files from tools/source/*.ktx, and checks that every answer runs.

    python tools/build.py                 # build files for all lessons (never overwrites your notebook)
    python tools/build.py --check         # run every answer and report any that fail
    python tools/build.py --check numpy   # check one lesson
    python tools/build.py --fresh numpy   # make a blank copy: exercises-fresh.ipynb (to redo everything)
"""
import contextlib
import io
import json
import os
import signal
import sys
import time
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from practice import LESSONS, LEVEL_NAMES, ROOT, STARS, level, load  # noqa: E402


def heading(n, q, stars):
    """Exercise heading: stars go on the first line, so a code block at the end of the question stays intact."""
    first, _, rest = q.partition("\n")
    return f"#### {n}. {first} ({stars})" + (f"\n{rest}" if rest else "")


def md_cell(text):
    return {"cell_type": "markdown", "metadata": {}, "source": text.splitlines(keepends=True)}


def code_cell(text=""):
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
            "source": text.splitlines(keepends=True)}


def notebook(lesson, qa):
    folder, title, _ = LESSONS[lesson]
    cells = [
        md_cell(f"# {title}\n\n"
                "**How to use this notebook**\n\n"
                "1. Run the first code cell below (click it, press **Shift+Enter**). It loads `hint()` and `answer()`.\n"
                "2. Each exercise has an empty code cell under it. Write your code there and press **Shift+Enter**.\n"
                "3. Stuck? Type `hint(7)` in a cell to see the hint for exercise 7.\n"
                "4. Still stuck after 10 minutes? Type `answer(7)`. Then **close it and type the answer yourself**, "
                "do not copy-paste.\n"
                "5. Today's exercise numbers are in `DAILY-PLAN.md`.\n\n"
                "Stars: ★☆☆ easy · ★★☆ medium · ★★★ hard"),
        code_cell(f"%run ../tools/initialise.py {lesson}"),
    ]
    current = None
    for n, it in qa.items():
        lv = level(lesson, n)
        if lv != current:
            cells.append(md_cell(f"## {LEVEL_NAMES[lv]}"))
            current = lv
        cells.append(md_cell(heading(n, it["q"], STARS[lv])))
        cells.append(code_cell())
    return {"cells": cells, "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python"}}, "nbformat": 4, "nbformat_minor": 5}


def markdown(lesson, qa, with_answers):
    folder, title, _ = LESSONS[lesson]
    kind = "hints and answers" if with_answers else "hints"
    out = [f"# {title} ({kind})\n",
           "_Generated from `tools/source/" + lesson + ".ktx`. Don't edit this file; it gets rebuilt._\n"]
    current = None
    for n, it in qa.items():
        lv = level(lesson, n)
        if lv != current:
            out.append(f"\n## {LEVEL_NAMES[lv]}\n")
            current = lv
        out.append(heading(n, it["q"], STARS[lv]) + "\n")
        out.append(f"`hint:` {it['h']}\n")
        if with_answers:
            out.append(f"```python\n{it['a']}\n```\n")
    return "\n".join(out)


def build(lesson, fresh=False):
    qa = load(lesson)
    folder = ROOT / LESSONS[lesson][0]
    folder.mkdir(exist_ok=True)
    (folder / "exercises-with-hints.md").write_text(markdown(lesson, qa, False), encoding="utf-8")
    (folder / "exercises-with-answers.md").write_text(markdown(lesson, qa, True), encoding="utf-8")
    nb_path = folder / ("exercises-fresh.ipynb" if fresh else "exercises.ipynb")
    if nb_path.exists() and not fresh:
        print(f"{lesson}: kept your existing {nb_path.name} (your work is safe)")
    else:
        nb_path.write_text(json.dumps(notebook(lesson, qa), indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"{lesson}: wrote {nb_path.relative_to(ROOT)}")
    print(f"{lesson}: {len(qa)} exercises, md files rebuilt")


class Timeout(Exception):
    pass


def check(lesson, limit=60):
    """Run every answer in its own fresh namespace, from inside the lesson folder."""
    import matplotlib
    matplotlib.use("Agg")
    qa = load(lesson)
    folder = ROOT / LESSONS[lesson][0]
    old = os.getcwd()
    os.chdir(folder)
    failures, slow = [], []

    def on_alarm(*_):
        raise Timeout()
    signal.signal(signal.SIGALRM, on_alarm)
    for n, it in qa.items():
        start = time.time()
        signal.alarm(limit)
        try:
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                exec(compile(it["a"], f"{lesson}#{n}", "exec"), {"__name__": "__main__"})
        except Timeout:
            failures.append((n, f"took longer than {limit}s"))
        except Exception:
            failures.append((n, traceback.format_exc().strip().splitlines()[-1]))
        finally:
            signal.alarm(0)
            try:
                import matplotlib.pyplot as plt
                plt.close("all")
            except Exception:
                pass
        if time.time() - start > 10:
            slow.append((n, round(time.time() - start, 1)))
    os.chdir(old)
    print(f"{lesson}: {len(qa) - len(failures)}/{len(qa)} answers ran OK")
    for n, msg in failures:
        print(f"  FAIL #{n}: {msg}")
    for n, s in slow:
        print(f"  slow #{n}: {s}s")
    return not failures


if __name__ == "__main__":
    args = sys.argv[1:]
    available = [k for k in LESSONS if (ROOT / "tools" / "source" / f"{k}.ktx").exists()]
    if args and args[0] == "--check":
        targets = args[1:] or available
        ok = all([check(t) for t in targets])
        sys.exit(0 if ok else 1)
    elif args and args[0] == "--fresh":
        for t in args[1:] or available:
            build(t, fresh=True)
    else:
        for t in args or available:
            build(t)
