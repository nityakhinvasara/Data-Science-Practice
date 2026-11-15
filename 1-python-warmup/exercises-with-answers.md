# Python warm-up: 30 exercises (hints and answers)

_Generated from `tools/source/python.ktx`. Don't edit this file; it gets rebuilt._


## Level 1: Easy

#### 1. Make three variables for one swimmer: `name` = `"Diya"`, `age` = `13`, `time_sec` = `31.47`. Print each value next to its type. (★☆☆)

`hint:` `type(x)` tells you what kind of value `x` is.

```python
name = "Diya"       # text -> str
age = 13            # whole number -> int
time_sec = 31.47    # number with a decimal point -> float
print(name, type(name))
print(age, type(age))
print(time_sec, type(time_sec))
```

#### 2. Using the variables below, print exactly: `Diya swam 50 Free in 31.5 s` (time rounded to 1 decimal) using one f-string. (★☆☆)
```python
name = "Diya"
event = "50 Free"
time_sec = 31.47
```

`hint:` `f"{time_sec:.1f}"` shows the number with 1 decimal place.

```python
name = "Diya"
event = "50 Free"
time_sec = 31.47
# the f before the quotes lets us put variables inside {}; :.1f means "1 decimal"
print(f"{name} swam {event} in {time_sec:.1f} s")
```

#### 3. A time came from a form as text: `raw = "75.3"`. Convert it to a float, then split it into whole minutes and leftover seconds, and print `1:15.30`. (★☆☆)

`hint:` `float(raw)`, then `//` (whole-number division) and `%` (remainder).

```python
raw = "75.3"
seconds = float(raw)          # "75.3" is text; float() turns it into a number
minutes = int(seconds // 60)  # how many full minutes fit: 1
rest = seconds % 60           # what is left over: 15.3
print(f"{minutes}:{rest:.2f}")
```

#### 4. Print the first time, the last time and how many times are in the list. (★☆☆)
```python
times = [31.47, 29.80, 33.12, 30.05, 28.90]
```

`hint:` Indexes start at 0. `times[-1]` is the last item. `len(times)` counts items.

```python
times = [31.47, 29.80, 33.12, 30.05, 28.90]
print(times[0])     # first item is at index 0
print(times[-1])    # negative index counts from the end
print(len(times))   # number of items
```

#### 5. From the same list, print the first three times, and then the last two times, using slicing. (★☆☆)
```python
times = [31.47, 29.80, 33.12, 30.05, 28.90]
```

`hint:` `lst[start:stop]` stops just *before* `stop`. `lst[-2:]` means "from the second-last to the end".

```python
times = [31.47, 29.80, 33.12, 30.05, 28.90]
print(times[:3])    # indexes 0, 1, 2 (stop at 3, not included)
print(times[-2:])   # last two
```

#### 6. Start with the marks list below. Add a new mark `88` to the end, then print the list, the total and the average (rounded to 2 decimals). (★☆☆)
```python
marks = [72, 65, 90, 58]
```

`hint:` `marks.append(88)`, `sum(marks)`, `len(marks)`, `round(x, 2)`.

```python
marks = [72, 65, 90, 58]
marks.append(88)                  # adds to the end, changes the list in place
total = sum(marks)
average = total / len(marks)      # there is no mean() for lists; divide sum by count
print(marks)
print(total)
print(round(average, 2))
```

#### 7. Loop over the transaction amounts and print each one as `Amount: 12.50 EUR` (always 2 decimals). (★☆☆)
```python
amounts = [12.5, 250.0, 8.99, 1200.0]
```

`hint:` `for a in amounts:` then an f-string with `:.2f`.

```python
amounts = [12.5, 250.0, 8.99, 1200.0]
for a in amounts:                  # a takes each value in turn
    print(f"Amount: {a:.2f} EUR")
```

#### 8. A 400 m race in a 50 m pool has 8 lengths. Use `range` to print `Length 1` up to `Length 8`. (★☆☆)

`hint:` `range(1, 9)` gives 1, 2, ..., 8 (the stop number is not included).

```python
for i in range(1, 9):     # stop is 9 because range stops before it
    print(f"Length {i}")
```

#### 9. Write `if/elif/else` code that turns a mark into a grade: 75 or more is `"Distinction"`, 50–74 is `"Pass"`, below 50 is `"Fail"`. Test it on `mark = 68`. (★☆☆)

`hint:` Check the highest band first: `if mark >= 75:` then `elif mark >= 50:`.

```python
mark = 68
# Python checks top to bottom and stops at the first True condition,
# so the order matters: the highest band goes first
if mark >= 75:
    grade = "Distinction"
elif mark >= 50:
    grade = "Pass"
else:
    grade = "Fail"
print(mark, grade)
```

#### 10. Make a dictionary of best times: Diya 31.47, Kabir 28.90, Ananya 30.05. Print Kabir's time, add Rohan with 29.60, then print Meera's time using `.get` so it prints `None` instead of crashing. Then print it again with a default of `"no time"`. (★☆☆)

`hint:` `best["Kabir"]`, `best["Rohan"] = 29.60`, `best.get("Meera")`, `best.get("Meera", "no time")`.

```python
best = {"Diya": 31.47, "Kabir": 28.90, "Ananya": 30.05}
print(best["Kabir"])                 # look up a value by its key
best["Rohan"] = 29.60                # a new key adds a new entry
print(best.get("Meera"))             # best["Meera"] would raise KeyError; get gives None
print(best.get("Meera", "no time"))  # or a default you choose
print(best)
```

#### 11. Loop over the dictionary with `.items()` and print one line per merchant: `groceries: 45.2 EUR`. (★☆☆)
```python
spend = {"groceries": 45.2, "electronics": 899.0, "travel": 310.5}
```

`hint:` `for key, value in spend.items():`

```python
spend = {"groceries": 45.2, "electronics": 899.0, "travel": 310.5}
for category, amount in spend.items():   # items() gives (key, value) pairs
    print(f"{category}: {amount} EUR")
```

#### 12. A result is stored as a tuple: `result = ("Kabir", "50 Free", 28.90)`. Unpack it into three variables in one line and print a sentence. Then swap `a = 1` and `b = 2` in one line and print them. (★☆☆)

`hint:` `name, event, t = result` and `a, b = b, a`.

```python
result = ("Kabir", "50 Free", 28.90)   # a tuple: like a list but cannot be changed
name, event, t = result                # unpacking: one variable per item
print(f"{name} swam {event} in {t} s")

a = 1
b = 2
a, b = b, a        # right side is built first, then unpacked: a clean swap
print(a, b)
```


## Level 2: Medium

#### 13. Count how many transactions came from each channel, using a dictionary. Print the dictionary. (★★☆)
```python
channels = ["online", "in_store", "online", "contactless", "online", "in_store"]
```

`hint:` Start with `counts = {}`, then for each item: `counts[c] = counts.get(c, 0) + 1`.

```python
channels = ["online", "in_store", "online", "contactless", "online", "in_store"]
counts = {}
for c in channels:
    # get(c, 0) gives the count so far, or 0 the first time we see c
    counts[c] = counts.get(c, 0) + 1
print(counts)
```

#### 14. Write a function `to_inr(eur, rate=100)` that returns the amount in Indian rupees (use 100 as a round example rate). Print `to_inr(25)` and `to_inr(25, rate=104.5)`. (★★☆)

`hint:` `def to_inr(eur, rate=100):` and `return eur * rate`. A default argument is used when you don't pass that value.

```python
def to_inr(eur, rate=100):
    # rate=100 is a default: used only when the caller doesn't give a rate
    return eur * rate

print(to_inr(25))               # uses rate 100
print(to_inr(25, rate=104.5))   # overrides the default
```

#### 15. Loop over the amounts and build a new list `big` with only the amounts above 500. Also count how many there are. Print both. (★★☆)
```python
amounts = [12.5, 950.0, 8.99, 1200.0, 499.99, 640.0]
```

`hint:` Start with `big = []`, use `if a > 500:` inside the loop, then `big.append(a)`.

```python
amounts = [12.5, 950.0, 8.99, 1200.0, 499.99, 640.0]
big = []
for a in amounts:
    if a > 500:
        big.append(a)
print(big)
print(len(big))   # no need for a separate counter: the list length is the count
```

#### 16. Use a list comprehension to make a list of the times rounded to 1 decimal. (★★☆)
```python
times = [31.47, 29.83, 33.12, 30.05, 28.96]
```

`hint:` `[round(t, 1) for t in times]`

```python
times = [31.47, 29.83, 33.12, 30.05, 28.96]
rounded = [round(t, 1) for t in times]   # "for each t in times, keep round(t, 1)"
print(rounded)
```

#### 17. Redo exercise 15 in one line: a list comprehension with a condition that keeps amounts above 500. (★★☆)
```python
amounts = [12.5, 950.0, 8.99, 1200.0, 499.99, 640.0]
```

`hint:` `[a for a in amounts if a > 500]`

```python
amounts = [12.5, 950.0, 8.99, 1200.0, 499.99, 640.0]
big = [a for a in amounts if a > 500]   # the if at the end filters
print(big, len(big))
```

#### 18. Use `enumerate` to print each swimmer with a lane number starting from 1: `Lane 1: Diya`. (★★☆)
```python
swimmers = ["Diya", "Kabir", "Ananya", "Rohan"]
```

`hint:` `for lane, name in enumerate(swimmers, start=1):`

```python
swimmers = ["Diya", "Kabir", "Ananya", "Rohan"]
for lane, name in enumerate(swimmers, start=1):   # enumerate gives (position, item)
    print(f"Lane {lane}: {name}")
```

#### 19. Use `zip` to print each swimmer with their time, then build a dictionary `{name: time}` from the two lists. (★★☆)
```python
names = ["Diya", "Kabir", "Ananya"]
times = [31.47, 28.90, 30.05]
```

`hint:` `for n, t in zip(names, times):` and `dict(zip(names, times))`.

```python
names = ["Diya", "Kabir", "Ananya"]
times = [31.47, 28.90, 30.05]
for n, t in zip(names, times):     # zip walks both lists side by side
    print(n, t)
best = dict(zip(names, times))     # pairs become key: value
print(best)
```

#### 20. Sort the results from fastest to slowest using `sorted` with `key=` and a `lambda`. Then print the slowest-first order too. (★★☆)
```python
results = [("Diya", 31.47), ("Kabir", 28.90), ("Ananya", 30.05), ("Rohan", 29.60)]
```

`hint:` `sorted(results, key=lambda r: r[1])`. Add `reverse=True` for the other order.

```python
results = [("Diya", 31.47), ("Kabir", 28.90), ("Ananya", 30.05), ("Rohan", 29.60)]
# key= tells sorted WHAT to compare; lambda r: r[1] means "the time part of each tuple"
fastest_first = sorted(results, key=lambda r: r[1])
print(fastest_first)
print(sorted(results, key=lambda r: r[1], reverse=True))
print(results)   # sorted() returns a NEW list; the original is unchanged
```

#### 21. Write a function `find_time(results, name)` that returns that swimmer's time, or `None` if the name is not in the list. Test it with `"Rohan"` and `"Meera"` and print a friendly message when the result `is None`. (★★☆)
```python
results = [("Diya", 31.47), ("Kabir", 28.90), ("Rohan", 29.60)]
```

`hint:` Loop, `return t` when the name matches, and `return None` after the loop. Check with `if t is None:`.

```python
def find_time(results, name):
    for n, t in results:
        if n == name:
            return t        # return stops the function right away
    return None             # only reached if no name matched

results = [("Diya", 31.47), ("Kabir", 28.90), ("Rohan", 29.60)]
for who in ["Rohan", "Meera"]:
    t = find_time(results, who)
    if t is None:           # use "is None", not "== None"
        print(f"{who}: no time recorded")
    else:
        print(f"{who}: {t} s")
```

#### 22. Times arrive as text and disqualified swims are written as `"DQ"`. Convert each to a float with `try/except ValueError`, skip the bad ones, and print the valid times and how many were skipped. (★★☆)
```python
raw = ["31.47", "DQ", "29.80", "", "30.05"]
```

`hint:` `try: t = float(r)` and `except ValueError: skipped += 1`.

```python
raw = ["31.47", "DQ", "29.80", "", "30.05"]
valid = []
skipped = 0
for r in raw:
    try:
        valid.append(float(r))   # float("DQ") and float("") raise ValueError
    except ValueError:
        skipped += 1             # instead of crashing, we count it and move on
print(valid)
print("skipped:", skipped)
```

#### 23. Import the `statistics` module and print the mean, median and standard deviation (2 decimals) of the marks. Also import `math` and print `math.sqrt(2)` rounded to 3 decimals. (★★☆)
```python
marks = [72, 65, 90, 58, 88, 74, 61]
```

`hint:` `import statistics` then `statistics.mean(marks)`, `statistics.median(marks)`, `statistics.stdev(marks)`.

```python
import math
import statistics

marks = [72, 65, 90, 58, 88, 74, 61]
# module.function: the name before the dot says where the function lives
print(round(statistics.mean(marks), 2))
print(statistics.median(marks))
print(round(statistics.stdev(marks), 2))   # sample standard deviation: how spread out
print(round(math.sqrt(2), 3))
```

#### 24. Open `../data/swimmers.csv` with the `csv` module (`csv.DictReader`). Print how many swimmers there are, and the first row. (★★☆)

`hint:` `with open("../data/swimmers.csv", newline="") as f:` then `rows = list(csv.DictReader(f))`.

```python
import csv

# "with" closes the file for us when the block ends
with open("../data/swimmers.csv", newline="") as f:
    rows = list(csv.DictReader(f))   # each row becomes a dict: {column name: value}
print(len(rows))
print(rows[0])
print(type(rows[0]["birth_year"]))   # note: every value comes in as text (str)
```


## Level 3: Hard

#### 25. From `../data/swimmers.csv`, count the swimmers per city with a dictionary. Some cities are empty: count those as `"Unknown"`. Print the counts from most to fewest. (★★★)

`hint:` `city = row["city"] or "Unknown"` (empty text counts as False). Then sort `counts.items()` with `key=lambda kv: kv[1], reverse=True`.

```python
import csv

with open("../data/swimmers.csv", newline="") as f:
    rows = list(csv.DictReader(f))

counts = {}
for row in rows:
    city = row["city"] or "Unknown"   # "" is falsy, so "or" swaps in "Unknown"
    counts[city] = counts.get(city, 0) + 1

for city, n in sorted(counts.items(), key=lambda kv: kv[1], reverse=True):
    print(f"{city}: {n}")
```

#### 26. Write `summarize(amounts)` that returns a tuple `(count, total, average)`, or `None` if the list is empty. Unpack the result for the list below, and show what happens for `[]`. (★★★)
```python
amounts = [12.5, 950.0, 8.99, 1200.0]
```

`hint:` `if not amounts: return None`, then `return len(amounts), total, total / len(amounts)`.

```python
def summarize(amounts):
    if not amounts:              # an empty list counts as False
        return None              # avoid dividing by zero
    total = sum(amounts)
    return len(amounts), total, total / len(amounts)   # commas make a tuple

amounts = [12.5, 950.0, 8.99, 1200.0]
count, total, avg = summarize(amounts)
print(f"{count} transactions, total {total:.2f} EUR, average {avg:.2f} EUR")

result = summarize([])
if result is None:
    print("no transactions")
```

#### 27. **Spot the bug.** This code should remove every disqualified time (`0`) from the list, but one `0` survives. Explain why, then fix it. (★★★)
```python
times = [31.47, 0, 0, 29.80, 0, 30.05]
for t in times:
    if t == 0:
        times.remove(t)
print(times)   # [31.47, 29.8, 0, 30.05]  <- a 0 is left!
```

`hint:` Removing items from a list *while looping over it* makes the loop skip the next item. Build a new list instead.

```python
times = [31.47, 0, 0, 29.80, 0, 30.05]
# Why the bug happens: the loop walks by position (0, 1, 2, ...).
# When we remove the item at position 1, everything shifts left, so the
# second 0 moves into position 1, and the loop jumps on to position 2: it never checks it.
# Fix: never change a list while looping over it. Build a new one.
clean = [t for t in times if t != 0]
print(clean)
```

#### 28. **Spot the bug.** Each call should start a fresh list of flagged transactions, but the second call still remembers the first one. Explain why and fix it. (★★★)
```python
def flag(tx_id, flagged=[]):
    flagged.append(tx_id)
    return flagged

print(flag("T1"))   # ['T1']
print(flag("T2"))   # ['T1', 'T2']  <- expected ['T2']
```

`hint:` A default value is created **once**, when `def` runs, not on every call. Use `flagged=None` and make the list inside.

```python
# Why: the [] in the def line is built one time. Every call that doesn't pass
# its own list shares that same list, so it keeps growing.
def flag(tx_id, flagged=None):
    if flagged is None:
        flagged = []        # a brand-new list on every call
    flagged.append(tx_id)
    return flagged

print(flag("T1"))   # ['T1']
print(flag("T2"))   # ['T2']
```

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

```python
channels = ["online", "in_store", "online", "contactless", "in_store", "online"]
# Why: "or" joins two separate conditions. The right side is just the text
# "contactless", which is non-empty and so always counts as True.
count = 0
for c in channels:
    if c in ("online", "contactless"):   # or: c == "online" or c == "contactless"
        count += 1
print(count)   # 4
# Bonus: "=" stores a value, "==" compares. "if c = 'online':" is a SyntaxError,
# so Python refuses to run it at all. Always use == inside if.
```

#### 30. Mini task: from `../data/swimmers.csv`, work out each swimmer's age in 2025 (`2025 - birth_year`; remember it is text). Then print, for each club, the number of swimmers and the average age (1 decimal), sorted by average age, youngest club first. (★★★)

`hint:` Keep a dict of lists: `ages.setdefault(club, []).append(age)` (or check `if club not in ages`). Then build `(club, count, avg)` tuples and sort by `avg`.

```python
import csv

with open("../data/swimmers.csv", newline="") as f:
    rows = list(csv.DictReader(f))

ages = {}   # club -> list of ages
for row in rows:
    age = 2025 - int(row["birth_year"])        # int() because CSV values are text
    if row["club"] not in ages:
        ages[row["club"]] = []
    ages[row["club"]].append(age)

summary = [(club, len(a), sum(a) / len(a)) for club, a in ages.items()]
for club, n, avg in sorted(summary, key=lambda s: s[2]):
    print(f"{club}: {n} swimmers, average age {avg:.1f}")
```
