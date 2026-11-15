# NumPy guide

## How to use this guide
- Each day: read **one Part** (about 10 minutes), then do that Part's exercises in `exercises.ipynb` (about 45 minutes), then spend 5 minutes looking back at what was hard.
- Type the examples yourself in a spare cell. Typing beats reading.
- Stuck on an exercise? `hint(n)` first. After 10 minutes, `answer(n)`, then close it and type the answer from memory.
- Review days: use `cheatsheet.md`.

---

## Part 1: Your first arrays (exercises 1–13)

### What it is
**NumPy** ("Numerical Python") is a library: a package of ready-made code you load into Python. It gives you the **array**, a grid of numbers that you can do maths on all at once. pandas and scikit-learn are built on top of NumPy, so everything later uses it.

You load it with a short nickname:

```python
import numpy as np      # everyone uses "np"
print(np.__version__)   # 2.3.1  (the version you have)
```

### Making arrays
| You want | Write | Result |
|---|---|---|
| From a list | `np.array([4, 8, 15])` | `[ 4  8 15]` |
| All zeros | `np.zeros(4)` | `[0. 0. 0. 0.]` |
| All ones | `np.ones(3)` | `[1. 1. 1.]` |
| All the same value | `np.full(3, 25.0)` | `[25. 25. 25.]` |
| Counting, like `range` | `np.arange(0, 10, 2)` | `[0 2 4 6 8]` (10 not included) |
| N evenly spaced points | `np.linspace(0, 1, 5)` | `[0. 0.25 0.5 0.75 1.]` (1 included) |

A **2D array** is a table: rows and columns. Give its size as a **tuple** (values in round brackets) `(rows, columns)`:

```python
table = np.zeros((2, 3))   # note the double brackets
print(table)
# [[0. 0. 0.]
#  [0. 0. 0.]]
```

The dot after a number (`0.`) means it is a decimal number (a **float**).

### Facts about an array (attributes)
An **attribute** is information stored on an object. You read it with a dot and **no brackets**.

```python
laps = np.array([[31.2, 33.0, 33.4],
                 [29.8, 31.5, 32.0]])
print(laps.shape)  # (2, 3)  -> 2 rows, 3 columns
print(laps.size)   # 6       -> number of values
print(laps.ndim)   # 2       -> number of dimensions (1 = a line, 2 = a table)
print(laps.dtype)  # float64 -> the data type of every value
```

**dtype** (data type) tells you what kind of numbers are stored. Common ones: `int64` (whole numbers), `float64` (decimals), `bool` (True/False). Every value in an array has the same dtype.

```python
a = np.array([1, 2, 3])            # int64
b = np.array([1, 2, 3], dtype=float)  # float64, chosen at creation
c = a.astype(float)                # float64, converted copy; a itself is unchanged
```

### Maths on whole arrays
Maths between an array and a single number happens to **every element**. Maths between two arrays of the same length happens **position by position** (element-wise).

```python
amounts = np.array([10.0, 20.0, 30.0])
print(amounts + 0.35)      # [10.35 20.35 30.35]
print(amounts * 90)        # [ 900. 1800. 2700.]  (EUR -> INR at 90)
other = np.array([1.0, 2.0, 3.0])
print(amounts - other)     # [ 9. 18. 27.]
print(amounts ** 2)        # [100. 400. 900.]     (** means "to the power of")
```

### Why arrays beat lists
```python
print([1, 2, 3] * 2)            # [1, 2, 3, 1, 2, 3]  list is repeated
print(np.array([1, 2, 3]) * 2)  # [2 4 6]             numbers are doubled
```
Arrays do maths without loops, and they are much faster (you will measure this in exercise 63).

**Why it matters at work:** a bank has millions of transactions; converting all amounts to another currency is one line with NumPy.

### Common mistakes
- `np.zeros(3, 4)` gives an error. The shape must be one tuple: `np.zeros((3, 4))`.
- Forgetting that `arange` stops **before** the stop value. `np.arange(50, 400, 50)` does not include 400.
- Writing `laps.shape()` with brackets. Attributes have no brackets.

**Now do exercises 1–13.**

---

## Part 2: Indexing, reshaping and first statistics (exercises 14–27)

### Indexing: getting one value
An **index** is a position number. Counting starts at **0**. Negative numbers count from the end.

```python
a = np.array([12.5, 40.0, 7.25, 120.0, 3.99])
print(a[0])    # 12.5   first
print(a[2])    # 7.25   third
print(a[-1])   # 3.99   last
```

### Slicing: getting a range
A **slice** is `start:stop:step`. Stop is not included. Leave a part empty for "from the beginning" or "to the end".

```python
print(a[:3])    # [12.5  40.   7.25]   first 3
print(a[-2:])   # [120.    3.99]       last 2
print(a[::2])   # [12.5   7.25  3.99]  every second
print(a[::-1])  # reversed
```

### 2D indexing: `[row, column]`
```python
laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])
print(laps[1, 2])     # 32.0  row 1, column 2
print(laps[0, :])     # whole first row   (":" means "all")
print(laps[:, -1])    # whole last column
print(laps[:2, -2:])  # first 2 rows, last 2 columns -> a 2x2 block
```

### Changing values
```python
a[2] = 0        # one value
a[-2:] = 0      # a whole slice gets 0
```

### Reshape and flatten
**reshape** changes the shape without changing the values. The total number of values must stay the same. `-1` means "work this number out for me".

```python
x = np.arange(12)
print(x.reshape(3, 4).shape)   # (3, 4)
print(x.reshape(4, -1).shape)  # (4, 3)  since 12 / 4 = 3
print(x.reshape(3, 4).flatten())  # back to 1D, row by row
```

### Views and copies (important!)
A slice is a **view**: a window onto the same data. Changing the view changes the original. `.copy()` makes an independent copy.

```python
a = np.array([1, 2, 3, 4])
v = a[:2]       # view
v[0] = 99
print(a)        # [99  2  3  4]  the original changed!
c = a[:2].copy()  # copy: safe to change
```

### Random numbers (with a seed)
A **random number generator** (rng) makes "random" numbers. A **seed** (here 42) makes it give the same numbers every run, so your results can be repeated.

```python
rng = np.random.default_rng(42)
print(rng.integers(1, 7, size=5))     # whole numbers 1..6 (7 is excluded)
print(rng.random(3))                  # decimals between 0 and 1
print(rng.uniform(26, 32, size=3))    # decimals between 26 and 32, all equally likely
print(rng.normal(50, 15, size=3))     # "bell curve" around 50, spread 15
```
The **normal distribution** is the bell curve: most values close to the average, fewer far away. Its spread is the **standard deviation**.

### Basic statistics
```python
spend = np.array([14.2, 3.5, 22.0, 8.75, 41.3])
spend.sum(), spend.mean(), spend.min(), spend.max()
np.median(spend)   # the middle value when sorted (no .median() method)
spend.std()        # standard deviation: typical distance from the mean
spend.argmax()     # 4 -> the POSITION of the biggest value
spend.argmin()     # 1 -> the position of the smallest
```
- **mean** = average. **median** = middle value; it ignores extreme values better than the mean.
- **standard deviation (std)** = how spread out values are. Small std = values close together (a consistent swimmer).
- **argmax / argmin** return a position. Use it to look up a matching array, e.g. `days[spend.argmax()]`.

**Why it matters at work:** "Which customer spent the most?" is `argmax`; "how unusual is this payment?" starts with `mean` and `std`.

### Common mistakes
- Off by one: the 3rd element is `a[2]`.
- Changing a slice and being surprised the original changed. Use `.copy()`.
- Confusing `argmax()` (position) with `max()` (value).
- Forgetting the seed, so your numbers differ every run.

**Now do exercises 14–27.**

---

## Part 3: Boolean masks and filtering (exercises 28–40)

### What it is
A comparison on an array gives a **boolean array** (all True/False). This is called a **mask**. Putting a mask in square brackets keeps only the True positions.

```python
amounts = np.array([12.5, 140.0, 7.25, 320.0, 100.0])
mask = amounts > 100
print(mask)            # [False  True False  True False]
print(amounts[mask])   # [140. 320.]
```

### Counting and percentages
True counts as 1 and False as 0. So:

```python
print((amounts > 100).sum())    # 2   -> HOW MANY are above 100
print((amounts > 100).mean())   # 0.4 -> WHAT FRACTION (40%)
```
`len(mask)` is the length of the whole mask, not the number of Trues. (Same trap as `.count()` vs `.sum()` in pandas.)

### Combining conditions
Use `&` (and), `|` (or), `~` (not). **Every condition needs brackets.** Python's `and`/`or` do not work on arrays.

```python
amounts[(amounts >= 50) & (amounts <= 200)]   # between 50 and 200
amounts[(amounts < 10) | (amounts > 300)]     # very small or very big
```

### np.where: two uses
```python
np.where(amounts > 100, "big", "small")   # if/else for every element
# ['small' 'big' 'small' 'big' 'small']

is_fraud = np.array([0, 0, 1, 0, 1])
np.where(is_fraud == 1)[0]                # positions where True: [2 4]
```
With only a condition, `np.where` returns a tuple, so take `[0]`.

### Changing values with a mask
```python
x = np.array([25.0, -10.0, 60.5])
x[x < 0] = 0        # set all negatives to 0
```

### Sorting and unique values
```python
np.sort(times)          # small to big (makes a sorted copy)
np.sort(times)[::-1]    # big to small
values, counts = np.unique(channel, return_counts=True)  # distinct values + how often each appears
```

### One mask, two arrays
If two arrays are in the same order (same row = same swimmer), a mask from one can select from the other:

```python
names = np.array(["Asha", "Rohan", "Meera"])
times = np.array([29.4, 31.2, 28.7])
print(names[times < 30])          # ['Asha' 'Meera']
```

### any and all
```python
np.any(times <= 31)   # True if at least one is True
np.all(times <= 31)   # True only if every one is True
```

**Why it matters at work:** "show me all foreign transactions over 500 EUR" and "what share of transactions are fraud?" are masks plus `.sum()` or `.mean()`.

### Common mistakes
- Forgetting the brackets: `amounts > 50 & amounts < 200` gives an error or a wrong answer.
- Using `and` instead of `&`.
- Counting with `len(mask)` instead of `mask.sum()`.

**Now do exercises 28–40.**

---

## Part 4: Axis, broadcasting, scaling and missing values (exercises 41–52)

### The axis argument
In a 2D table, `axis` says which direction to collapse.
- `axis=0`: go **down** the rows -> one answer **per column**.
- `axis=1`: go **across** the columns -> one answer **per row**.

```python
laps = np.array([[31.2, 33.0, 33.4, 32.1],    # swimmer 0
                 [29.8, 31.5, 32.0, 30.9],    # swimmer 1
                 [34.0, 35.2, 35.9, 34.4]])   # swimmer 2
laps.sum(axis=1)      # [129.7 124.2 139.5] total per swimmer (row)
laps.mean(axis=0)     # average per lap (column), 4 values
laps.argmin(axis=0)   # [1 1 1 1] which row was fastest in each column
```
Memory trick: the axis you name is the one that **disappears**. (3, 4) with `axis=1` -> (3,).

### Broadcasting
**Broadcasting** is NumPy's rule for doing maths on arrays of different shapes: the smaller one is "stretched" to fit. Shapes are compared from the right; each pair of sizes must be equal or one of them must be 1.

```python
marks = np.array([[40, 72, 60],
                  [35, 88, 70]])      # shape (2, 3)
max_marks = np.array([50, 100, 80])   # shape (3,)
marks / max_marks * 100               # each column divided by its own max
# [[80. 72. 75. ]
#  [70. 88. 87.5]]
```
To do something **per row**, you need shape (rows, 1). `keepdims=True` keeps that shape:

```python
row_avg = marks.mean(axis=1, keepdims=True)   # shape (2, 1), not (2,)
marks - row_avg                               # each row minus its own average
```

### Scaling (normalising) data
ML models work better when features are on similar scales (amount in EUR can be 1000s; hour of day is 0–23).

| Method | Formula | Result |
|---|---|---|
| Min-max | `(x - x.min()) / (x.max() - x.min())` | values between 0 and 1 |
| Z-score (standardise) | `(x - x.mean()) / x.std()` | mean 0, std 1 |

A **z-score** tells you how many standard deviations a value is from the average. z = 2 means "2 std above average", which is unusual.

For a table, add `axis=0` to scale **each column** separately:
```python
Z = (X - X.mean(axis=0)) / X.std(axis=0)
```
A mean like `4.4e-17` means 0.000...044: just 0 with rounding noise.

### Joining arrays
```python
np.concatenate([jan, feb])          # join 1D arrays (pass a list!)
np.vstack([table, new_row])         # add rows (vertical)
np.hstack([table, col.reshape(-1, 1)])  # add a column (horizontal); col needs shape (rows, 1)
```

### Missing values: NaN
`np.nan` ("Not a Number") marks a missing value. Any maths with NaN gives NaN, and NaN is not equal to anything, not even itself.

```python
t = np.array([29.4, np.nan, 28.7])
t.mean()            # nan
t == np.nan         # [False False False]  never use this
np.isnan(t)         # [False  True False]  the right test
np.isnan(t).sum()   # 1 missing
np.nanmean(t)       # 29.05  (skips NaN); also nanmin, nanmax, nansum, nanstd
t[~np.isnan(t)]     # drop the NaNs ( ~ flips True/False )
```
Fill missing values with each column's mean:
```python
filled = np.where(np.isnan(X), np.nanmean(X, axis=0), X)
```

**Why it matters at work:** scaling features and handling missing values happens in nearly every ML project, before any model is trained.

### Common mistakes
- Mixing up `axis=0` and `axis=1`. Check the shape of the result: it should have one value per thing you wanted.
- Subtracting row averages without `keepdims=True` (shape error).
- Testing `x == np.nan`. Always use `np.isnan(x)`.

**Now do exercises 41–52.**

---

## Part 5: Fancy indexing, ranking and everyday tools (exercises 53–64)

### Fancy indexing
Index with a **list or array of positions** to pick several items at once, in any order. The result is a copy.

```python
a = np.array([12.5, 140.0, 7.25, 320.0])
a[[0, 3]]          # [ 12.5 320. ]
laps[[2, 0]]       # rows 2 and 0
```
In 2D, two position arrays pair up: `laps[[0, 1, 2], [2, 0, 1]]` picks (0,2), (1,0), (2,1).

### argsort: positions in sorted order
```python
times = np.array([29.4, 31.2, 28.7])
order = np.argsort(times)     # [2 0 1] -> position 2 is smallest, then 0, then 1
names[order]                  # names in finishing order
np.argsort(a)[::-1][:3]       # positions of the 3 BIGGEST values ("top-k")
```

### Running totals and differences
```python
np.cumsum([500, -45, -12.5])        # [500.  455.  442.5]  running total (cumulative sum)
np.diff([30.1, 63.0, 96.8])         # [32.9 33.8]          each value minus the one before
np.diff([30.1, 63.0], prepend=0)    # [30.1 32.9]          keeps the first value too
```

### Percentiles
The **p-th percentile** is the value below which p% of the data lies. The 50th percentile is the median. The **IQR** (interquartile range) = 75th − 25th percentile: the spread of the middle half.

```python
p25, p75 = np.percentile(amounts, [25, 75])
```
Exercise 58 uses `rng.exponential(scale=40, size=1000)`: it makes many small values and a few big ones, which is what real payment amounts look like.

### Clip and round
```python
np.clip(x, 1, 500)     # below 1 -> 1, above 500 -> 500
np.round(x, 2)         # 2 decimals
np.floor(x), np.ceil(x)  # always down / always up
```

### np.select: more than two labels
```python
conditions = [amounts < 20, amounts < 100]
choices = ["small", "medium"]
np.select(conditions, choices, default="large")
```
The **first** True condition wins, so order them carefully.

### Vectorising a loop
**Vectorising** means replacing a Python loop with one array operation. It is shorter and much faster.

```python
# loop:   fee = a * 0.015 if a > 100 else 1.0, for every a
fees = np.where(amounts > 100, amounts * 0.015, 1.0)
np.allclose(fees_loop, fees)   # True if equal (allowing tiny rounding differences)
```
To time code: `import time`, `start = time.perf_counter()`, run the code, then `time.perf_counter() - start` is the seconds taken.

**Why it matters at work:** "top 10 biggest transactions", "95th percentile of amount", "running balance" are daily questions for a data scientist.

### Common mistakes
- `a[0, 3]` (one row 0, column 3) vs `a[[0, 3]]` (items 0 and 3). The inner brackets matter.
- Using `np.sort` when you need positions: use `np.argsort`.
- Putting the `np.select` conditions in the wrong order (the broad one first catches everything).

**Now do exercises 53–64.**

---

## Part 6: Linear algebra basics, distances and files (exercises 65–75)

**Linear algebra** is the maths of vectors and matrices. A **vector** is a 1D array; a **matrix** is a 2D array. ML models are mostly matrix maths underneath.

### Dot product
Multiply matching elements, then add them up. One number comes out.

```python
prices = np.array([2.5, 0.99, 4.2])
qty    = np.array([3,   6,    1])
prices @ qty          # 2.5*3 + 0.99*6 + 4.2*1 = 17.64
np.dot(prices, qty)   # same thing
```

### Matrix times vector
Each row of the matrix is dotted with the vector: one result per row.
```python
scores @ weights    # (4, 3) @ (3,) -> (4,): a weighted grade per student
```

### Matrix times matrix
`A @ B`: entry [i, j] = row i of A dotted with column j of B.
**Shape rule:** (n, k) @ (k, m) -> (n, m). The inner numbers (k) must match, otherwise you get a `ValueError`.

```python
A = np.ones((2, 3)); B = np.ones((3, 2))
(A @ B).shape    # (2, 2)
```

### Transpose and identity
- `M.T` (**transpose**): rows become columns. (3, 4) -> (4, 3).
- `np.eye(3)` (**identity matrix**): 1s on the diagonal, 0s elsewhere. `M @ np.eye(3)` equals `M`, like multiplying by 1.
- `np.array_equal(a, b)` checks two arrays are exactly the same.

### Solving equations
"2a + 3c = 31 and a + 4c = 28" is `A @ x = b` with `A = [[2, 3], [1, 4]]`, `b = [31, 28]`.
```python
x = np.linalg.solve(A, b)    # [8. 5.]
```

### Distances
The **Euclidean distance** is the straight-line distance (Pythagoras): square the differences, add, square root.

```python
p, q = np.array([1.0, 2.0]), np.array([4.0, 6.0])
np.sqrt(((p - q) ** 2).sum())   # 5.0
np.linalg.norm(p - q)           # 5.0  (norm = length of a vector)
```
From one point to many points (broadcasting), one distance per row:
```python
dists = np.linalg.norm(points - p, axis=1)
dists.argmin()                  # the nearest point
```
All pairs at once (a **distance matrix**) uses `None` to add an axis:
```python
diff = pts[:, None, :] - pts[None, :, :]   # shape (n, n, 2)
D = np.linalg.norm(diff, axis=2)           # shape (n, n)
```
`None` inside an index adds a new axis of size 1, so broadcasting can pair every point with every other.

### Saving and loading
```python
import os
os.makedirs("outputs", exist_ok=True)       # create the folder if missing
np.save("outputs/amounts.npy", amounts)     # NumPy's own file format
loaded = np.load("outputs/amounts.npy")
```
Reading numeric columns from a CSV file:
```python
data = np.loadtxt("../data/transactions.csv", delimiter=",",
                  skiprows=1, usecols=(6, 7))   # amount_eur, is_fraud
amounts, is_fraud = data[:, 0], data[:, 1]
```
`skiprows=1` skips the header line; `usecols` picks columns by number (counting from 0). For most CSV work you will use pandas, but this shows NumPy can read files too.

**Why it matters at work:** nearest-neighbour search, recommendation ("similar customers") and every neural network are built on dot products and distances.

### Common mistakes
- Using `*` when you meant `@`. `*` multiplies element by element; `@` is the dot/matrix product.
- Shape mismatch with `@`. Print `.shape` of both sides first.
- Forgetting `axis=1` in `np.linalg.norm`, which gives one number for the whole array.

**Now do exercises 65–75.**

---

## Part 7: Encoding, smoothing and evaluating (exercises 76–83)

From here on, exercises combine ideas. Each one is a small task a junior data scientist really does.

### One-hot encoding
Models need numbers, but codes like `online = 1, contactless = 2` suggest a false order. **One-hot encoding** gives each category its own 0/1 column.

```python
codes = np.array([1, 0, 2])
np.eye(3, dtype=int)[codes]
# [[0 1 0]
#  [1 0 0]
#  [0 0 1]]
```
Row `k` of `np.eye(3)` is the one-hot row for code `k`, so fancy indexing does all rows at once. From strings, first get codes:
```python
names, codes = np.unique(channel, return_inverse=True)  # codes = position of each value in names
```

### Moving average
A **moving average** averages each value with its neighbours to smooth out noise.
```python
np.convolve(spend, np.ones(3) / 3, mode="valid")
```
`np.convolve` slides the window `[1/3, 1/3, 1/3]` along the data, multiplying and adding: that is the average of 3 neighbours. `mode="valid"` only keeps positions where the full window fits (n − 3 + 1 values).

### Outliers with z-scores
An **outlier** is a value far from the rest. A common rule: |z| > 3. In fraud work you usually care about "too big", so `z > 3`.

### The confusion matrix
For a 0/1 prediction there are four outcomes:

| | Really fraud (1) | Really normal (0) |
|---|---|---|
| **Predicted fraud (1)** | TP true positive | FP false positive (false alarm) |
| **Predicted normal (0)** | FN false negative (missed fraud) | TN true negative |

```python
TP = ((y_pred == 1) & (y_true == 1)).sum()
```
- **Accuracy** = (TP + TN) / total: share of all predictions that were right.
- **Precision** = TP / (TP + FP): of the alarms, how many were real fraud?
- **Recall** = TP / (TP + FN): of the real frauds, how many did we catch?

When one class is rare (fraud is ~2%), accuracy can look great while the model is useless. Always compare with the "always predict 0" **baseline**.

### Train/test split by hand
You test a model on rows it has never seen. Shuffle row numbers once, then cut:
```python
rng = np.random.default_rng(42)
idx = rng.permutation(len(X))       # 0..n-1 in random order
cut = int(0.8 * len(X))
X_train, X_test = X[idx[:cut]], X[idx[cut:]]
y_train, y_test = y[idx[:cut]], y[idx[cut:]]   # SAME idx keeps rows and labels together
```

### Spot-the-bug habit
Some exercises give you code that runs without errors but gives wrong results. Read it line by line and ask "is this a view or a copy?", "what dtype is this?", "what happens to the missing values?". Write the explanation as a `#` comment, then show the fix.

**Why it matters at work:** a fraud team reports precision and recall, not accuracy, and every model is judged on a held-out test set.

### Common mistakes
- Shuffling X and y with two different permutations (labels end up on the wrong rows).
- Reporting accuracy on imbalanced data.
- Using `/=` on a slice and changing the original data (view!).

**Now do exercises 76–83.**

---

## Part 8: Traps, neighbours and thresholds (exercises 84–91)

### Integer overflow
Small integer dtypes have limits: `uint8` holds 0–255, `int8` holds −128 to 127. Past the limit the value **wraps around** silently (like a car's odometer rolling from 999 to 000).

```python
np.array([250], dtype=np.uint8) + 10    # [4], not 260!
np.array([250], dtype=np.uint8).astype(np.int64) + 10   # [260]
```

### Floats into an int array
Writing decimals into an existing integer array chops off the decimals, with no warning:
```python
m = np.array([45, 60])
m[:] = [0.7, -1.3]   # m is now [0 -1]
```
Create a new array instead (`z = (m - m.mean()) / m.std()`), or convert first with `.astype(float)`.

### Missing values are not zero
`np.nan_to_num(x)` turns NaN into 0. That is only right if "missing" really means 0. A disqualified swim is "no time", not "0 seconds".
`np.genfromtxt(...)` reads a CSV like `loadtxt` but turns empty cells into NaN instead of crashing.

### Nearest neighbours
To classify a new point, look at the most similar past points.
```python
dists = np.linalg.norm(X_train - new, axis=1)
y_train[dists.argmin()]                # 1 nearest neighbour
k_idx = np.argsort(dists)[:3]          # 3 nearest
np.bincount(y_train[k_idx]).argmax()   # majority vote
```
`np.bincount(labels)` counts how many 0s, 1s, 2s... there are: `np.bincount([1, 0, 1])` is `[1 2]`.

### Group totals with bincount
`np.bincount(codes, weights=amounts)` **adds up** the amounts for each code instead of counting:
```python
codes = np.array([0, 1, 1]); amounts = np.array([20.0, 150.0, 80.0])
np.bincount(codes, weights=amounts)   # [ 20. 230.]
```

### Scores and thresholds
Many models output a **score** (0 to 1). You choose a **threshold**: flag if score ≥ threshold.
- Higher threshold -> fewer alarms -> precision up, recall down.
- Lower threshold -> more alarms -> recall up, precision down.

`(scores >= 0.5).astype(int)` turns True/False into 1/0.

**Why it matters at work:** choosing a fraud threshold is a business decision: missed fraud costs money, false alarms annoy customers.

### Common mistakes
- Assuming integer maths cannot go wrong. Check the dtype.
- Filling NaN with 0 by habit.
- Forgetting that `bincount` needs whole, non-negative numbers.

**Now do exercises 84–91.**

---

## Part 9: Fitting models by hand (exercises 92–100)

### Mean squared error (MSE)
To fit a line `y = w * x`, we need a number that says how wrong a guess for `w` is:
```python
mse = ((w * x - y) ** 2).mean()   # average squared gap between prediction and truth
```
Squaring makes all gaps positive and punishes big misses more. The best `w` has the smallest MSE.

### Gradient descent (in plain words)
Imagine standing on a foggy hill and wanting to reach the bottom. You feel which way the ground slopes, take a small step downhill, and repeat.
- The "hill" is the MSE for every possible `w`.
- The **gradient** is the slope at your current `w`: `grad = 2 * ((w * x - y) * x).mean()`.
- The **learning rate** (e.g. 0.01) is your step size.
- Update: `w = w - learning_rate * grad`. Positive slope -> move left; negative -> move right.

For a line with intercept, `y = w * x + b`, update both:
```python
error = (w * x + b) - y
w -= lr * 2 * (error * x).mean()
b -= lr * 2 * error.mean()
```
`np.polyfit(x, y, 1)` gives the exact best line `[slope, intercept]`, so you can check your answer.

You do not need calculus for these exercises: the gradient formulas are given. (If you are curious, they come from differentiating the MSE, which you did in 12th.)

### Data leakage
**Data leakage** means information from the test set sneaks into training. Example: scaling with the test set's min/max or mean. Always learn these numbers on the training set only, then apply them to the test set.

### Sigmoid and logistic regression
The **sigmoid** function squashes any number into 0..1, so it can be read as a probability:
```python
p = 1 / (1 + np.exp(-s))    # np.exp(s) = e to the power s
```
Logistic regression computes `s = X @ w + b`, then the sigmoid. Training finds good `w` and `b`.

### Cosine similarity
Compares the **direction** (pattern) of two vectors, not their size:
```python
cos = a @ b / (np.linalg.norm(a) * np.linalg.norm(b))   # 1 = same pattern, 0 = unrelated
```

### Bootstrap
How sure are we about an average from only 12 swims? Resample the data **with replacement** (the same value can be picked twice) many times and see how much the average moves.
```python
samples = rng.choice(times, size=(2000, len(times)), replace=True)
means = samples.mean(axis=1)
np.percentile(means, [2.5, 97.5])   # a 95% confidence interval
```

### Putting it together
Exercise 100 is a mini project: load real data, split, learn a threshold on train only, evaluate on test with a confusion matrix, and judge the result honestly.

**Why it matters at work:** interviewers often ask "explain gradient descent" or "what is data leakage?". Doing it by hand once means you can explain it.

### Common mistakes
- Learning rate too big: `w` jumps around and grows. Too small: it barely moves. Try 0.01 first.
- Using test-set statistics anywhere in training.
- Shuffling X and y separately.

**Now do exercises 92–100.**
