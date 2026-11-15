# Daily plan: 1 hour a day, about 6 weeks

**Start after your exams.** Before that, only do the setup (Day 0). Your grades come first.

Each day = ~10 min reading the guide + ~45 min exercises + ~5 min writing in `my-mistakes.md`.
Find the first unticked day and do it. Tick it with an `x`: `- [x]`.

> **Why this order?** NumPy first (pandas is built on top of it), then pandas (you clean and shape data
> with it), then scikit-learn (you build models on the clean data). The **hard** levels come back
> 2–3 weeks later on purpose: coming back to a topic after a gap makes it stick far better than
> doing it all in one go.
>
> **Why 6 weeks, not 4?** 330 exercises in 30 days means 11+ a day, including the hard ones. That's
> too fast to actually learn them. 6 weeks with review days is fast but still realistic. If you're
> flying, do two days' work in one sitting. If a day takes longer, finish it the next day. Review
> days absorb the overflow.

---

## Day 0: setup (any free evening, ~20 min)
- [ ] Follow `0-setup/SETUP.md` until the check says **ALL GOOD**

## Week 1: Python warm-up + NumPy basics
- [ ] **Day 1**: `1-python-warmup/guide.md` Part 1 → exercises **1–15**
- [ ] **Day 2**: `1-python-warmup/guide.md` Part 2 → exercises **16–30** (a longer day, ~75 min: if time runs out, finish 25–30 at the start of Day 3)
- [ ] **Day 3**: `2-numpy/guide.md` Part 1 → NumPy **1–13**
- [ ] **Day 4**: `2-numpy/guide.md` Part 2 → NumPy **14–27**
- [ ] **Day 5**: `2-numpy/guide.md` Part 3 → NumPy **28–40**
- [ ] **Day 6**: `2-numpy/guide.md` Part 4 → NumPy **41–52** (medium starts)
- [ ] **Day 7: Review.** See "How to do a review day" below. Topics: Python, NumPy 1–52

## Week 2: NumPy medium + pandas basics
- [ ] **Day 8**: `2-numpy/guide.md` Part 5 → NumPy **53–64**
- [ ] **Day 9**: `2-numpy/guide.md` Part 6 → NumPy **65–75**
- [ ] **Day 10**: `3-pandas/guide.md` Part 1 → pandas **1–13**
- [ ] **Day 11**: `3-pandas/guide.md` Part 2 → pandas **14–27**
- [ ] **Day 12**: `3-pandas/guide.md` Part 3 → pandas **28–40**
- [ ] **Day 13**: `3-pandas/guide.md` Part 4 → pandas **41–52**
- [ ] **Day 14: Review.** Topics: NumPy 53–75, pandas 1–52

## Week 3: pandas medium + scikit-learn basics
- [ ] **Day 15**: `3-pandas/guide.md` Part 5 → pandas **53–64**
- [ ] **Day 16**: `3-pandas/guide.md` Part 6 → pandas **65–75**
- [ ] **Day 17**: `4-scikit-learn/guide.md` Part 1 → sklearn **1–13** (your first ML models!)
- [ ] **Day 18**: `4-scikit-learn/guide.md` Part 2 → sklearn **14–27**
- [ ] **Day 19**: `4-scikit-learn/guide.md` Part 3 → sklearn **28–40**
- [ ] **Day 20**: `4-scikit-learn/guide.md` Part 4 → sklearn **41–52**
- [ ] **Day 21: Review.** Topics: pandas 53–75, sklearn 1–52

## Week 4: scikit-learn medium + hard levels begin
- [ ] **Day 22**: `4-scikit-learn/guide.md` Part 5 → sklearn **53–64**
- [ ] **Day 23**: `4-scikit-learn/guide.md` Part 6 → sklearn **65–75**
- [ ] **Day 24**: `2-numpy/guide.md` Part 7 → NumPy **76–83** (hard ★★★)
- [ ] **Day 25**: `2-numpy/guide.md` Part 8 → NumPy **84–91**
- [ ] **Day 26**: `2-numpy/guide.md` Part 9 → NumPy **92–100** 🎉 NumPy done
- [ ] **Day 27**: `3-pandas/guide.md` Part 7 → pandas **76–83**
- [ ] **Day 28: Review.** Topics: sklearn 53–75, NumPy hard, pandas 76–83

## Week 5: hard levels + project start
- [ ] **Day 29**: `3-pandas/guide.md` Part 8 → pandas **84–91**
- [ ] **Day 30**: `3-pandas/guide.md` Part 9 → pandas **92–100** 🎉 pandas done
- [ ] **Day 31**: `4-scikit-learn/guide.md` Part 7 → sklearn **76–83**
- [ ] **Day 32**: `4-scikit-learn/guide.md` Part 8 → sklearn **84–91**
- [ ] **Day 33**: `4-scikit-learn/guide.md` Part 9 → sklearn **92–100** 🎉 all 330 done
- [ ] **Day 34**: `5-mini-project/PROJECT.md` → **Step 1** (explore the data)
- [ ] **Day 35: Review.** Topics: pandas hard, sklearn hard

## Week 6: mini project + final test
- [ ] **Day 36**: Project **Step 2** (clean + build features)
- [ ] **Day 37**: Project **Step 3** (first models)
- [ ] **Day 38**: Project **Step 4** (improve + choose a threshold)
- [ ] **Day 39**: Project **Step 5** (write the README, put it on GitHub)
- [ ] **Day 40: Final test.** Open `exercises-fresh.ipynb` (see below) and redo 10 random hard exercises
  from each library with **no hints**. Note your score here: NumPy __/10, pandas __/10, sklearn __/10
- [ ] **Days 41–42**: Rest, or redo anything from `my-mistakes.md`

---

## How to do a review day (1 hour)
1. **(25 min)** Open `my-mistakes.md`. Redo every exercise you listed this week, in a new cell,
   **without hints**. Got it right? Put ✅ next to it in the file.
2. **(15 min)** Read the `cheatsheet.md` of this week's topics. Anything unclear? Re-read that guide part.
3. **(15 min)** Pick 5 exercises from this week at random and redo them from scratch.
4. **(5 min)** Write one line at the bottom of `my-mistakes.md`: "This week I learned…"

Behind or overflowing? Use the review day to finish, and skip steps 3–4.

## Want to redo a whole set from scratch?
In VS Code's terminal (inside this folder), run, for example:
```bash
.venv/bin/python tools/build.py --fresh numpy
```
This makes a blank `2-numpy/exercises-fresh.ipynb`. Your original notebook is not touched.

---

## What comes after these 6 weeks
You'll be ready to start **real projects**. The next stage (we'll plan it when you get there):
1. **Charts**: matplotlib + seaborn (making clear graphs is half of explaining results)
2. **SQL** practice (your DBA minor helps): SQLBolt, then LeetCode SQL 50
3. **Statistics** (needed for Utrecht anyway): NPTEL Prob & Stats + StatQuest videos
4. **Projects 2–4** for your GitHub (see `RESOURCES.md`)
