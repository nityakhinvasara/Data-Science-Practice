# NumPy: 100 exercises (hints)

_Generated from `tools/source/numpy.ktx`. Don't edit this file; it gets rebuilt._


## Level 1: Easy

#### 1. Import NumPy with its usual short name `np` and print which version you have. (★☆☆)

`hint:` `import numpy as np`, then print `np.__version__` (two underscores on each side).

#### 2. Turn this Python list of transaction amounts (in EUR) into a NumPy array. Print the array and its `type`. (★☆☆)
```python
amounts_list = [12.5, 40.0, 7.25, 120.0, 3.99]
```

`hint:` `np.array(amounts_list)` turns a list into an array. `type(x)` tells you what kind of object `x` is.

#### 3. Make an array of 10 zeros and print it. (★☆☆)

`hint:` `np.zeros(10)`

#### 4. Make an array of 5 ones. Then make a table (2D array) of zeros with 3 rows and 4 columns. Print both. (★☆☆)

`hint:` `np.ones(5)`. For a table, give the shape as a tuple: `np.zeros((3, 4))` (note the double brackets).

#### 5. Every new customer starts with a balance of 25.0 EUR. Make an array that holds the starting balance for 6 customers. (★☆☆)

`hint:` `np.full(how_many, value)` makes an array where every value is the same.

#### 6. Use `np.arange` to make (a) the numbers 0 to 9, and (b) the lane distances 50, 100, 150, ..., 400 (in metres). (★☆☆)

`hint:` `np.arange(start, stop, step)`. The stop value is NOT included, like Python's `range`. So for 400 to appear, stop must be bigger than 400.

#### 7. Make 5 numbers spread evenly from 0 to 1, including both ends. (★☆☆)

`hint:` `np.linspace(start, stop, how_many)`. Unlike `arange`, here the stop value IS included and you choose how many numbers you get.

#### 8. Here are lap times (seconds) for 3 swimmers (rows) over 4 laps (columns). Print the array's `shape`, `size`, `ndim` and `dtype`. (★☆☆)
```python
import numpy as np
laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])
```

`hint:` These are attributes, so no brackets: `laps.shape`, `laps.size`, `laps.ndim`, `laps.dtype`.

#### 9. Make the array `[1, 2, 3]` and print its dtype. Then make a float version of it in two ways: with `dtype=float` when creating it, and with `.astype(float)` on the existing array. (★☆☆)

`hint:` `np.array([1, 2, 3], dtype=float)` or `arr.astype(float)`. `astype` returns a NEW array; it does not change the old one.

#### 10. A bank adds a fixed fee of 0.35 EUR to every card payment. Add the fee to every amount, then also print the amounts doubled. No loops! (★☆☆)
```python
import numpy as np
amounts = np.array([12.5, 40.0, 7.25, 120.0, 3.99])
```

`hint:` Maths with a single number applies to every element: `amounts + 0.35`, `amounts * 2`.

#### 11. Convert these EUR amounts to Indian rupees, using the rate 1 EUR = 90 INR. Print the INR array. (★☆☆)
```python
import numpy as np
amounts_eur = np.array([12.5, 40.0, 7.25, 120.0, 3.99])
```

`hint:` One multiplication: `amounts_eur * 90`.

#### 12. Two swimmers' times (seconds) for the same 4 events are below. Make an array of how much faster swimmer A was in each event (B minus A), and an array of their combined time per event. (★☆☆)
```python
import numpy as np
a = np.array([28.4, 62.1, 135.0, 290.2])
b = np.array([29.0, 61.5, 138.2, 295.0])
```

`hint:` Arrays of the same length combine element by element: `b - a`, `a + b`.

#### 13. Why arrays beat lists: multiply the Python list `[1, 2, 3]` by 2, then multiply the array `np.array([1, 2, 3])` by 2. Also square the array with `** 2`. Print all three and notice the difference. (★☆☆)

`hint:` A list times 2 repeats the list. An array times 2 doubles each number.

#### 14. Print the first, the third and the last amount. Use a negative index for the last one. (★☆☆)
```python
import numpy as np
amounts = np.array([12.5, 40.0, 7.25, 120.0, 3.99, 56.0])
```

`hint:` Counting starts at 0, so the third element is `amounts[2]`. `amounts[-1]` is the last one.

#### 15. Using slicing, print: the first 3 amounts, the last 2 amounts, and every second amount starting from the first. (★☆☆)
```python
import numpy as np
amounts = np.array([12.5, 40.0, 7.25, 120.0, 3.99, 56.0])
```

`hint:` Slices are `start:stop:step`, stop not included. First 3: `[:3]`. Last 2: `[-2:]`. Every second: `[::2]`.

#### 16. Reverse the order of this array of swim times. (★☆☆)
```python
import numpy as np
times = np.array([30.1, 29.8, 31.4, 28.9, 30.5])
```

`hint:` A step of -1 walks backwards: `times[::-1]`.

#### 17. Using the lap table, print: swimmer 2's time on lap 3 (remember counting starts at 0), all of swimmer 1's laps (the first row), and everyone's time on the last lap (last column). (★☆☆)
```python
import numpy as np
laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])
```

`hint:` 2D indexing is `laps[row, column]`. A `:` means "all". So a whole row is `laps[0, :]` and a whole column is `laps[:, -1]`.

#### 18. From the same lap table, cut out the first two swimmers and only their last two laps (a 2x2 block). (★☆☆)
```python
import numpy as np
laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])
```

`hint:` Slice rows and columns at the same time: `laps[:2, -2:]` or `laps[0:2, 2:4]`.

#### 19. A payment at position 2 was cancelled: set it to 0. Then the last two payments were also cancelled: set both to 0 in one line. Print the array after each change. (★☆☆)
```python
import numpy as np
amounts = np.array([12.5, 40.0, 7.25, 120.0, 3.99, 56.0])
```

`hint:` Assign to an index or a slice: `amounts[2] = 0`, `amounts[-2:] = 0`.

#### 20. Make the numbers 0 to 11 with `arange`, then reshape them into a 3x4 table. Then reshape the same numbers into 4 rows and let NumPy work out the number of columns. (★☆☆)

`hint:` `np.arange(12).reshape(3, 4)`. Use `-1` for "work it out for me": `.reshape(4, -1)`. The total (12) must stay the same.

#### 21. Flatten the lap table into one long 1D array (all of swimmer 1's laps, then swimmer 2's, ...). How many values does it have? (★☆☆)
```python
import numpy as np
laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])
```

`hint:` `laps.flatten()` gives a 1D copy, row by row. `.size` (or `len`) tells you how many values.

#### 22. Copies vs views. Run the code below and print `amounts` at the end. Why did `amounts` change? Then fix it with `.copy()` so that `amounts` stays the same. (★☆☆)
```python
import numpy as np
amounts = np.array([12.5, 40.0, 7.25, 120.0])
first_two = amounts[:2]
first_two[0] = 999
```

`hint:` A slice is a **view**: a window onto the SAME data, not a new array. `amounts[:2].copy()` makes an independent copy.

#### 23. Create a random number generator with seed 42 and roll a dice 10 times (whole numbers 1 to 6). (★☆☆)

`hint:` `rng = np.random.default_rng(42)`, then `rng.integers(1, 7, size=10)`. The upper value 7 is NOT included, so you get 1..6.

#### 24. With a seeded generator (seed 42), simulate 8 swim times for the 50 m freestyle, each a decimal number between 26 and 32 seconds. Then simulate 5 transaction amounts from a normal ("bell curve") distribution with mean 50 and standard deviation 15. (★☆☆)

`hint:` `rng.uniform(26, 32, size=8)` gives any decimal in that range, all equally likely. `rng.normal(50, 15, size=5)` gives values that cluster around 50.

#### 25. A student's daily spending (EUR) for one week is below. Print the total, the average, the smallest and the largest day. (★☆☆)
```python
import numpy as np
spend = np.array([14.2, 3.5, 22.0, 8.75, 41.3, 5.0, 17.6])
```

`hint:` `spend.sum()`, `spend.mean()`, `spend.min()`, `spend.max()`.

#### 26. Two swimmers have the same average 100 m time, but one is much more consistent. Print the mean, median and standard deviation of each. Which one is more consistent? (★☆☆)
```python
import numpy as np
steady = np.array([62.0, 61.8, 62.3, 62.1, 61.9])
up_down = np.array([58.5, 66.0, 60.1, 64.9, 60.6])
```

`hint:` `x.mean()`, `np.median(x)` (there is no `.median()` method), `x.std()`. Standard deviation = how spread out the values are; smaller = more consistent.

#### 27. Which day had the biggest spend (print its position and the value)? Which day had the smallest? (★☆☆)
```python
import numpy as np
spend = np.array([14.2, 3.5, 22.0, 8.75, 41.3, 5.0, 17.6])
days = np.array(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
```

`hint:` `spend.argmax()` gives the POSITION of the biggest value, not the value. Use that position to index `days` and `spend`.

#### 28. Make a True/False array showing which amounts are above 100 EUR. (★☆☆)
```python
import numpy as np
amounts = np.array([12.5, 140.0, 7.25, 320.0, 99.99, 100.0, 56.0])
```

`hint:` A comparison on an array, like `amounts > 100`, compares every element and gives a boolean (True/False) array.

#### 29. Use that mask to keep only the amounts above 100 EUR. (★☆☆)
```python
import numpy as np
amounts = np.array([12.5, 140.0, 7.25, 320.0, 99.99, 100.0, 56.0])
```

`hint:` Put the mask inside square brackets: `amounts[amounts > 100]`.

#### 30. How MANY amounts are above 100 EUR? (Careful: you want a count of the True values.) (★☆☆)
```python
import numpy as np
amounts = np.array([12.5, 140.0, 7.25, 320.0, 99.99, 100.0, 56.0])
```

`hint:` True counts as 1 and False as 0, so `(amounts > 100).sum()` counts the Trues. `len(amounts > 100)` would wrongly give 7 (the length of the whole mask).

#### 31. Find amounts that are between 50 and 200 EUR (inclusive). Then find amounts that are either under 10 or over 300. (★☆☆)
```python
import numpy as np
amounts = np.array([12.5, 140.0, 7.25, 320.0, 99.99, 100.0, 56.0])
```

`hint:` Combine masks with `&` (and) and `|` (or). Each condition needs its own brackets: `(amounts >= 50) & (amounts <= 200)`. Python's `and` / `or` do NOT work on arrays.

#### 32. What percentage of these 12 transactions were fraud (1 = fraud, 0 = normal)? Use `.mean()`. (★☆☆)
```python
import numpy as np
is_fraud = np.array([0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0])
```

`hint:` The mean of 0/1 values (or of True/False) is the fraction of 1s. Multiply by 100 for a percentage.

#### 33. Label every amount as `"big"` if it is over 100 EUR, else `"small"`, in one line. (★☆☆)
```python
import numpy as np
amounts = np.array([12.5, 140.0, 7.25, 320.0, 99.99, 100.0, 56.0])
```

`hint:` `np.where(condition, value_if_true, value_if_false)` works like an if/else on every element.

#### 34. At which positions (indices) are the fraud cases? (★☆☆)
```python
import numpy as np
is_fraud = np.array([0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0])
```

`hint:` `np.where(condition)` with ONLY a condition returns the positions where it is True (inside a tuple, so take `[0]`). `np.flatnonzero(is_fraud == 1)` is another way.

#### 35. Negative amounts are refunds. Replace every negative amount with 0, changing the array in place. (★☆☆)
```python
import numpy as np
amounts = np.array([25.0, -10.0, 60.5, -3.2, 14.0])
```

`hint:` Assign through a mask: `amounts[amounts < 0] = 0`.

#### 36. Sort these 100 m times from fastest to slowest, then from slowest to fastest. (★☆☆)
```python
import numpy as np
times = np.array([64.2, 61.9, 66.5, 60.3, 63.0])
```

`hint:` `np.sort(times)` sorts small to big (fastest first for times). Reverse that with `[::-1]` for the other order.

#### 37. Which payment channels appear in this list, and how many times does each appear? (★☆☆)
```python
import numpy as np
channel = np.array(["online", "in_store", "online", "contactless",
                    "online", "in_store", "contactless", "online"])
```

`hint:` `np.unique(channel, return_counts=True)` gives two arrays: the distinct values and how often each appears.

#### 38. Which swimmers swam the 50 m freestyle in under 30 seconds? Print their names. (★☆☆)
```python
import numpy as np
names = np.array(["Asha", "Rohan", "Meera", "Kabir", "Isha", "Dev"])
times = np.array([29.4, 31.2, 28.7, 30.0, 29.9, 32.5])
```

`hint:` Build the mask from one array and use it on the OTHER array: `names[times < 30]`. This works because both arrays are in the same order.

#### 39. Is the average fraud transaction bigger than the average normal one? Print both averages. (★☆☆)
```python
import numpy as np
amounts  = np.array([23.0, 410.0, 15.5, 8.0, 999.0, 42.0, 61.0, 350.0, 12.0, 30.0])
is_fraud = np.array([0,    1,     0,    0,   1,     0,    0,    1,     0,    0])
```

`hint:` `amounts[is_fraud == 1].mean()` and `amounts[is_fraud == 0].mean()`.

#### 40. The qualifying time for the state meet is 31.0 seconds. Did ANY swimmer qualify? Did ALL of them qualify? (★☆☆)
```python
import numpy as np
times = np.array([29.4, 31.2, 28.7, 30.0, 29.9, 32.5])
```

`hint:` `np.any(mask)` is True if at least one value is True; `np.all(mask)` only if every value is True.


## Level 2: Medium

#### 41. Using the lap table (rows = swimmers, columns = laps), print each swimmer's total time and the average time for each lap. (★★☆)
```python
import numpy as np
laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])
```

`hint:` `axis=1` works ACROSS the columns, giving one result per row: `laps.sum(axis=1)`. `axis=0` works DOWN the rows, giving one result per column: `laps.mean(axis=0)`.

#### 42. Which swimmer (row number) had the fastest total time? And for each lap, which swimmer was fastest on that lap? (★★☆)
```python
import numpy as np
laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])
```

`hint:` Fastest = smallest time, so use `argmin`. `laps.sum(axis=1).argmin()` for totals; `laps.argmin(axis=0)` gives one row number per column.

#### 43. Four students' raw marks in 3 tests are below. Test maximums are 50, 100 and 80. Turn every mark into a percentage in ONE line (no loops). (★★☆)
```python
import numpy as np
marks = np.array([[40, 72, 60],
                  [35, 88, 70],
                  [48, 65, 52],
                  [30, 91, 77]])
max_marks = np.array([50, 100, 80])
```

`hint:` **Broadcasting**: when shapes are (4, 3) and (3,), NumPy repeats the small array for every row. So `marks / max_marks * 100` divides each column by its own maximum.

#### 44. For each student (row) subtract that student's own average mark, so you can see which test was above or below their personal average. Use the percentages below. (★★☆)
```python
import numpy as np
pct = np.array([[80.0, 72.0, 75.0],
                [70.0, 88.0, 87.5],
                [96.0, 65.0, 65.0],
                [60.0, 91.0, 96.25]])
```

`hint:` `pct.mean(axis=1)` has shape (4,), which does not line up with (4, 3). Use `pct.mean(axis=1, keepdims=True)` to get shape (4, 1): one value per row that broadcasts across the columns.

#### 45. **Min-max normalise** these amounts so the smallest becomes 0 and the biggest becomes 1. (★★☆)
```python
import numpy as np
amounts = np.array([20.0, 35.0, 50.0, 80.0, 220.0])
```

`hint:` Formula: `(x - x.min()) / (x.max() - x.min())`.

#### 46. **Standardise** (z-score) the same amounts: subtract the mean, divide by the standard deviation. Check that the result has mean about 0 and standard deviation 1. (★★☆)
```python
import numpy as np
amounts = np.array([20.0, 35.0, 50.0, 80.0, 220.0])
```

`hint:` `z = (x - x.mean()) / x.std()`. A z-score says "how many standard deviations away from the average" a value is. The mean may print as something tiny like `4e-17`: that is just 0 with rounding noise.

#### 47. Each row is a transaction with two features: amount (EUR) and hour of day. Standardise EACH column separately so both features are on the same scale. (★★☆)
```python
import numpy as np
X = np.array([[25.0, 14],
              [310.0, 2],
              [42.0, 19],
              [18.0, 11],
              [95.0, 23]])
```

`hint:` Same z-score formula, but with `axis=0` so you get one mean and one std per column: `(X - X.mean(axis=0)) / X.std(axis=0)`. Broadcasting does the rest.

#### 48. Join January and February transaction amounts into one array. (★★☆)
```python
import numpy as np
jan = np.array([12.0, 45.5, 8.25])
feb = np.array([60.0, 3.5, 19.0, 77.7])
```

`hint:` `np.concatenate([jan, feb])`. Note the arrays go inside a list (square brackets).

#### 49. A new swimmer joins: add their 4 lap times as a new row of the table. Then add a column of each swimmer's total time on the right. (★★☆)
```python
import numpy as np
laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9]])
new = np.array([30.5, 32.0, 32.8, 31.6])
```

`hint:` `np.vstack([laps, new])` stacks vertically (adds rows). For a new column, the totals must be shape (rows, 1): `totals.reshape(-1, 1)`, then `np.hstack([table, totals])` (stacks horizontally).

#### 50. Two swimmers were disqualified, so their times are missing (`np.nan` means "Not a Number", NumPy's marker for a missing value). Print the plain `.mean()` and see what happens. Then count how many values are missing. (★★☆)
```python
import numpy as np
times = np.array([29.4, np.nan, 28.7, 30.0, np.nan, 32.5])
```

`hint:` Any maths with NaN gives NaN. You cannot test for NaN with `== np.nan` (it is always False); use `np.isnan(times)`, then `.sum()` to count.

#### 51. Now get the average and fastest time while ignoring the missing values, in two ways: (a) with NaN-aware functions, (b) by dropping the NaNs with a mask first. (★★☆)
```python
import numpy as np
times = np.array([29.4, np.nan, 28.7, 30.0, np.nan, 32.5])
```

`hint:` (a) `np.nanmean(times)`, `np.nanmin(times)`. (b) `times[~np.isnan(times)]` keeps the non-missing values; `~` flips True and False.

#### 52. Some sensor readings are missing in this feature table. Fill each missing value with the mean of ITS column (ignoring NaNs). (★★☆)
```python
import numpy as np
X = np.array([[1.0, 200.0, 3.0],
              [np.nan, 180.0, 5.0],
              [4.0, np.nan, 4.0],
              [3.0, 220.0, np.nan]])
```

`hint:` `col_means = np.nanmean(X, axis=0)` gives shape (3,). Then `np.where(np.isnan(X), col_means, X)`: where X is missing take the column mean (broadcast over rows), otherwise keep X.

#### 53. Pick out transactions number 0, 3 and 5 in one go. Then, from the lap table, pick rows 2 and 0 (in that order). (★★☆)
```python
import numpy as np
amounts = np.array([12.5, 140.0, 7.25, 320.0, 99.99, 100.0, 56.0])
laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])
```

`hint:` **Fancy indexing**: index with a LIST of positions, e.g. `amounts[[0, 3, 5]]` (double brackets: the inner ones make the list). `laps[[2, 0]]` picks whole rows.

#### 54. Print the swimmers' names in finishing order (fastest first). (★★☆)
```python
import numpy as np
names = np.array(["Asha", "Rohan", "Meera", "Kabir", "Isha", "Dev"])
times = np.array([29.4, 31.2, 28.7, 30.0, 29.9, 32.5])
```

`hint:` `np.argsort(times)` returns the POSITIONS that would sort `times`. Use those positions to index `names`.

#### 55. Find the 3 biggest transactions: print their positions and amounts, biggest first. (★★☆)
```python
import numpy as np
amounts = np.array([12.5, 140.0, 7.25, 320.0, 99.99, 100.0, 56.0, 870.0])
```

`hint:` `np.argsort(amounts)[::-1]` gives positions from biggest to smallest; then take the first 3 with `[:3]`.

#### 56. A student starts the month with 0 EUR. Below are money in (+) and out (-) each day. Print the balance after each day. (★★☆)
```python
import numpy as np
flows = np.array([500.0, -45.0, -12.5, -200.0, 150.0, -80.0])
```

`hint:` `np.cumsum(flows)` gives a running total: first value, first+second, first+second+third, ...

#### 57. A 200 m race gives **split times**: the clock reading at 50, 100, 150 and 200 m. Work out how long each 50 m lap took. Which lap was slowest? (★★☆)
```python
import numpy as np
splits = np.array([30.1, 63.0, 96.8, 129.4])
```

`hint:` `np.diff(x)` gives the differences between neighbours (x[1]-x[0], x[2]-x[1], ...). It returns one fewer value, so add the first lap back: `np.diff(splits, prepend=0)`.

#### 58. Print the 25th, 50th, 75th and 95th percentiles of these amounts, and the **interquartile range** (IQR = 75th minus 25th percentile). (★★☆)
```python
import numpy as np
rng = np.random.default_rng(42)
amounts = rng.exponential(scale=40, size=1000)
```

`hint:` `np.percentile(amounts, [25, 50, 75, 95])` returns all four at once. The p-th percentile is the value below which p% of the data falls.

#### 59. A few huge amounts can distort a chart or a model. Cap all amounts at 500 EUR (anything above becomes 500) and raise anything below 1 EUR to 1. (★★☆)
```python
import numpy as np
amounts = np.array([0.2, 45.0, 1200.0, 18.0, 640.0, 3.0])
```

`hint:` `np.clip(amounts, 1, 500)` squeezes every value into the range 1..500.

#### 60. Convert to INR at 90.37 INR per EUR and round to 2 decimals. Also print the EUR amounts rounded down and rounded up to whole euros. (★★☆)
```python
import numpy as np
amounts = np.array([12.345, 40.5, 7.999, 120.01])
```

`hint:` `np.round(x, 2)` rounds to 2 decimals. `np.floor(x)` always rounds down, `np.ceil(x)` always rounds up.

#### 61. Put every amount into a size band: under 20 -> "small", 20 to under 100 -> "medium", 100 to under 500 -> "large", 500 or more -> "huge". (★★☆)
```python
import numpy as np
amounts = np.array([5.0, 25.0, 99.0, 100.0, 480.0, 1500.0, 19.99])
```

`hint:` `np.select(list_of_conditions, list_of_choices, default=...)`: the FIRST condition that is True decides the label. Order the conditions from smallest to biggest.

#### 62. Rewrite this loop without a loop (vectorise it) using `np.where`, and check that both give the same result. (★★☆)
```python
import numpy as np
amounts = np.array([45.0, 150.0, 99.0, 1200.0, 20.0])
fees = []
for a in amounts:
    if a > 100:
        fees.append(a * 0.015)   # 1.5% fee on big payments
    else:
        fees.append(1.0)         # flat 1 EUR fee otherwise
fees = np.array(fees)
```

`hint:` `np.where(amounts > 100, amounts * 0.015, 1.0)`. Compare decimal arrays with `np.allclose(a, b)` (it allows tiny rounding differences).

#### 63. How much faster is NumPy? Make the numbers 0 to 999,999. Compute the sum of their squares (a) with a Python loop over a list and (b) with NumPy. Time both with `time.perf_counter()`. (★★☆)

`hint:` `start = time.perf_counter()` before, `time.perf_counter() - start` after. For NumPy: `(x ** 2).sum()`. Use `dtype=np.int64` so the big total fits.

#### 64. For each swimmer (row), find which lap was their fastest AND what that time was, without a loop. (★★☆)
```python
import numpy as np
laps = np.array([[31.2, 33.0, 30.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 33.2, 35.9, 34.4]])
```

`hint:` `best = laps.argmin(axis=1)` gives one column number per row. Pair it with the row numbers `np.arange(3)` and fancy-index: `laps[np.arange(3), best]`.

#### 65. A shopping basket: prices (EUR) and how many of each item. Compute the total bill with a **dot product**. (★★☆)
```python
import numpy as np
prices = np.array([2.5, 0.99, 4.2, 12.0])
qty = np.array([3, 6, 1, 2])
```

`hint:` The dot product multiplies matching elements and adds them up: `prices @ qty` or `np.dot(prices, qty)`. Same as `(prices * qty).sum()`.

#### 66. Final grade = 20% quiz + 30% project + 50% exam. Compute every student's final grade with one matrix-vector product. (★★☆)
```python
import numpy as np
scores = np.array([[80, 70, 65],
                   [92, 85, 78],
                   [55, 60, 72],
                   [70, 95, 88]])   # columns: quiz, project, exam
weights = np.array([0.2, 0.3, 0.5])
```

`hint:` `scores @ weights`: each row is dotted with the weights, so (4, 3) @ (3,) gives 4 grades.

#### 67. **Transpose** the lap table so rows become laps and columns become swimmers. Print the shape before and after. (★★☆)
```python
import numpy as np
laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])
```

`hint:` `laps.T` flips rows and columns.

#### 68. Multiply a 2x3 matrix `A` by a 3x2 matrix `B` with `@`. What shape is the result? Then try `A @ A` inside `try/except` and print the error message: why does it fail? (★★☆)
```python
import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[1, 0],
              [0, 1],
              [2, 2]])
```

`hint:` Rule: (n, k) @ (k, m) -> (n, m). The two inner numbers must match. (2, 3) @ (2, 3) has inner numbers 3 and 2, so it fails.

#### 69. Make a 3x3 **identity matrix** (1s on the diagonal, 0s elsewhere). Show that multiplying a matrix by it changes nothing. (★★☆)
```python
import numpy as np
M = np.array([[2, 7, 1],
              [0, 3, 5],
              [4, 4, 9]])
```

`hint:` `np.eye(3)`. Then compare with `np.array_equal(M @ I, M)`. The identity matrix is the "multiply by 1" of matrices.

#### 70. Compute the straight-line (**Euclidean**) distance between two points, first with the formula and then with `np.linalg.norm`. (★★☆)
```python
import numpy as np
p = np.array([1.0, 2.0])
q = np.array([4.0, 6.0])
```

`hint:` Formula: square root of the sum of squared differences, `np.sqrt(((p - q) ** 2).sum())`. `np.linalg.norm(p - q)` does the same.

#### 71. A customer is at position (2, 3) on a city map. There are 5 ATMs. Compute the distance to every ATM at once and print which ATM is nearest. (★★☆)
```python
import numpy as np
customer = np.array([2.0, 3.0])
atms = np.array([[0.0, 0.0],
                 [5.0, 4.0],
                 [2.5, 2.0],
                 [1.0, 7.0],
                 [3.0, 3.5]])
```

`hint:` `atms - customer` broadcasts: (5, 2) minus (2,). Then square, sum with `axis=1` (across x and y), and take the square root. Or `np.linalg.norm(atms - customer, axis=1)`. Finish with `argmin`.

#### 72. Make the full **distance matrix** for 4 points: entry [i, j] is the distance between point i and point j. (★★☆)
```python
import numpy as np
pts = np.array([[0.0, 0.0],
                [3.0, 4.0],
                [6.0, 0.0],
                [3.0, 1.0]])
```

`hint:` Add a new axis so broadcasting pairs every point with every point: `pts[:, None, :] - pts[None, :, :]` has shape (4, 4, 2). Then norm over the last axis: `np.linalg.norm(..., axis=2)`.

#### 73. Solve two equations with NumPy. At a swim meet, 2 adult tickets and 3 child tickets cost 31 EUR; 1 adult and 4 child tickets cost 28 EUR. What does each ticket cost? (★★☆)

`hint:` Write it as a matrix `A` (the numbers of tickets) times unknown prices `x` = totals `b`: `A = [[2, 3], [1, 4]]`, `b = [31, 28]`. Then `np.linalg.solve(A, b)`.

#### 74. Save an array of simulated amounts to `outputs/amounts.npy`, load it back, and check that it is identical. (★★☆)
```python
import numpy as np
rng = np.random.default_rng(42)
amounts = rng.normal(60, 20, size=100).round(2)
```

`hint:` `os.makedirs("outputs", exist_ok=True)` creates the folder. Then `np.save(path, array)` and `np.load(path)`. Compare with `np.array_equal`.

#### 75. Load the real data: read the `amount_eur` and `is_fraud` columns of `../data/transactions.csv` (columns 6 and 7, counting from 0) into NumPy. Print the number of rows, the average amount and the fraud rate. (★★☆)

`hint:` `np.loadtxt("../data/transactions.csv", delimiter=",", skiprows=1, usecols=(6, 7))`. `skiprows=1` skips the header line. You get a 2D array: column 0 = amount, column 1 = is_fraud.


## Level 3: Hard

#### 76. **One-hot encoding** by hand. Payment channels are stored as codes: 0 = in_store, 1 = online, 2 = contactless. Turn them into a table with one column per channel, holding 1 where that row has that channel and 0 elsewhere. (★★★)
```python
import numpy as np
codes = np.array([1, 0, 2, 1, 1, 0])
```

`hint:` Each row of `np.eye(3)` is already a one-hot row (row 1 is `[0, 1, 0]`). So fancy-index it with the codes: `np.eye(3)[codes]`.

#### 77. One-hot encode the channel NAMES directly (strings). First turn the names into codes 0, 1, 2 with `np.unique`, then one-hot encode as before. Print the column names too. (★★★)
```python
import numpy as np
channel = np.array(["online", "in_store", "online", "contactless", "in_store"])
```

`hint:` `names, codes = np.unique(channel, return_inverse=True)`. `codes` says, for each row, the position of its value in `names`. Then `np.eye(len(names), dtype=int)[codes]`.

#### 78. Compute the 3-day **moving average** of daily spending (the average of each day and the two days before it). Use `np.convolve`. (★★★)
```python
import numpy as np
spend = np.array([20.0, 35.0, 5.0, 50.0, 10.0, 40.0, 25.0])
```

`hint:` `np.convolve(spend, np.ones(3) / 3, mode="valid")` slides a window of 3 weights (each 1/3) along the data and sums: that is the average of 3 neighbours. `mode="valid"` keeps only full windows, so you get 7 - 3 + 1 = 5 values.

#### 79. **Outlier detection** on the real transactions: compute the z-score of every amount and flag those with z > 3. How many are flagged? What is the fraud rate among flagged transactions compared with all transactions? (★★★)

`hint:` Load as in exercise 75. `z = (amounts - amounts.mean()) / amounts.std()`, `flag = z > 3`. Fraud rate in the flagged group: `is_fraud[flag].mean()`.

#### 80. **Spot the bug.** This function should return normalised amounts and leave the original alone. But after calling it, `raw` has changed. Find the bug, explain it in a comment and fix it. (★★★)
```python
import numpy as np

def scale_first_week(amounts):
    week = amounts[:7]
    week /= week.max()        # scale to 0..1
    return week

raw = np.array([20.0, 50.0, 10.0, 40.0, 80.0, 30.0, 60.0, 90.0, 15.0])
scaled = scale_first_week(raw)
print(raw)
```

`hint:` `amounts[:7]` is a view (exercise 22), and `/=` changes values IN PLACE, so it writes into `raw`. Use `amounts[:7].copy()`, or `week = week / week.max()` which makes a new array.

#### 81. A fraud model made predictions (1 = fraud). Count the four cells of the **confusion matrix**: TP (true positive: predicted 1, really 1), FP (predicted 1, really 0), FN (predicted 0, really 1), TN (predicted 0, really 0). Then compute accuracy, precision and recall. (★★★)
```python
import numpy as np
y_true = np.array([0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0])
y_pred = np.array([0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0])
```

`hint:` Combine masks: `TP = ((y_pred == 1) & (y_true == 1)).sum()`, and so on. Accuracy = (TP + TN) / total. Precision = TP / (TP + FP): "of the alarms, how many were real?". Recall = TP / (TP + FN): "of the real frauds, how many did we catch?".

#### 82. **Why is this misleading?** A colleague says: "My fraud model is 98% accurate on our transactions!" Their "model" predicts 0 (not fraud) for every transaction. Compute its accuracy and recall on the real data and explain in a comment why accuracy is the wrong number to report here. (★★★)

`hint:` Load `is_fraud` as in exercise 75. `y_pred = np.zeros_like(y_true)`. Accuracy = `(y_pred == y_true).mean()`. Recall = caught frauds / all frauds.

#### 83. **Train/test split by hand.** Shuffle the 10 rows below with a seeded random permutation, then put the first 80% into a training set and the rest into a test set. Keep `X` and `y` lined up. (★★★)
```python
import numpy as np
X = np.arange(20).reshape(10, 2)   # 10 rows, 2 features
y = np.array([0, 1, 0, 0, 1, 0, 1, 0, 0, 1])
```

`hint:` `idx = rng.permutation(10)` gives the numbers 0..9 in random order. Use the SAME `idx` for X and y: `X[idx]`, `y[idx]`. Then slice: the first 8 for training, the last 2 for testing.

#### 84. **Spot the bug.** Image pixels are often stored as `uint8` (whole numbers 0 to 255). Someone brightens an image by adding 100, and someone else adds up two big `int8` counts. Run the code, explain the strange results in comments, and fix them. (★★★)
```python
import numpy as np
pixels = np.array([100, 150, 200, 250], dtype=np.uint8)
print(pixels + 100)

counts = np.array([100, 90], dtype=np.int8)   # int8 holds -128..127
print(counts.sum(dtype=np.int8))
```

`hint:` Small integer types **overflow**: past the maximum they wrap around (like a car's odometer going from 999 back to 000). Convert to a bigger type first, e.g. `pixels.astype(np.int64) + 100`, then `np.clip` to 0..255 if needed.

#### 85. **Why is this misleading?** Load the real 50 m swim results (columns `distance_m` and `time_sec`, numbers 7 and 8). Disqualified swims have no time (NaN). A coach replaces the missing times with 0 before averaging. Compare that average with the correct one and explain the difference. (★★★)

`hint:` `np.genfromtxt("../data/swim_results.csv", delimiter=",", skip_header=1, usecols=(7, 8))` turns empty cells into NaN (`loadtxt` would crash on them). Keep rows where distance == 50, then compare `np.nan_to_num(t).mean()` (NaN -> 0) with `np.nanmean(t)`.

#### 86. **Nearest neighbour** by hand. Each row of `X_train` is a past transaction: (amount in hundreds of EUR, hour / 24). `y_train` says if it was fraud. Classify the new transaction by copying the label of the closest past transaction. (★★★)
```python
import numpy as np
X_train = np.array([[0.2, 0.50], [0.4, 0.60], [3.5, 0.10],
                    [0.3, 0.45], [4.0, 0.05], [0.1, 0.70]])
y_train = np.array([0, 0, 1, 0, 1, 0])
new = np.array([3.2, 0.12])
```

`hint:` Distances from `new` to every row, as in exercise 71: `np.linalg.norm(X_train - new, axis=1)`. The prediction is `y_train[dists.argmin()]`.

#### 87. Now use **k = 3 nearest neighbours**: find the 3 closest training points and predict the label that appears most often among them (a majority vote). (★★★)
```python
import numpy as np
X_train = np.array([[1.0, 1.0], [1.5, 2.0], [3.0, 4.0],
                    [5.0, 7.0], [3.5, 5.0], [4.5, 5.0], [3.5, 4.5]])
y_train = np.array([0, 0, 1, 1, 1, 1, 0])
new = np.array([3.0, 3.5])
```

`hint:` `np.argsort(dists)[:3]` gives the positions of the 3 closest. `np.bincount(labels)` counts how many 0s, 1s, ... there are; `.argmax()` of that is the winning label.

#### 88. Group statistics by hand: compute the total and average amount for each channel code (0, 1, 2) WITHOUT a loop. (★★★)
```python
import numpy as np
codes = np.array([0, 1, 1, 2, 0, 1, 2, 2, 1])
amounts = np.array([20.0, 150.0, 80.0, 12.0, 35.0, 300.0, 8.0, 15.0, 95.0])
```

`hint:` `np.bincount(codes)` counts rows per code. `np.bincount(codes, weights=amounts)` ADDS the amounts per code instead of counting. Average = sums / counts.

#### 89. **Spot the bug.** This code tries to standardise student marks in place, but every result comes out as a whole number. Explain why and fix it. (★★★)
```python
import numpy as np
marks = np.array([45, 60, 75, 90, 30])
marks[:] = (marks - marks.mean()) / marks.std()
print(marks)
```

`hint:` `marks` has dtype int64. Writing decimals INTO an int array chops off the decimal part (no warning). Make a new float array instead: `z = (marks - marks.mean()) / marks.std()`.

#### 90. A model gives each transaction a fraud **score** between 0 and 1. You flag a transaction when its score is at least a threshold. For thresholds 0.3, 0.5 and 0.7, print precision and recall. What happens as the threshold goes up? (★★★)
```python
import numpy as np
scores = np.array([0.05, 0.92, 0.40, 0.65, 0.10, 0.81, 0.33, 0.55, 0.20, 0.75])
y_true = np.array([0,    1,    0,    1,    0,    1,    0,    0,    0,    0])
```

`hint:` Loop over the thresholds. Inside: `y_pred = (scores >= t).astype(int)`, then TP, FP, FN as in exercise 81.

#### 91. A simple rule on the real data: flag every transaction above the 95th percentile of amount. Print how many are flagged, the precision and the recall of this rule. (★★★)

`hint:` Load as in exercise 75. `cut = np.percentile(amounts, 95)`, `y_pred = amounts > cut`. Then precision and recall as in exercise 81.

#### 92. Fitting a line, step 1: the **mean squared error** (MSE). For the data below we guess the line `y = w * x`. Try every `w` from 0 to 4 in steps of 0.1, compute the MSE for each, and print the `w` with the smallest error. (★★★)
```python
import numpy as np
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])        # study hours (tens of hours)
y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])       # marks (tens of marks)
```

`hint:` MSE for one `w` = `((w * x - y) ** 2).mean()`: the average squared gap between prediction and truth. Make `ws = np.arange(0, 4.01, 0.1)`, compute a list of MSEs in a loop (or a list comprehension), then `ws[np.argmin(mses)]`.

#### 93. Fitting a line, step 2: **gradient descent** with one number. Start at `w = 0`. Repeat 100 times: compute the slope of the error, `grad = 2 * ((w * x - y) * x).mean()`, and move `w` a small step DOWNHILL: `w = w - 0.01 * grad`. Print `w` every 20 steps. (★★★)
```python
import numpy as np
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])
```

`hint:` Use `for step in range(100):` and update `w` inside the loop. `if step % 20 == 0: print(...)`. The 0.01 is the **learning rate**: the size of each step.

#### 94. Fitting a line, step 3: gradient descent with TWO numbers, slope `w` and intercept `b`, for `y = w * x + b` on simulated study-hours data. Compare your answer with `np.polyfit(x, y, 1)`. (★★★)
```python
import numpy as np
rng = np.random.default_rng(42)
x = rng.uniform(0, 10, size=50)                  # hours of study per week
y = 3.0 * x + 20 + rng.normal(0, 4, size=50)     # marks, with some noise
```

`hint:` Error = `pred - y` with `pred = w * x + b`. Gradients: `grad_w = 2 * (error * x).mean()`, `grad_b = 2 * error.mean()`. Update both each step. Learning rate 0.01, about 5,000 steps. `np.polyfit(x, y, 1)` returns `[slope, intercept]`.

#### 95. **Spot the bug / why is this misleading?** Someone min-max scales the training and test amounts SEPARATELY, each with its own min and max. Show why that is wrong: the same amount (100 EUR) ends up with different scaled values. Then fix it using only the training min and max for both. (★★★)
```python
import numpy as np
train = np.array([10.0, 50.0, 100.0, 400.0])
test = np.array([100.0, 30.0, 150.0])
```

`hint:` Scale both with `(x - train.min()) / (train.max() - train.min())`. Test values may then fall outside 0..1, and that is fine. Learning anything (min, max, mean) from the test set is **data leakage**.

#### 96. **Logistic prediction** by hand. A (made-up) fraud model gives each transaction a score `s = w @ features + b`. The **sigmoid** function `1 / (1 + e^(-s))` turns any score into a probability between 0 and 1. Compute the fraud probability for each transaction and flag those above 0.5. (★★★)
```python
import numpy as np
# features per row: [amount in hundreds of EUR, is_night (0/1), is_foreign (0/1)]
X = np.array([[0.3, 0, 0],
              [5.0, 1, 1],
              [1.2, 0, 1],
              [0.8, 1, 0],
              [9.0, 0, 0]])
w = np.array([0.6, 1.5, 2.0])
b = -4.0
```

`hint:` `s = X @ w + b` gives one score per row (exercise 66). Then `p = 1 / (1 + np.exp(-s))`. `np.exp` is e to the power of each value.

#### 97. **Cosine similarity**: each customer's spending is a vector of EUR per category [groceries, travel, electronics, restaurants]. Find the customer whose spending PATTERN is most similar to customer 0. Cosine similarity = `a @ b / (norm(a) * norm(b))`; 1 means same direction (same pattern), 0 means nothing in common. (★★★)
```python
import numpy as np
spend = np.array([[300.0,  20.0,  10.0, 120.0],   # customer 0
                  [ 30.0, 900.0, 200.0,  40.0],
                  [600.0,  50.0,  15.0, 230.0],
                  [ 50.0,  10.0, 800.0,  20.0]])
```

`hint:` Compute all at once: `spend @ spend[0]` gives the dot product of every row with customer 0. Divide by `np.linalg.norm(spend, axis=1) * np.linalg.norm(spend[0])`. Ignore customer 0 itself (it is always 1).

#### 98. How sure are we about an average? Use the **bootstrap**: resample the 12 swim times WITH replacement 2,000 times, compute the mean of each resample, and report the 2.5th and 97.5th percentiles of those means (a 95% confidence interval). (★★★)
```python
import numpy as np
times = np.array([29.4, 30.1, 28.7, 31.0, 29.9, 30.5, 29.2, 30.8, 28.9, 31.4, 30.0, 29.6])
```

`hint:` `rng.choice(times, size=(2000, 12), replace=True)` makes 2,000 resamples at once (one per row). Then `.mean(axis=1)` and `np.percentile(means, [2.5, 97.5])`.

#### 99. **Spot the bug.** Someone shuffles the features and the labels before splitting, but the model's results look like random guessing. Find the bug and fix it. (★★★)
```python
import numpy as np
rng = np.random.default_rng(42)
X = np.arange(10).reshape(-1, 1) * 10      # amounts 0, 10, ..., 90
y = (X[:, 0] >= 60).astype(int)            # 1 for big amounts
X_shuffled = rng.permutation(X)
y_shuffled = rng.permutation(y)
print(np.column_stack([X_shuffled[:, 0], y_shuffled]))   # column_stack: amounts and labels side by side
```

`hint:` Two separate `permutation` calls shuffle in two DIFFERENT orders, so the labels no longer belong to their rows. Make ONE `idx = rng.permutation(len(X))` and use it for both (exercise 83).

#### 100. **Mini project.** On the real transactions: (1) split the rows 70/30 into train and test with a seeded permutation; (2) on TRAIN only, compute the 95th percentile of amount and use it as the cut-off; (3) on TEST, flag amounts above that cut-off and print TP, FP, FN, TN, precision and recall; (4) in a comment, say whether you would use this rule at a bank. (★★★)

`hint:` Combine exercises 75 (load), 83 (split), 91 (percentile rule) and 81 (confusion matrix). The cut-off comes from `amounts[train_idx]` only (exercise 95).
