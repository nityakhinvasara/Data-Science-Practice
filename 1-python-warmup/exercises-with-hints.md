# Python warm-up: 30 exercises (hints)

_Generated from `tools/source/python.ktx`. Don't edit this file; it gets rebuilt._


## Level 1: Easy

#### 1. Make three variables for one swimmer: `name` = `"Diya"`, `age` = `13`, `time_sec` = `31.47`. Print each value next to its type. (★☆☆)

`hint:` `type(x)` tells you what kind of value `x` is.

#### 2. Using the variables below, print exactly: `Diya swam 50 Free in 31.5 s` (time rounded to 1 decimal) using one f-string. (★☆☆)
```python
name = "Diya"
event = "50 Free"
time_sec = 31.47
```

`hint:` `f"{time_sec:.1f}"` shows the number with 1 decimal place.

#### 3. A time came from a form as text: `raw = "75.3"`. Convert it to a float, then split it into whole minutes and leftover seconds, and print `1:15.30`. (★☆☆)

`hint:` `float(raw)`, then `//` (whole-number division) and `%` (remainder).

#### 4. Print the first time, the last time and how many times are in the list. (★☆☆)
```python
times = [31.47, 29.80, 33.12, 30.05, 28.90]
```

`hint:` Indexes start at 0. `times[-1]` is the last item. `len(times)` counts items.

#### 5. From the same list, print the first three times, and then the last two times, using slicing. (★☆☆)
```python
times = [31.47, 29.80, 33.12, 30.05, 28.90]
```

`hint:` `lst[start:stop]` stops just *before* `stop`. `lst[-2:]` means "from the second-last to the end".

#### 6. Start with the marks list below. Add a new mark `88` to the end, then print the list, the total and the average (rounded to 2 decimals). (★☆☆)
```python
marks = [72, 65, 90, 58]
```

`hint:` `marks.append(88)`, `sum(marks)`, `len(marks)`, `round(x, 2)`.

#### 7. Loop over the transaction amounts and print each one as `Amount: 12.50 EUR` (always 2 decimals). (★☆☆)
```python
amounts = [12.5, 250.0, 8.99, 1200.0]
```

`hint:` `for a in amounts:` then an f-string with `:.2f`.

#### 8. A 400 m race in a 50 m pool has 8 lengths. Use `range` to print `Length 1` up to `Length 8`. (★☆☆)

`hint:` `range(1, 9)` gives 1, 2, ..., 8 (the stop number is not included).

#### 9. Write `if/elif/else` code that turns a mark into a grade: 75 or more is `"Distinction"`, 50–74 is `"Pass"`, below 50 is `"Fail"`. Test it on `mark = 68`. (★☆☆)

`hint:` Check the highest band first: `if mark >= 75:` then `elif mark >= 50:`.

#### 10. Make a dictionary of best times: Diya 31.47, Kabir 28.90, Ananya 30.05. Print Kabir's time, add Rohan with 29.60, then print Meera's time using `.get` so it prints `None` instead of crashing. Then print it again with a default of `"no time"`. (★☆☆)

`hint:` `best["Kabir"]`, `best["Rohan"] = 29.60`, `best.get("Meera")`, `best.get("Meera", "no time")`.

#### 11. Loop over the dictionary with `.items()` and print one line per merchant: `groceries: 45.2 EUR`. (★☆☆)
```python
spend = {"groceries": 45.2, "electronics": 899.0, "travel": 310.5}
```

`hint:` `for key, value in spend.items():`

#### 12. A result is stored as a tuple: `result = ("Kabir", "50 Free", 28.90)`. Unpack it into three variables in one line and print a sentence. Then swap `a = 1` and `b = 2` in one line and print them. (★☆☆)

`hint:` `name, event, t = result` and `a, b = b, a`.


## Level 2: Medium

#### 13. Count how many transactions came from each channel, using a dictionary. Print the dictionary. (★★☆)
```python
channels = ["online", "in_store", "online", "contactless", "online", "in_store"]
```

`hint:` Start with `counts = {}`, then for each item: `counts[c] = counts.get(c, 0) + 1`.

#### 14. Write a function `to_inr(eur, rate=100)` that returns the amount in Indian rupees (use 100 as a round example rate). Print `to_inr(25)` and `to_inr(25, rate=104.5)`. (★★☆)

`hint:` `def to_inr(eur, rate=100):` and `return eur * rate`. A default argument is used when you don't pass that value.

#### 15. Loop over the amounts and build a new list `big` with only the amounts above 500. Also count how many there are. Print both. (★★☆)
```python
amounts = [12.5, 950.0, 8.99, 1200.0, 499.99, 640.0]
```

`hint:` Start with `big = []`, use `if a > 500:` inside the loop, then `big.append(a)`.

#### 16. Use a list comprehension to make a list of the times rounded to 1 decimal. (★★☆)
```python
times = [31.47, 29.83, 33.12, 30.05, 28.96]
```

`hint:` `[round(t, 1) for t in times]`

#### 17. Redo exercise 15 in one line: a list comprehension with a condition that keeps amounts above 500. (★★☆)
```python
amounts = [12.5, 950.0, 8.99, 1200.0, 499.99, 640.0]
```

`hint:` `[a for a in amounts if a > 500]`

#### 18. Use `enumerate` to print each swimmer with a lane number starting from 1: `Lane 1: Diya`. (★★☆)
```python
swimmers = ["Diya", "Kabir", "Ananya", "Rohan"]
```

`hint:` `for lane, name in enumerate(swimmers, start=1):`

#### 19. Use `zip` to print each swimmer with their time, then build a dictionary `{name: time}` from the two lists. (★★☆)
```python
names = ["Diya", "Kabir", "Ananya"]
times = [31.47, 28.90, 30.05]
```

`hint:` `for n, t in zip(names, times):` and `dict(zip(names, times))`.

#### 20. Sort the results from fastest to slowest using `sorted` with `key=` and a `lambda`. Then print the slowest-first order too. (★★☆)
```python
results = [("Diya", 31.47), ("Kabir", 28.90), ("Ananya", 30.05), ("Rohan", 29.60)]
```

`hint:` `sorted(results, key=lambda r: r[1])`. Add `reverse=True` for the other order.

#### 21. Write a function `find_time(results, name)` that returns that swimmer's time, or `None` if the name is not in the list. Test it with `"Rohan"` and `"Meera"` and print a friendly message when the result `is None`. (★★☆)
```python
results = [("Diya", 31.47), ("Kabir", 28.90), ("Rohan", 29.60)]
```

`hint:` Loop, `return t` when the name matches, and `return None` after the loop. Check with `if t is None:`.

#### 22. Times arrive as text and disqualified swims are written as `"DQ"`. Convert each to a float with `try/except ValueError`, skip the bad ones, and print the valid times and how many were skipped. (★★☆)
```python
raw = ["31.47", "DQ", "29.80", "", "30.05"]
```

`hint:` `try: t = float(r)` and `except ValueError: skipped += 1`.

#### 23. Import the `statistics` module and print the mean, median and standard deviation (2 decimals) of the marks. Also import `math` and print `math.sqrt(2)` rounded to 3 decimals. (★★☆)
```python
marks = [72, 65, 90, 58, 88, 74, 61]
```

`hint:` `import statistics` then `statistics.mean(marks)`, `statistics.median(marks)`, `statistics.stdev(marks)`.

#### 24. Open `../data/swimmers.csv` with the `csv` module (`csv.DictReader`). Print how many swimmers there are, and the first row. (★★☆)

`hint:` `with open("../data/swimmers.csv", newline="") as f:` then `rows = list(csv.DictReader(f))`.


## Level 3: Hard

#### 25. From `../data/swimmers.csv`, count the swimmers per city with a dictionary. Some cities are empty: count those as `"Unknown"`. Print the counts from most to fewest. (★★★)

`hint:` `city = row["city"] or "Unknown"` (empty text counts as False). Then sort `counts.items()` with `key=lambda kv: kv[1], reverse=True`.

#### 26. Write `summarize(amounts)` that returns a tuple `(count, total, average)`, or `None` if the list is empty. Unpack the result for the list below, and show what happens for `[]`. (★★★)
```python
amounts = [12.5, 950.0, 8.99, 1200.0]
```

`hint:` `if not amounts: return None`, then `return len(amounts), total, total / len(amounts)`.

#### 27. **Spot the bug.** This code should remove every disqualified time (`0`) from the list, but one `0` survives. Explain why, then fix it. (★★★)
```python
times = [31.47, 0, 0, 29.80, 0, 30.05]
for t in times:
    if t == 0:
        times.remove(t)
print(times)   # [31.47, 29.8, 0, 30.05]  <- a 0 is left!
```

`hint:` Removing items from a list *while looping over it* makes the loop skip the next item. Build a new list instead.

#### 28. **Spot the bug.** Each call should start a fresh list of flagged transactions, but the second call still remembers the first one. Explain why and fix it. (★★★)
```python
def flag(tx_id, flagged=[]):
    flagged.append(tx_id)
    return flagged

print(flag("T1"))   # ['T1']
print(flag("T2"))   # ['T1', 'T2']  <- expected ['T2']
```

`hint:` A default value is created **once**, when `def` runs, not on every call. Use `flagged=None` and make the list inside.

#### 29. **Spot the bug.** This should count only online and contactless payments (answer: 4), but it counts all 6. Explain why and fix it. (Bonus: what goes wrong if someone writes `if c = "online":`?) (★★★)
```python
channels = ["online", "in_store", "online", "contactless", "in_store", "online"]
count = 0
for c in channels:
    if c == "online" or "contactless":
        count += 1
print(count)   # 6
```

`hint:` Python reads it as `(c == "online") or ("contactless")`, and non-empty text is always True. Use `c in ("online", "contactless")`.

#### 30. Mini task: from `../data/swimmers.csv`, work out each swimmer's age in 2025 (`2025 - birth_year`; remember it is text). Then print, for each club, the number of swimmers and the average age (1 decimal), sorted by average age, youngest club first. (★★★)

`hint:` Keep a dict of lists: `ages.setdefault(club, []).append(age)` (or check `if club not in ages`). Then build `(club, count, avg)` tuples and sort by `avg`.
