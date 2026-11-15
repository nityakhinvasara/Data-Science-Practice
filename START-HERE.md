# Data Science Practice: start here

This folder is your daily training for data science. It works like the famous
[numpy-100](https://github.com/rougier/numpy-100) exercise list, but it's built for you, covers
**Python, NumPy, pandas and scikit-learn**, and uses data you care about: card fraud, swim meets
and student marks.

- **330 exercises** that go from easy (★☆☆) to medium (★★☆) to hard (★★★)
- A **guide** for each topic that teaches you what you need before you try the exercises
- A **day-by-day plan**: 1 hour a day, about 6 weeks
- A **mini project** at the end (a fraud detection model) that you can put on GitHub

---

## What to open, in order

| Step | Open this | When |
|---|---|---|
| 1 | `0-setup/SETUP.md` | Once, before Day 1 (about 10 minutes) |
| 2 | Double-click `start-jupyter.command` | Every day, to open Jupyter in this folder |
| 3 | `DAILY-PLAN.md` | Every day: it tells you exactly what to do |
| 4 | The folder the plan names (e.g. `2-numpy/`) | Every day |
| 5 | `my-mistakes.md` | Every day, last 5 minutes |

## Folder map

```
Data-Science-Practice/
├── START-HERE.md          ← you are here
├── start-jupyter.command  ← double-click to open Jupyter here
├── DAILY-PLAN.md          ← what to do each day (tick the boxes)
├── my-mistakes.md         ← write down what tripped you up
├── RESOURCES.md           ← more exercise sets like this one, for later
│
├── 0-setup/               ← one-time setup
├── 1-python-warmup/       ← 30 exercises (Days 1–2)
├── 2-numpy/               ← 100 exercises
├── 3-pandas/              ← 100 exercises
├── 4-scikit-learn/        ← 100 exercises
├── 5-mini-project/        ← fraud detection project (end of the plan)
│
├── data/                  ← the CSV files the exercises use (don't edit)
├── tools/                 ← code that makes hint()/answer() work (don't need to open)
└── .venv/                 ← your Python + libraries (don't touch)
```

## Inside every topic folder

| File | What it is | When to use it |
|---|---|---|
| `guide.md` | The lesson. Split into parts that match the plan's days | Read today's part **before** the exercises (~10 min) |
| `exercises.ipynb` | The exercises. **You write your code here** | The main 45 minutes |
| `cheatsheet.md` | One-page summary | Review days |
| `exercises-with-hints.md` | All questions with hints, no answers | Reading on your phone |
| `exercises-with-answers.md` | All questions with answers | Only after you've tried |

Tip: Jupyter shows `.md` files as plain text. To read them nicely formatted, open them on your GitHub page
(https://github.com/nityakhinvasara/Data-Science-Practice), which also works on your phone.

## How one day works (1 hour)

1. **Open `DAILY-PLAN.md`** and find the first day that isn't ticked.
2. **Read** the guide part it names (~10 min). Type the small examples yourself if you have time.
3. **Do the exercises** in `exercises.ipynb` (~45 min).
4. **Write 1–3 lines in `my-mistakes.md`** about anything you got wrong or had to look up (~5 min).
5. **Tick the box** in `DAILY-PLAN.md`. Done.

## The rules (these are what make it work)

1. **Try first.** Give every exercise a real attempt before asking for help.
2. **Stuck for 5 minutes?** Type `hint(n)` in a cell (n = the exercise number).
3. **Stuck for 10 more minutes?** Type `answer(n)`. Read it, understand it, then **close it and type it
   yourself from memory**. Never copy-paste.
4. **No AI code-writing while practising.** Turn off any AI autocomplete. You can ask ChatGPT
   or Claude to *explain* a concept or an error message, but not to solve the exercise. (We
   talked about why: you need to be able to judge code, and that only comes from writing it.)
5. **Don't skip days to "catch up".** Missed a day? Just do the next unticked day. Busy day?
   Do a **15-minute minimum**: 3 exercises. That keeps the habit alive.
6. **Run cells top to bottom.** If something weird happens, click **Kernel → Restart**,
   then run the first cell again.
