# How the exercise sets are written (for whoever adds or edits exercises)

## The learner
- 20, 3rd-year BCA (Data Science major) student in Pune, India. Goal: a data science / ML master's in the Netherlands (2028), then a junior data scientist job, e.g. **fraud detection at Dutch banks** or junior data engineer.
- **Coding is weak** by their own account. They have never built a project. They know basic Python syntax and have done ~20 of the "100 pandas puzzles" (with small mistakes, e.g. using `.count()` where `.sum()` was needed). Little university maths, but did full maths in 12th and likes it.
- Former **swimming coach** (2 years). Sociable, very hard-working. Learns best from numpy-100-style graded exercises.
- Will train **1 hour a day**: ~10 min reading the guide, ~45 min exercises, ~5 min review.
- Wants **plain, simple language**: explain every technical term the first time it is used, step-by-step, no jargon or fluff.

## Files per lesson
| File | What |
|---|---|
| `tools/source/<lesson>.ktx` | The exercises: question, hint, answer (source of truth) |
| `<folder>/guide.md` | The learning document, read before the exercises |
| `<folder>/cheatsheet.md` | One-page summary for review days |
| `<folder>/exercises.ipynb`, `exercises-with-hints.md`, `exercises-with-answers.md` | **Generated** by `tools/build.py`. Never hand-edit |

Lessons: `python` -> `1-python-warmup` (30 exercises), `numpy` -> `2-numpy`, `pandas` -> `3-pandas`, `sklearn` -> `4-scikit-learn` (100 each).

## .ktx format
```
< q1
Question text in markdown. May contain a ```python code block``` with starting code.
< h1
Short hint, e.g. `np.zeros`, or one sentence.
< a1
import numpy as np
z = np.zeros(10)
print(z)
```
- Numbers 1..N, no gaps. Don't put stars or levels in the text: the build adds them from the number.
- Levels: 100-sets are easy 1–40, medium 41–75, hard 76–100. Python warm-up: easy 1–12, medium 13–24, hard 25–30.

## Rules for questions and answers
1. **Original exercises.** You may be inspired by numpy-100 / 100-pandas-puzzles, but don't copy them.
2. **Every answer is self-contained**: it includes its own imports, builds or loads its own data, and runs alone in a fresh Python session. The learner calls `answer(n)` on any exercise.
3. **Deterministic**: use `np.random.default_rng(42)` (or `random_state=42`), never unseeded randomness.
4. **Print the result** so the learner sees output. Add short `#` comments in answers that explain the *why*, in plain words.
5. If the question needs starting data, show the exact starting code in the question in a code block, and repeat it in the answer.
6. Data files are in `data/` at the project root. Notebooks run from inside the lesson folder, so load with `pd.read_csv("../data/transactions.csv")`. No internet. Built-in sklearn datasets that ship offline are fine (`load_iris`, `load_wine`, `load_breast_cancer`, `load_diabetes`, `load_digits`, `make_classification`, `make_blobs`...). **Never** `fetch_*` (needs internet).
7. If an answer must write a file, write it to `outputs/` inside the lesson folder (create it with `os.makedirs("outputs", exist_ok=True)`).
8. Each answer must run in **under 10 seconds**. Silence warnings only if they would confuse the learner.
9. **Daily load:** each day-chunk (below) must fit about **45 minutes for this learner**. Easy ≈ 2–3 min, medium ≈ 4–5 min, hard ≈ 6–8 min each. "Hard" means hard for a beginner, not a research puzzle: a few lines, one or two new ideas combined.
10. Build skill **gradually**: each exercise uses only things from the guide so far and earlier exercises, plus at most one new idea (which the hint names).
11. **Tailor contexts** where natural: card transactions and fraud (the career target), swim meets (their coaching background), student marks. Use generic arrays where that's clearer. Aim for skills a junior data scientist actually uses at work and in interviews.
12. Versions in `.venv`: Python 3.13, numpy 2.3, pandas 2.3, scikit-learn 1.9, matplotlib 3.11. Use modern, non-deprecated APIs.
13. Hard levels should include a few "spot the bug" or "why is this result misleading?" exercises (answer explains in comments and shows the fix), because judging code matters more than typing it in the AI era.

## Day-chunks (the guide's parts must line up with these)
- Python warm-up: 1–15, 16–30
- NumPy, pandas, scikit-learn: 1–13, 14–27, 28–40, 41–52, 53–64, 65–75, 76–83, 84–91, 92–100

## guide.md structure
- Title, then "How to use this guide" (3–4 lines), then one **Part per day-chunk**, headed like
  `## Part 3: Boolean masks and filtering (exercises 28–40)`.
- Each part: what it is (plain words, define every term), why it matters at work (one line, real example), small runnable examples with the output shown as comments, "Common mistakes" (2–4 bullets), and "Now do exercises X–Y".
- Teach everything the exercises in that part need. Short paragraphs, tables, bullets. Friendly, direct, not childish.

## cheatsheet.md
One page: the most-used functions as a table (function | what it does | tiny example), grouped by topic.

## Data files (in `data/`)
- `swimmers.csv` (60 rows): swimmer_id, name, gender, birth_year, city (3 missing), club, coach, joined_date
- `swim_results.csv` (~940 rows): result_id, meet, date, pool_length_m (25/50), swimmer_id, event (e.g. "50 Free"; some messy "50 free"), stroke (some messy " freestyle "), distance_m, time_sec (NaN when DQ), status ("OK"/"DQ"); includes 6 exact duplicate rows
- `customers.csv` (800 rows): customer_id, age (some -1 = data-entry errors), city (Dutch cities), account_open_date, credit_limit_eur, segment (student/standard/premium)
- `transactions.csv` (6,000 rows, ~1.9% fraud): transaction_id, customer_id, timestamp ("YYYY-MM-DD HH:MM:SS", Jan–Mar 2025), merchant_category (30 missing), channel (in_store/online/contactless), country, amount_eur, is_fraud (0/1). Fraud is more likely for foreign countries (NG, RU, US), online, gift_cards/electronics, night hours (0–5) and big amounts.
- `student_marks.csv` (300 rows): student_id, study_hours_per_week, attendance_pct, sleep_hours (10 missing), previous_cgpa, part_time_job (0/1), favourite_subject, final_marks (0–100), passed (0/1)

## Build and check
```bash
cd ~/Data-Science-Practice
.venv/bin/python tools/build.py <lesson>          # makes notebook + md files
.venv/bin/python tools/build.py --check <lesson>  # runs every answer; must say N/N OK
```
If you change the .ktx after the notebook exists and nobody has started it, delete `<folder>/exercises.ipynb` and build again.
