# Python warm-up guide

## How to use this guide
- This is a 2-day refresher of the plain Python you need before NumPy, pandas and scikit-learn.
- Each day: read one Part (about 10 minutes), then do its 15 exercises in `exercises.ipynb` (about 45 minutes).
- Type every example yourself in a spare notebook cell. The output is shown after `#` so you can compare.
- Stuck for 10 minutes? Use `hint(n)`, then `answer(n)`. Close the answer and type it yourself.

---

## Part 1: Values, lists, loops, decisions and dictionaries (exercises 1–15)

### Variables and types
A **variable** is a name that points to a value. The **type** is the kind of value it is.

| Type | Meaning | Example |
|---|---|---|
| `int` | whole number | `age = 13` |
| `float` | number with a decimal point | `time_sec = 31.47` |
| `str` | text ("string"), always in quotes | `name = "Diya"` |
| `bool` | `True` or `False` | `passed = True` |

```python
time_sec = 31.47
print(type(time_sec))   # <class 'float'>
```

**Converting types.** Data from files and forms often arrives as text. You must convert it before doing maths.
```python
raw = "75.3"
seconds = float(raw)    # 75.3  (now a number)
print(int(seconds))     # 75    (int() cuts off the decimals)
print(str(13) + " yrs") # 13 yrs (str() turns a number into text)
```

**Arithmetic.** `+ - * /` as usual. Two extra ones are very handy:
- `//` whole-number division: `75 // 60` gives `1` (one full minute).
- `%` remainder ("modulo"): `75 % 60` gives `15` (15 seconds left over).

### f-strings: putting values into text
Put `f` before the quotes, then any variable inside `{ }`. Add `:.2f` to show 2 decimals.
```python
name = "Kabir"
t = 28.9
print(f"{name} swam in {t:.2f} s")   # Kabir swam in 28.90 s
print(f"{name} swam in {t:.1f} s")   # Kabir swam in 28.9 s
```

### Lists
A **list** holds many values in order, inside `[ ]`. Each item has a position called an **index**, starting at **0**.
```python
times = [31.47, 29.80, 33.12, 30.05, 28.90]
print(times[0])     # 31.47   first item
print(times[-1])    # 28.9    last item (negative = count from the end)
print(len(times))   # 5       how many items
```

**Slicing** takes a piece: `lst[start:stop]`. The `stop` position is **not** included.
```python
print(times[1:3])   # [29.8, 33.12]  positions 1 and 2
print(times[:2])    # [31.47, 29.8]  from the start
print(times[-2:])   # [30.05, 28.9]  the last two
```

**Changing a list:** `append` adds one item to the end. `sum` adds up numbers.
```python
marks = [72, 65]
marks.append(90)
print(marks, sum(marks), sum(marks) / len(marks))   # [72, 65, 90] 227 75.666...
print(round(75.666, 1))                             # 75.7
```

### Loops and range
A **for loop** repeats a block of code once for each item. The indented lines (4 spaces) are the block.
```python
for t in [31.47, 29.80]:
    print(f"Time: {t:.2f}")
# Time: 31.47
# Time: 29.80
```

`range` makes a sequence of numbers. Like slicing, the stop number is not included.
```python
for i in range(1, 4):
    print(i)        # 1, then 2, then 3
```
`range(5)` means 0, 1, 2, 3, 4.

### if / elif / else: making decisions
Python checks each condition from top to bottom and runs the **first** block whose condition is True.
```python
amount = 640
if amount > 1000:
    print("very large")
elif amount > 500:
    print("large")      # this one runs
else:
    print("normal")
```
Comparisons: `==` equal, `!=` not equal, `>`, `>=`, `<`, `<=`. Combine with `and`, `or`, `not`.

### Dictionaries
A **dictionary** (`dict`) stores **key: value** pairs inside `{ }`. You look things up by key, not by position. Think of it as a lookup table.
```python
best = {"Diya": 31.47, "Kabir": 28.90}
print(best["Kabir"])               # 28.9
best["Rohan"] = 29.60              # add a new pair (or change an existing one)
print(best.get("Meera"))           # None  (key missing, but no crash)
print(best.get("Meera", 0))        # 0     (your own default)
```
`best["Meera"]` would crash with a **KeyError** because the key does not exist. `.get` is the safe version.

Loop over keys and values together with `.items()`:
```python
for name, t in best.items():
    print(name, t)
# Diya 31.47
# Kabir 28.9
# Rohan 29.6
```

**Counting with a dict** is a pattern you will use constantly (pandas' `value_counts()` does the same thing later):
```python
cards = ["visa", "mastercard", "visa"]
counts = {}
for c in cards:
    counts[c] = counts.get(c, 0) + 1   # 0 the first time, then add 1
print(counts)   # {'visa': 2, 'mastercard': 1}
```

### Tuples and unpacking
A **tuple** is like a list but uses `( )` and cannot be changed after it is made. It is good for a fixed group of values, like one race result.
```python
result = ("Kabir", "50 Free", 28.90)
name, event, t = result      # "unpacking": one variable per item
print(name)                  # Kabir
a, b = 1, 2
a, b = b, a                  # swap in one line
print(a, b)                  # 2 1
```

### Functions
A **function** is a named, reusable piece of code. `def` creates it. **Arguments** are the inputs in brackets. `return` sends a result back.
```python
def pace_per_50(time_sec, distance_m):
    return time_sec / (distance_m / 50)

print(pace_per_50(62.0, 100))   # 31.0
```
A **default argument** has a value already, used when the caller leaves it out:
```python
def add_fee(amount, fee=2.5):
    return amount + fee

print(add_fee(100))          # 102.5
print(add_fee(100, fee=0))   # 100
```

### Building a filtered list with a loop
```python
marks = [72, 45, 90, 38]
failed = []
for m in marks:
    if m < 50:
        failed.append(m)
print(failed, len(failed))   # [45, 38] 2
```

**Why it matters at work:** a fraud analyst's first step is often exactly this: loop over transactions, count by category, and keep the suspicious ones.

### Common mistakes
- Forgetting that indexes start at 0, so `times[1]` is the **second** item.
- Forgetting that the stop in `range(1, 8)` and `lst[0:3]` is not included.
- Doing maths on text: `"75.3" * 2` gives `"75.375.3"`. Convert with `float()` first.
- Forgetting `return` in a function: then it gives back `None`.

**Now do exercises 1–15.**

---

## Part 2: Comprehensions, sorting, errors, modules and CSV files (exercises 16–30)

### List comprehensions
A **list comprehension** builds a new list in one line. It is a short way to write the "loop + append" pattern.
```python
times = [31.47, 29.83]
print([round(t, 1) for t in times])          # [31.5, 29.8]
```
Add `if` at the end to keep only some items:
```python
amounts = [12.5, 950.0, 640.0]
print([a for a in amounts if a > 500])       # [950.0, 640.0]
```
Read it as: "give me `a`, for each `a` in `amounts`, if `a > 500`".

### enumerate and zip
`enumerate` gives you the position **and** the item. `start=1` makes counting start at 1.
```python
for i, name in enumerate(["Diya", "Kabir"], start=1):
    print(i, name)
# 1 Diya
# 2 Kabir
```
`zip` walks through two lists side by side, pairing items.
```python
names = ["Diya", "Kabir"]
times = [31.47, 28.90]
for n, t in zip(names, times):
    print(n, t)                 # Diya 31.47, then Kabir 28.9
print(dict(zip(names, times)))  # {'Diya': 31.47, 'Kabir': 28.9}
```

### sorted, key= and lambda
`sorted(lst)` returns a **new** sorted list (the original stays as it was). `reverse=True` sorts high to low.

For lists of tuples you tell it **what to compare** with `key=`. A **lambda** is a tiny unnamed function written in one line: `lambda r: r[1]` means "given `r`, give back `r[1]`".
```python
results = [("Diya", 31.47), ("Kabir", 28.90)]
print(sorted(results, key=lambda r: r[1]))     # [('Kabir', 28.9), ('Diya', 31.47)]
print(sorted([3, 1, 2], reverse=True))         # [3, 2, 1]
```
You can sort a dict's pairs the same way: `sorted(counts.items(), key=lambda kv: kv[1])`.

### None
`None` means "no value here". Functions with no `return` give back `None`, and it is a good way to say "not found". Check it with `is None` (not `== None`).
```python
def find(names, target):
    for n in names:
        if n == target:
            return n
    return None

print(find(["Diya"], "Meera") is None)   # True
```

### Handling errors with try / except
When something goes wrong, Python raises an **exception** (an error) and stops. `try/except` lets you catch a specific error and carry on. `ValueError` is what `float()` or `int()` raise when the text is not a number.
```python
for r in ["31.47", "DQ"]:
    try:
        print(float(r))
    except ValueError:
        print("not a number:", r)
# 31.47
# not a number: DQ
```
Catch the specific error you expect (`ValueError`), not every error, so real bugs still show up.

### Importing modules
A **module** is a file of ready-made functions. `import` loads it, then you use `module.function`.
```python
import statistics
import math
print(statistics.mean([2, 4, 9]))     # 5
print(statistics.median([2, 4, 9]))   # 4
print(math.sqrt(16))                  # 4.0
from statistics import mean           # or import just one name
print(mean([1, 2]))                   # 1.5
```
`statistics.stdev` gives the **standard deviation**: a number for how spread out the values are around the mean (small = values close together).

### Reading a CSV file with the csv module
A **CSV** ("comma-separated values") file is a table saved as text: one row per line, columns split by commas, first line = column names.
```python
import csv
with open("../data/swimmers.csv", newline="") as f:
    rows = list(csv.DictReader(f))
print(len(rows))              # 60
print(rows[0]["name"])        # Aarav Patil
```
- `with open(...) as f:` opens the file and closes it automatically when the block ends.
- `csv.DictReader` turns each row into a dict: `{"name": "Aarav Patil", "club": "Deccan Dolphins", ...}`.
- `../data/` means "go up one folder, then into `data`", because the notebook runs from inside `1-python-warmup`.
- **Every value is text**, even numbers. Use `int(row["birth_year"])` before doing maths.
- An empty cell is the empty text `""`. Empty text counts as False, so `row["city"] or "Unknown"` gives `"Unknown"` when the city is blank.

Counting per club combines this with the dict pattern from Part 1:
```python
clubs = {}
for row in rows:
    clubs[row["club"]] = clubs.get(row["club"], 0) + 1
```
pandas does all of this in one line later (`pd.read_csv`, `value_counts`), but now you will know what it is doing for you.

### Spot the bug: three classic traps
1. **Changing a list while looping over it** makes the loop skip items. Build a new list with a comprehension instead.
2. **Mutable default argument**: `def f(x, items=[])` creates the list only once, so every call shares it. Use `items=None` and create the list inside.
3. **`or` with comparisons**: `if c == "a" or "b":` is always True, because `"b"` alone counts as True. Write `if c in ("a", "b"):`. And remember: `=` **stores** a value, `==` **compares** two values.

**Why it matters at work:** reading a file, cleaning bad values without crashing, and summarising by group is the daily job of a junior data scientist. Interviewers also love these three bugs.

### Common mistakes
- Forgetting `newline=""` or the `../` in the CSV path (`FileNotFoundError` means the path is wrong).
- Doing maths on CSV values without `int()` / `float()`.
- Expecting `sorted()` to change the original list. It returns a new one (`lst.sort()` is the in-place version).
- Writing `== None` instead of `is None`.

**Now do exercises 16–30.**
