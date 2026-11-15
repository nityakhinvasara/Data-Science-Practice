# NumPy: 100 exercises (hints and answers)

_Generated from `tools/source/numpy.ktx`. Don't edit this file; it gets rebuilt._


## Level 1: Easy

#### 1. Import NumPy with its usual short name `np` and print which version you have. (★☆☆)

`hint:` `import numpy as np`, then print `np.__version__` (two underscores on each side).

```python
import numpy as np  # "np" is the short name everyone uses

print(np.__version__)  # the version number, e.g. 2.3.1
```

#### 2. Turn this Python list of transaction amounts (in EUR) into a NumPy array. Print the array and its `type`. (★☆☆)
```python
amounts_list = [12.5, 40.0, 7.25, 120.0, 3.99]
```

`hint:` `np.array(amounts_list)` turns a list into an array. `type(x)` tells you what kind of object `x` is.

```python
import numpy as np

amounts_list = [12.5, 40.0, 7.25, 120.0, 3.99]
amounts = np.array(amounts_list)  # list -> array

print(amounts)
print(type(amounts))  # <class 'numpy.ndarray'>  ("n-dimensional array")
```

#### 3. Make an array of 10 zeros and print it. (★☆☆)

`hint:` `np.zeros(10)`

```python
import numpy as np

z = np.zeros(10)  # handy as a "starting point" you fill in later
print(z)  # the dots mean these are decimal (float) numbers
```

#### 4. Make an array of 5 ones. Then make a table (2D array) of zeros with 3 rows and 4 columns. Print both. (★☆☆)

`hint:` `np.ones(5)`. For a table, give the shape as a tuple: `np.zeros((3, 4))` (note the double brackets).

```python
import numpy as np

ones = np.ones(5)
table = np.zeros((3, 4))  # (rows, columns) goes inside its own brackets

print(ones)
print(table)
```

#### 5. Every new customer starts with a balance of 25.0 EUR. Make an array that holds the starting balance for 6 customers. (★☆☆)

`hint:` `np.full(how_many, value)` makes an array where every value is the same.

```python
import numpy as np

balances = np.full(6, 25.0)  # 6 values, all 25.0
print(balances)
```

#### 6. Use `np.arange` to make (a) the numbers 0 to 9, and (b) the lane distances 50, 100, 150, ..., 400 (in metres). (★☆☆)

`hint:` `np.arange(start, stop, step)`. The stop value is NOT included, like Python's `range`. So for 400 to appear, stop must be bigger than 400.

```python
import numpy as np

a = np.arange(10)             # 0..9 (stop=10 is not included)
b = np.arange(50, 401, 50)    # stop at 401 so that 400 is included

print(a)
print(b)
```

#### 7. Make 5 numbers spread evenly from 0 to 1, including both ends. (★☆☆)

`hint:` `np.linspace(start, stop, how_many)`. Unlike `arange`, here the stop value IS included and you choose how many numbers you get.

```python
import numpy as np

x = np.linspace(0, 1, 5)  # 0, 0.25, 0.5, 0.75, 1
print(x)
```

#### 8. Here are lap times (seconds) for 3 swimmers (rows) over 4 laps (columns). Print the array's `shape`, `size`, `ndim` and `dtype`. (★☆☆)
```python
import numpy as np
laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])
```

`hint:` These are attributes, so no brackets: `laps.shape`, `laps.size`, `laps.ndim`, `laps.dtype`.

```python
import numpy as np

laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])

print("shape:", laps.shape)  # (3, 4) -> 3 rows, 4 columns
print("size:", laps.size)    # 12 values in total
print("ndim:", laps.ndim)    # 2 dimensions (a table)
print("dtype:", laps.dtype)  # float64 -> decimal numbers
```

#### 9. Make the array `[1, 2, 3]` and print its dtype. Then make a float version of it in two ways: with `dtype=float` when creating it, and with `.astype(float)` on the existing array. (★☆☆)

`hint:` `np.array([1, 2, 3], dtype=float)` or `arr.astype(float)`. `astype` returns a NEW array; it does not change the old one.

```python
import numpy as np

a = np.array([1, 2, 3])
print(a, a.dtype)  # int64 -> whole numbers

b = np.array([1, 2, 3], dtype=float)  # way 1: choose the type when creating
c = a.astype(float)                   # way 2: convert an existing array (makes a copy)
print(b, b.dtype)
print(c, c.dtype)
```

#### 10. A bank adds a fixed fee of 0.35 EUR to every card payment. Add the fee to every amount, then also print the amounts doubled. No loops! (★☆☆)
```python
import numpy as np
amounts = np.array([12.5, 40.0, 7.25, 120.0, 3.99])
```

`hint:` Maths with a single number applies to every element: `amounts + 0.35`, `amounts * 2`.

```python
import numpy as np

amounts = np.array([12.5, 40.0, 7.25, 120.0, 3.99])

with_fee = amounts + 0.35  # 0.35 is added to EVERY element at once
doubled = amounts * 2

print(with_fee)
print(doubled)
```

#### 11. Convert these EUR amounts to Indian rupees, using the rate 1 EUR = 90 INR. Print the INR array. (★☆☆)
```python
import numpy as np
amounts_eur = np.array([12.5, 40.0, 7.25, 120.0, 3.99])
```

`hint:` One multiplication: `amounts_eur * 90`.

```python
import numpy as np

amounts_eur = np.array([12.5, 40.0, 7.25, 120.0, 3.99])
rate = 90  # INR per EUR (a round number for practice; real rates change daily)

amounts_inr = amounts_eur * rate
print(amounts_inr)
```

#### 12. Two swimmers' times (seconds) for the same 4 events are below. Make an array of how much faster swimmer A was in each event (B minus A), and an array of their combined time per event. (★☆☆)
```python
import numpy as np
a = np.array([28.4, 62.1, 135.0, 290.2])
b = np.array([29.0, 61.5, 138.2, 295.0])
```

`hint:` Arrays of the same length combine element by element: `b - a`, `a + b`.

```python
import numpy as np

a = np.array([28.4, 62.1, 135.0, 290.2])
b = np.array([29.0, 61.5, 138.2, 295.0])

gap = b - a       # position 0 with position 0, 1 with 1, ...
combined = a + b

print("B minus A:", gap)  # a negative number means B was faster in that event
print("combined:", combined)
```

#### 13. Why arrays beat lists: multiply the Python list `[1, 2, 3]` by 2, then multiply the array `np.array([1, 2, 3])` by 2. Also square the array with `** 2`. Print all three and notice the difference. (★☆☆)

`hint:` A list times 2 repeats the list. An array times 2 doubles each number.

```python
import numpy as np

lst = [1, 2, 3]
arr = np.array([1, 2, 3])

print(lst * 2)   # [1, 2, 3, 1, 2, 3] -> the list is REPEATED
print(arr * 2)   # [2 4 6] -> each number is doubled (what we usually want)
print(arr ** 2)  # [1 4 9] -> each number squared; a list would give an error here
```

#### 14. Print the first, the third and the last amount. Use a negative index for the last one. (★☆☆)
```python
import numpy as np
amounts = np.array([12.5, 40.0, 7.25, 120.0, 3.99, 56.0])
```

`hint:` Counting starts at 0, so the third element is `amounts[2]`. `amounts[-1]` is the last one.

```python
import numpy as np

amounts = np.array([12.5, 40.0, 7.25, 120.0, 3.99, 56.0])

print(amounts[0])   # first
print(amounts[2])   # third (index 2, because we count from 0)
print(amounts[-1])  # last; -1 means "one from the end"
```

#### 15. Using slicing, print: the first 3 amounts, the last 2 amounts, and every second amount starting from the first. (★☆☆)
```python
import numpy as np
amounts = np.array([12.5, 40.0, 7.25, 120.0, 3.99, 56.0])
```

`hint:` Slices are `start:stop:step`, stop not included. First 3: `[:3]`. Last 2: `[-2:]`. Every second: `[::2]`.

```python
import numpy as np

amounts = np.array([12.5, 40.0, 7.25, 120.0, 3.99, 56.0])

print(amounts[:3])   # positions 0, 1, 2
print(amounts[-2:])  # from 2nd-last to the end
print(amounts[::2])  # step of 2: positions 0, 2, 4
```

#### 16. Reverse the order of this array of swim times. (★☆☆)
```python
import numpy as np
times = np.array([30.1, 29.8, 31.4, 28.9, 30.5])
```

`hint:` A step of -1 walks backwards: `times[::-1]`.

```python
import numpy as np

times = np.array([30.1, 29.8, 31.4, 28.9, 30.5])
print(times[::-1])  # empty start/stop = "whole array", step -1 = backwards
```

#### 17. Using the lap table, print: swimmer 2's time on lap 3 (remember counting starts at 0), all of swimmer 1's laps (the first row), and everyone's time on the last lap (last column). (★☆☆)
```python
import numpy as np
laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])
```

`hint:` 2D indexing is `laps[row, column]`. A `:` means "all". So a whole row is `laps[0, :]` and a whole column is `laps[:, -1]`.

```python
import numpy as np

laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])

print(laps[1, 2])   # swimmer 2 = row 1, lap 3 = column 2 -> 32.0
print(laps[0, :])   # row 0, all columns (laps[0] also works)
print(laps[:, -1])  # all rows, last column
```

#### 18. From the same lap table, cut out the first two swimmers and only their last two laps (a 2x2 block). (★☆☆)
```python
import numpy as np
laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])
```

`hint:` Slice rows and columns at the same time: `laps[:2, -2:]` or `laps[0:2, 2:4]`.

```python
import numpy as np

laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])

block = laps[:2, -2:]  # rows 0-1, columns 2-3
print(block)
print(block.shape)     # (2, 2)
```

#### 19. A payment at position 2 was cancelled: set it to 0. Then the last two payments were also cancelled: set both to 0 in one line. Print the array after each change. (★☆☆)
```python
import numpy as np
amounts = np.array([12.5, 40.0, 7.25, 120.0, 3.99, 56.0])
```

`hint:` Assign to an index or a slice: `amounts[2] = 0`, `amounts[-2:] = 0`.

```python
import numpy as np

amounts = np.array([12.5, 40.0, 7.25, 120.0, 3.99, 56.0])

amounts[2] = 0
print(amounts)

amounts[-2:] = 0  # one number is put into every spot of the slice
print(amounts)
```

#### 20. Make the numbers 0 to 11 with `arange`, then reshape them into a 3x4 table. Then reshape the same numbers into 4 rows and let NumPy work out the number of columns. (★☆☆)

`hint:` `np.arange(12).reshape(3, 4)`. Use `-1` for "work it out for me": `.reshape(4, -1)`. The total (12) must stay the same.

```python
import numpy as np

a = np.arange(12)
print(a.reshape(3, 4))   # 3 rows x 4 columns = 12 values

b = a.reshape(4, -1)     # -1: NumPy computes 12 / 4 = 3 columns
print(b)
print(b.shape)           # (4, 3)
```

#### 21. Flatten the lap table into one long 1D array (all of swimmer 1's laps, then swimmer 2's, ...). How many values does it have? (★☆☆)
```python
import numpy as np
laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])
```

`hint:` `laps.flatten()` gives a 1D copy, row by row. `.size` (or `len`) tells you how many values.

```python
import numpy as np

laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])

flat = laps.flatten()  # row 0, then row 1, then row 2
print(flat)
print(flat.size)       # 12
```

#### 22. Copies vs views. Run the code below and print `amounts` at the end. Why did `amounts` change? Then fix it with `.copy()` so that `amounts` stays the same. (★☆☆)
```python
import numpy as np
amounts = np.array([12.5, 40.0, 7.25, 120.0])
first_two = amounts[:2]
first_two[0] = 999
```

`hint:` A slice is a **view**: a window onto the SAME data, not a new array. `amounts[:2].copy()` makes an independent copy.

```python
import numpy as np

amounts = np.array([12.5, 40.0, 7.25, 120.0])
first_two = amounts[:2]   # a VIEW: looks at the same memory as amounts
first_two[0] = 999
print(amounts)            # [999. 40. 7.25 120.] -> the original changed too!

# Fix: take a copy, so changes do not leak back
amounts = np.array([12.5, 40.0, 7.25, 120.0])
first_two = amounts[:2].copy()
first_two[0] = 999
print(amounts)            # unchanged
print(first_two)          # [999. 40.]
```

#### 23. Create a random number generator with seed 42 and roll a dice 10 times (whole numbers 1 to 6). (★☆☆)

`hint:` `rng = np.random.default_rng(42)`, then `rng.integers(1, 7, size=10)`. The upper value 7 is NOT included, so you get 1..6.

```python
import numpy as np

rng = np.random.default_rng(42)  # seed 42 -> the same "random" numbers every run
rolls = rng.integers(1, 7, size=10)  # 7 is excluded, so values are 1..6
print(rolls)
```

#### 24. With a seeded generator (seed 42), simulate 8 swim times for the 50 m freestyle, each a decimal number between 26 and 32 seconds. Then simulate 5 transaction amounts from a normal ("bell curve") distribution with mean 50 and standard deviation 15. (★☆☆)

`hint:` `rng.uniform(26, 32, size=8)` gives any decimal in that range, all equally likely. `rng.normal(50, 15, size=5)` gives values that cluster around 50.

```python
import numpy as np

rng = np.random.default_rng(42)

times = rng.uniform(26, 32, size=8)        # every value between 26 and 32 equally likely
amounts = rng.normal(50, 15, size=5)       # mostly near 50; about 2/3 within 35..65

print(times)
print(amounts)
```

#### 25. A student's daily spending (EUR) for one week is below. Print the total, the average, the smallest and the largest day. (★☆☆)
```python
import numpy as np
spend = np.array([14.2, 3.5, 22.0, 8.75, 41.3, 5.0, 17.6])
```

`hint:` `spend.sum()`, `spend.mean()`, `spend.min()`, `spend.max()`.

```python
import numpy as np

spend = np.array([14.2, 3.5, 22.0, 8.75, 41.3, 5.0, 17.6])

print("total:", spend.sum())
print("average:", spend.mean())
print("smallest:", spend.min())
print("largest:", spend.max())
```

#### 26. Two swimmers have the same average 100 m time, but one is much more consistent. Print the mean, median and standard deviation of each. Which one is more consistent? (★☆☆)
```python
import numpy as np
steady = np.array([62.0, 61.8, 62.3, 62.1, 61.9])
up_down = np.array([58.5, 66.0, 60.1, 64.9, 60.6])
```

`hint:` `x.mean()`, `np.median(x)` (there is no `.median()` method), `x.std()`. Standard deviation = how spread out the values are; smaller = more consistent.

```python
import numpy as np

steady = np.array([62.0, 61.8, 62.3, 62.1, 61.9])
up_down = np.array([58.5, 66.0, 60.1, 64.9, 60.6])

for name, t in [("steady", steady), ("up_down", up_down)]:
    print(name, "mean:", round(t.mean(), 2), "median:", np.median(t), "std:", round(t.std(), 2))
# Same mean (62.02), but 'steady' has a tiny std -> much more consistent.
```

#### 27. Which day had the biggest spend (print its position and the value)? Which day had the smallest? (★☆☆)
```python
import numpy as np
spend = np.array([14.2, 3.5, 22.0, 8.75, 41.3, 5.0, 17.6])
days = np.array(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
```

`hint:` `spend.argmax()` gives the POSITION of the biggest value, not the value. Use that position to index `days` and `spend`.

```python
import numpy as np

spend = np.array([14.2, 3.5, 22.0, 8.75, 41.3, 5.0, 17.6])
days = np.array(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

i = spend.argmax()   # position of the max, here 4
j = spend.argmin()   # position of the min
print("biggest:", i, days[i], spend[i])
print("smallest:", j, days[j], spend[j])
```

#### 28. Make a True/False array showing which amounts are above 100 EUR. (★☆☆)
```python
import numpy as np
amounts = np.array([12.5, 140.0, 7.25, 320.0, 99.99, 100.0, 56.0])
```

`hint:` A comparison on an array, like `amounts > 100`, compares every element and gives a boolean (True/False) array.

```python
import numpy as np

amounts = np.array([12.5, 140.0, 7.25, 320.0, 99.99, 100.0, 56.0])

big = amounts > 100  # one True/False per element. This is called a "mask".
print(big)           # note 100.0 > 100 is False
```

#### 29. Use that mask to keep only the amounts above 100 EUR. (★☆☆)
```python
import numpy as np
amounts = np.array([12.5, 140.0, 7.25, 320.0, 99.99, 100.0, 56.0])
```

`hint:` Put the mask inside square brackets: `amounts[amounts > 100]`.

```python
import numpy as np

amounts = np.array([12.5, 140.0, 7.25, 320.0, 99.99, 100.0, 56.0])

big_ones = amounts[amounts > 100]  # keeps only positions where the mask is True
print(big_ones)
```

#### 30. How MANY amounts are above 100 EUR? (Careful: you want a count of the True values.) (★☆☆)
```python
import numpy as np
amounts = np.array([12.5, 140.0, 7.25, 320.0, 99.99, 100.0, 56.0])
```

`hint:` True counts as 1 and False as 0, so `(amounts > 100).sum()` counts the Trues. `len(amounts > 100)` would wrongly give 7 (the length of the whole mask).

```python
import numpy as np

amounts = np.array([12.5, 140.0, 7.25, 320.0, 99.99, 100.0, 56.0])

mask = amounts > 100
print(mask.sum())   # 2 -> True=1, False=0, so the sum is the number of Trues
print(len(mask))    # 7 -> NOT the answer: that is just how long the mask is
```

#### 31. Find amounts that are between 50 and 200 EUR (inclusive). Then find amounts that are either under 10 or over 300. (★☆☆)
```python
import numpy as np
amounts = np.array([12.5, 140.0, 7.25, 320.0, 99.99, 100.0, 56.0])
```

`hint:` Combine masks with `&` (and) and `|` (or). Each condition needs its own brackets: `(amounts >= 50) & (amounts <= 200)`. Python's `and` / `or` do NOT work on arrays.

```python
import numpy as np

amounts = np.array([12.5, 140.0, 7.25, 320.0, 99.99, 100.0, 56.0])

middle = amounts[(amounts >= 50) & (amounts <= 200)]  # brackets are required!
extreme = amounts[(amounts < 10) | (amounts > 300)]
print(middle)
print(extreme)
```

#### 32. What percentage of these 12 transactions were fraud (1 = fraud, 0 = normal)? Use `.mean()`. (★☆☆)
```python
import numpy as np
is_fraud = np.array([0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0])
```

`hint:` The mean of 0/1 values (or of True/False) is the fraction of 1s. Multiply by 100 for a percentage.

```python
import numpy as np

is_fraud = np.array([0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0])

rate = is_fraud.mean()  # (sum of 1s) / (count) = 2 / 12
print(rate)
print(f"{rate * 100:.1f}% fraud")
```

#### 33. Label every amount as `"big"` if it is over 100 EUR, else `"small"`, in one line. (★☆☆)
```python
import numpy as np
amounts = np.array([12.5, 140.0, 7.25, 320.0, 99.99, 100.0, 56.0])
```

`hint:` `np.where(condition, value_if_true, value_if_false)` works like an if/else on every element.

```python
import numpy as np

amounts = np.array([12.5, 140.0, 7.25, 320.0, 99.99, 100.0, 56.0])

labels = np.where(amounts > 100, "big", "small")  # if/else for each element
print(labels)
```

#### 34. At which positions (indices) are the fraud cases? (★☆☆)
```python
import numpy as np
is_fraud = np.array([0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0])
```

`hint:` `np.where(condition)` with ONLY a condition returns the positions where it is True (inside a tuple, so take `[0]`). `np.flatnonzero(is_fraud == 1)` is another way.

```python
import numpy as np

is_fraud = np.array([0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0])

positions = np.where(is_fraud == 1)[0]  # np.where returns a tuple; [0] takes the array out
print(positions)  # [2 7]
```

#### 35. Negative amounts are refunds. Replace every negative amount with 0, changing the array in place. (★☆☆)
```python
import numpy as np
amounts = np.array([25.0, -10.0, 60.5, -3.2, 14.0])
```

`hint:` Assign through a mask: `amounts[amounts < 0] = 0`.

```python
import numpy as np

amounts = np.array([25.0, -10.0, 60.5, -3.2, 14.0])

amounts[amounts < 0] = 0  # only the positions where the mask is True get 0
print(amounts)
```

#### 36. Sort these 100 m times from fastest to slowest, then from slowest to fastest. (★☆☆)
```python
import numpy as np
times = np.array([64.2, 61.9, 66.5, 60.3, 63.0])
```

`hint:` `np.sort(times)` sorts small to big (fastest first for times). Reverse that with `[::-1]` for the other order.

```python
import numpy as np

times = np.array([64.2, 61.9, 66.5, 60.3, 63.0])

fastest_first = np.sort(times)      # returns a sorted copy
slowest_first = np.sort(times)[::-1]
print(fastest_first)
print(slowest_first)
```

#### 37. Which payment channels appear in this list, and how many times does each appear? (★☆☆)
```python
import numpy as np
channel = np.array(["online", "in_store", "online", "contactless",
                    "online", "in_store", "contactless", "online"])
```

`hint:` `np.unique(channel, return_counts=True)` gives two arrays: the distinct values and how often each appears.

```python
import numpy as np

channel = np.array(["online", "in_store", "online", "contactless",
                    "online", "in_store", "contactless", "online"])

values, counts = np.unique(channel, return_counts=True)  # sorted alphabetically
print(values)
print(counts)
for v, c in zip(values, counts):
    print(v, c)
```

#### 38. Which swimmers swam the 50 m freestyle in under 30 seconds? Print their names. (★☆☆)
```python
import numpy as np
names = np.array(["Asha", "Rohan", "Meera", "Kabir", "Isha", "Dev"])
times = np.array([29.4, 31.2, 28.7, 30.0, 29.9, 32.5])
```

`hint:` Build the mask from one array and use it on the OTHER array: `names[times < 30]`. This works because both arrays are in the same order.

```python
import numpy as np

names = np.array(["Asha", "Rohan", "Meera", "Kabir", "Isha", "Dev"])
times = np.array([29.4, 31.2, 28.7, 30.0, 29.9, 32.5])

fast = times < 30          # mask built from the times
print(names[fast])         # ... used to pick names (same positions)
```

#### 39. Is the average fraud transaction bigger than the average normal one? Print both averages. (★☆☆)
```python
import numpy as np
amounts  = np.array([23.0, 410.0, 15.5, 8.0, 999.0, 42.0, 61.0, 350.0, 12.0, 30.0])
is_fraud = np.array([0,    1,     0,    0,   1,     0,    0,    1,     0,    0])
```

`hint:` `amounts[is_fraud == 1].mean()` and `amounts[is_fraud == 0].mean()`.

```python
import numpy as np

amounts  = np.array([23.0, 410.0, 15.5, 8.0, 999.0, 42.0, 61.0, 350.0, 12.0, 30.0])
is_fraud = np.array([0,    1,     0,    0,   1,     0,    0,    1,     0,    0])

fraud_avg = amounts[is_fraud == 1].mean()
normal_avg = amounts[is_fraud == 0].mean()
print("fraud average:", fraud_avg)
print("normal average:", normal_avg)
# Here fraud payments are much bigger on average: a useful clue for a fraud model.
```

#### 40. The qualifying time for the state meet is 31.0 seconds. Did ANY swimmer qualify? Did ALL of them qualify? (★☆☆)
```python
import numpy as np
times = np.array([29.4, 31.2, 28.7, 30.0, 29.9, 32.5])
```

`hint:` `np.any(mask)` is True if at least one value is True; `np.all(mask)` only if every value is True.

```python
import numpy as np

times = np.array([29.4, 31.2, 28.7, 30.0, 29.9, 32.5])

qualified = times <= 31.0
print("any qualified?", np.any(qualified))  # True
print("all qualified?", np.all(qualified))  # False (31.2 and 32.5 missed)
```


## Level 2: Medium

#### 41. Using the lap table (rows = swimmers, columns = laps), print each swimmer's total time and the average time for each lap. (★★☆)
```python
import numpy as np
laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])
```

`hint:` `axis=1` works ACROSS the columns, giving one result per row: `laps.sum(axis=1)`. `axis=0` works DOWN the rows, giving one result per column: `laps.mean(axis=0)`.

```python
import numpy as np

laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])

per_swimmer = laps.sum(axis=1)  # collapse the columns -> one total per row (3 values)
per_lap = laps.mean(axis=0)     # collapse the rows -> one average per column (4 values)
print("total per swimmer:", per_swimmer)
print("average per lap:", per_lap)
```

#### 42. Which swimmer (row number) had the fastest total time? And for each lap, which swimmer was fastest on that lap? (★★☆)
```python
import numpy as np
laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])
```

`hint:` Fastest = smallest time, so use `argmin`. `laps.sum(axis=1).argmin()` for totals; `laps.argmin(axis=0)` gives one row number per column.

```python
import numpy as np

laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])

best_total = laps.sum(axis=1).argmin()   # row with the smallest total
best_each_lap = laps.argmin(axis=0)      # for every column, the row with the smallest value
print("fastest overall: swimmer row", best_total)
print("fastest per lap:", best_each_lap)  # [1 1 1 1] -> swimmer row 1 won every lap
```

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

```python
import numpy as np

marks = np.array([[40, 72, 60],
                  [35, 88, 70],
                  [48, 65, 52],
                  [30, 91, 77]])
max_marks = np.array([50, 100, 80])

# (4, 3) / (3,) -> the 3 maximums are "stretched" over all 4 rows
pct = marks / max_marks * 100
print(pct)
```

#### 44. For each student (row) subtract that student's own average mark, so you can see which test was above or below their personal average. Use the percentages below. (★★☆)
```python
import numpy as np
pct = np.array([[80.0, 72.0, 75.0],
                [70.0, 88.0, 87.5],
                [96.0, 65.0, 65.0],
                [60.0, 91.0, 96.25]])
```

`hint:` `pct.mean(axis=1)` has shape (4,), which does not line up with (4, 3). Use `pct.mean(axis=1, keepdims=True)` to get shape (4, 1): one value per row that broadcasts across the columns.

```python
import numpy as np

pct = np.array([[80.0, 72.0, 75.0],
                [70.0, 88.0, 87.5],
                [96.0, 65.0, 65.0],
                [60.0, 91.0, 96.25]])

row_avg = pct.mean(axis=1, keepdims=True)  # shape (4, 1) instead of (4,)
print(row_avg.shape)
diff = pct - row_avg                        # (4, 3) - (4, 1): each row minus its own average
print(diff)
# Without keepdims, pct - pct.mean(axis=1) gives an error, because (4, 3) and (4,) do not line up.
```

#### 45. **Min-max normalise** these amounts so the smallest becomes 0 and the biggest becomes 1. (★★☆)
```python
import numpy as np
amounts = np.array([20.0, 35.0, 50.0, 80.0, 220.0])
```

`hint:` Formula: `(x - x.min()) / (x.max() - x.min())`.

```python
import numpy as np

amounts = np.array([20.0, 35.0, 50.0, 80.0, 220.0])

scaled = (amounts - amounts.min()) / (amounts.max() - amounts.min())
print(scaled)  # 0 ... 1. Puts features on the same 0-1 scale for ML models.
```

#### 46. **Standardise** (z-score) the same amounts: subtract the mean, divide by the standard deviation. Check that the result has mean about 0 and standard deviation 1. (★★☆)
```python
import numpy as np
amounts = np.array([20.0, 35.0, 50.0, 80.0, 220.0])
```

`hint:` `z = (x - x.mean()) / x.std()`. A z-score says "how many standard deviations away from the average" a value is. The mean may print as something tiny like `4e-17`: that is just 0 with rounding noise.

```python
import numpy as np

amounts = np.array([20.0, 35.0, 50.0, 80.0, 220.0])

z = (amounts - amounts.mean()) / amounts.std()
print(z)
print("mean:", round(z.mean(), 6), "std:", z.std())  # mean ~0, std 1
# 220 has z ~ 1.9: it is about 1.9 standard deviations above the average.
```

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

```python
import numpy as np

X = np.array([[25.0, 14],
              [310.0, 2],
              [42.0, 19],
              [18.0, 11],
              [95.0, 23]])

means = X.mean(axis=0)  # shape (2,): one mean per column
stds = X.std(axis=0)    # shape (2,)
Z = (X - means) / stds  # (5, 2) with (2,) -> broadcast over rows
print(Z.round(2))
print(Z.mean(axis=0).round(6), Z.std(axis=0))  # each column: mean ~0, std 1
```

#### 48. Join January and February transaction amounts into one array. (★★☆)
```python
import numpy as np
jan = np.array([12.0, 45.5, 8.25])
feb = np.array([60.0, 3.5, 19.0, 77.7])
```

`hint:` `np.concatenate([jan, feb])`. Note the arrays go inside a list (square brackets).

```python
import numpy as np

jan = np.array([12.0, 45.5, 8.25])
feb = np.array([60.0, 3.5, 19.0, 77.7])

both = np.concatenate([jan, feb])  # pass a LIST of arrays
print(both, both.shape)            # 7 values
```

#### 49. A new swimmer joins: add their 4 lap times as a new row of the table. Then add a column of each swimmer's total time on the right. (★★☆)
```python
import numpy as np
laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9]])
new = np.array([30.5, 32.0, 32.8, 31.6])
```

`hint:` `np.vstack([laps, new])` stacks vertically (adds rows). For a new column, the totals must be shape (rows, 1): `totals.reshape(-1, 1)`, then `np.hstack([table, totals])` (stacks horizontally).

```python
import numpy as np

laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9]])
new = np.array([30.5, 32.0, 32.8, 31.6])

table = np.vstack([laps, new])          # now 3 rows
totals = table.sum(axis=1)              # shape (3,)
table2 = np.hstack([table, totals.reshape(-1, 1)])  # (3, 4) next to (3, 1) -> (3, 5)
print(table)
print(table2)
```

#### 50. Two swimmers were disqualified, so their times are missing (`np.nan` means "Not a Number", NumPy's marker for a missing value). Print the plain `.mean()` and see what happens. Then count how many values are missing. (★★☆)
```python
import numpy as np
times = np.array([29.4, np.nan, 28.7, 30.0, np.nan, 32.5])
```

`hint:` Any maths with NaN gives NaN. You cannot test for NaN with `== np.nan` (it is always False); use `np.isnan(times)`, then `.sum()` to count.

```python
import numpy as np

times = np.array([29.4, np.nan, 28.7, 30.0, np.nan, 32.5])

print(times.mean())             # nan -> one missing value "poisons" the result
print(times == np.nan)          # all False! NaN is not equal even to itself
missing = np.isnan(times)       # the correct test
print(missing, missing.sum())   # 2 missing
```

#### 51. Now get the average and fastest time while ignoring the missing values, in two ways: (a) with NaN-aware functions, (b) by dropping the NaNs with a mask first. (★★☆)
```python
import numpy as np
times = np.array([29.4, np.nan, 28.7, 30.0, np.nan, 32.5])
```

`hint:` (a) `np.nanmean(times)`, `np.nanmin(times)`. (b) `times[~np.isnan(times)]` keeps the non-missing values; `~` flips True and False.

```python
import numpy as np

times = np.array([29.4, np.nan, 28.7, 30.0, np.nan, 32.5])

print(np.nanmean(times), np.nanmin(times))   # (a) skip NaNs automatically

clean = times[~np.isnan(times)]              # (b) ~ means "not": keep values that are NOT NaN
print(clean)
print(clean.mean(), clean.min())             # same answers
```

#### 52. Some sensor readings are missing in this feature table. Fill each missing value with the mean of ITS column (ignoring NaNs). (★★☆)
```python
import numpy as np
X = np.array([[1.0, 200.0, 3.0],
              [np.nan, 180.0, 5.0],
              [4.0, np.nan, 4.0],
              [3.0, 220.0, np.nan]])
```

`hint:` `col_means = np.nanmean(X, axis=0)` gives shape (3,). Then `np.where(np.isnan(X), col_means, X)`: where X is missing take the column mean (broadcast over rows), otherwise keep X.

```python
import numpy as np

X = np.array([[1.0, 200.0, 3.0],
              [np.nan, 180.0, 5.0],
              [4.0, np.nan, 4.0],
              [3.0, 220.0, np.nan]])

col_means = np.nanmean(X, axis=0)  # mean of each column, skipping NaNs
print(col_means)
filled = np.where(np.isnan(X), col_means, X)  # col_means is broadcast to every row
print(filled)
```

#### 53. Pick out transactions number 0, 3 and 5 in one go. Then, from the lap table, pick rows 2 and 0 (in that order). (★★☆)
```python
import numpy as np
amounts = np.array([12.5, 140.0, 7.25, 320.0, 99.99, 100.0, 56.0])
laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])
```

`hint:` **Fancy indexing**: index with a LIST of positions, e.g. `amounts[[0, 3, 5]]` (double brackets: the inner ones make the list). `laps[[2, 0]]` picks whole rows.

```python
import numpy as np

amounts = np.array([12.5, 140.0, 7.25, 320.0, 99.99, 100.0, 56.0])
laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])

print(amounts[[0, 3, 5]])  # the list [0, 3, 5] is the index
print(laps[[2, 0]])        # row 2 first, then row 0. Fancy indexing always makes a COPY.
```

#### 54. Print the swimmers' names in finishing order (fastest first). (★★☆)
```python
import numpy as np
names = np.array(["Asha", "Rohan", "Meera", "Kabir", "Isha", "Dev"])
times = np.array([29.4, 31.2, 28.7, 30.0, 29.9, 32.5])
```

`hint:` `np.argsort(times)` returns the POSITIONS that would sort `times`. Use those positions to index `names`.

```python
import numpy as np

names = np.array(["Asha", "Rohan", "Meera", "Kabir", "Isha", "Dev"])
times = np.array([29.4, 31.2, 28.7, 30.0, 29.9, 32.5])

order = np.argsort(times)  # [2 0 4 3 1 5]: Meera (pos 2) is fastest, then Asha (pos 0)...
print(order)
print(names[order])
print(times[order])
```

#### 55. Find the 3 biggest transactions: print their positions and amounts, biggest first. (★★☆)
```python
import numpy as np
amounts = np.array([12.5, 140.0, 7.25, 320.0, 99.99, 100.0, 56.0, 870.0])
```

`hint:` `np.argsort(amounts)[::-1]` gives positions from biggest to smallest; then take the first 3 with `[:3]`.

```python
import numpy as np

amounts = np.array([12.5, 140.0, 7.25, 320.0, 99.99, 100.0, 56.0, 870.0])

top3 = np.argsort(amounts)[::-1][:3]  # sort positions ascending, reverse, keep 3
print(top3)            # [7 3 1]
print(amounts[top3])   # [870. 320. 140.]
```

#### 56. A student starts the month with 0 EUR. Below are money in (+) and out (-) each day. Print the balance after each day. (★★☆)
```python
import numpy as np
flows = np.array([500.0, -45.0, -12.5, -200.0, 150.0, -80.0])
```

`hint:` `np.cumsum(flows)` gives a running total: first value, first+second, first+second+third, ...

```python
import numpy as np

flows = np.array([500.0, -45.0, -12.5, -200.0, 150.0, -80.0])

balance = np.cumsum(flows)  # running total
print(balance)  # [500. 455. 442.5 242.5 392.5 312.5]
```

#### 57. A 200 m race gives **split times**: the clock reading at 50, 100, 150 and 200 m. Work out how long each 50 m lap took. Which lap was slowest? (★★☆)
```python
import numpy as np
splits = np.array([30.1, 63.0, 96.8, 129.4])
```

`hint:` `np.diff(x)` gives the differences between neighbours (x[1]-x[0], x[2]-x[1], ...). It returns one fewer value, so add the first lap back: `np.diff(splits, prepend=0)`.

```python
import numpy as np

splits = np.array([30.1, 63.0, 96.8, 129.4])

lap_times = np.diff(splits, prepend=0)  # prepend=0 so lap 1 = 30.1 - 0
print(lap_times)                       # [30.1 32.9 33.8 32.6]
print("slowest lap:", lap_times.argmax() + 1)  # +1 to count laps from 1 -> lap 3
```

#### 58. Print the 25th, 50th, 75th and 95th percentiles of these amounts, and the **interquartile range** (IQR = 75th minus 25th percentile). (★★☆)
```python
import numpy as np
rng = np.random.default_rng(42)
amounts = rng.exponential(scale=40, size=1000)
```

`hint:` `np.percentile(amounts, [25, 50, 75, 95])` returns all four at once. The p-th percentile is the value below which p% of the data falls.

```python
import numpy as np

rng = np.random.default_rng(42)
amounts = rng.exponential(scale=40, size=1000)  # many small payments, a few big ones

p25, p50, p75, p95 = np.percentile(amounts, [25, 50, 75, 95])
print("25th:", round(p25, 2), "median:", round(p50, 2), "75th:", round(p75, 2), "95th:", round(p95, 2))
print("IQR:", round(p75 - p25, 2))  # the spread of the middle half of the data
```

#### 59. A few huge amounts can distort a chart or a model. Cap all amounts at 500 EUR (anything above becomes 500) and raise anything below 1 EUR to 1. (★★☆)
```python
import numpy as np
amounts = np.array([0.2, 45.0, 1200.0, 18.0, 640.0, 3.0])
```

`hint:` `np.clip(amounts, 1, 500)` squeezes every value into the range 1..500.

```python
import numpy as np

amounts = np.array([0.2, 45.0, 1200.0, 18.0, 640.0, 3.0])

capped = np.clip(amounts, 1, 500)  # below 1 -> 1, above 500 -> 500, else unchanged
print(capped)
```

#### 60. Convert to INR at 90.37 INR per EUR and round to 2 decimals. Also print the EUR amounts rounded down and rounded up to whole euros. (★★☆)
```python
import numpy as np
amounts = np.array([12.345, 40.5, 7.999, 120.01])
```

`hint:` `np.round(x, 2)` rounds to 2 decimals. `np.floor(x)` always rounds down, `np.ceil(x)` always rounds up.

```python
import numpy as np

amounts = np.array([12.345, 40.5, 7.999, 120.01])

inr = np.round(amounts * 90.37, 2)
print(inr)
print(np.floor(amounts))  # [12. 40. 7. 120.] -> down
print(np.ceil(amounts))   # [13. 41. 8. 121.] -> up
```

#### 61. Put every amount into a size band: under 20 -> "small", 20 to under 100 -> "medium", 100 to under 500 -> "large", 500 or more -> "huge". (★★☆)
```python
import numpy as np
amounts = np.array([5.0, 25.0, 99.0, 100.0, 480.0, 1500.0, 19.99])
```

`hint:` `np.select(list_of_conditions, list_of_choices, default=...)`: the FIRST condition that is True decides the label. Order the conditions from smallest to biggest.

```python
import numpy as np

amounts = np.array([5.0, 25.0, 99.0, 100.0, 480.0, 1500.0, 19.99])

conditions = [amounts < 20, amounts < 100, amounts < 500]
choices = ["small", "medium", "large"]
bands = np.select(conditions, choices, default="huge")  # nothing matched -> "huge"
print(bands)
# 25.0 is also < 500, but "amounts < 100" comes first, so it is "medium".
```

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

```python
import numpy as np

amounts = np.array([45.0, 150.0, 99.0, 1200.0, 20.0])

# the loop version
fees = []
for a in amounts:
    if a > 100:
        fees.append(a * 0.015)
    else:
        fees.append(1.0)
fees = np.array(fees)

# the vectorised version: one line, no loop
fees_vec = np.where(amounts > 100, amounts * 0.015, 1.0)
print(fees_vec)
print(np.allclose(fees, fees_vec))  # True
```

#### 63. How much faster is NumPy? Make the numbers 0 to 999,999. Compute the sum of their squares (a) with a Python loop over a list and (b) with NumPy. Time both with `time.perf_counter()`. (★★☆)

`hint:` `start = time.perf_counter()` before, `time.perf_counter() - start` after. For NumPy: `(x ** 2).sum()`. Use `dtype=np.int64` so the big total fits.

```python
import time
import numpy as np

n = 1_000_000

start = time.perf_counter()
total = 0
for i in range(n):          # Python handles one number at a time
    total += i * i
loop_secs = time.perf_counter() - start

x = np.arange(n, dtype=np.int64)
start = time.perf_counter()
total_np = (x ** 2).sum()   # the loop runs inside NumPy's fast compiled code
np_secs = time.perf_counter() - start

print(total, total_np, total == total_np)
print(f"loop: {loop_secs:.4f}s, numpy: {np_secs:.4f}s, about {loop_secs / np_secs:.0f}x faster")
```

#### 64. For each swimmer (row), find which lap was their fastest AND what that time was, without a loop. (★★☆)
```python
import numpy as np
laps = np.array([[31.2, 33.0, 30.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 33.2, 35.9, 34.4]])
```

`hint:` `best = laps.argmin(axis=1)` gives one column number per row. Pair it with the row numbers `np.arange(3)` and fancy-index: `laps[np.arange(3), best]`.

```python
import numpy as np

laps = np.array([[31.2, 33.0, 30.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 33.2, 35.9, 34.4]])

best_lap = laps.argmin(axis=1)          # [2 0 1]: a column for each row
rows = np.arange(laps.shape[0])         # [0 1 2]
best_time = laps[rows, best_lap]        # picks (0,2), (1,0), (2,1)
print("best lap (from 1):", best_lap + 1)
print("best time:", best_time)
# laps.min(axis=1) gives the same times, but argmin also tells you WHICH lap.
```

#### 65. A shopping basket: prices (EUR) and how many of each item. Compute the total bill with a **dot product**. (★★☆)
```python
import numpy as np
prices = np.array([2.5, 0.99, 4.2, 12.0])
qty = np.array([3, 6, 1, 2])
```

`hint:` The dot product multiplies matching elements and adds them up: `prices @ qty` or `np.dot(prices, qty)`. Same as `(prices * qty).sum()`.

```python
import numpy as np

prices = np.array([2.5, 0.99, 4.2, 12.0])
qty = np.array([3, 6, 1, 2])

print((prices * qty).sum())  # multiply pairs, then add: the long way
print(prices @ qty)          # dot product: the same thing in one step
print(np.dot(prices, qty))   # another way to write it
```

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

```python
import numpy as np

scores = np.array([[80, 70, 65],
                   [92, 85, 78],
                   [55, 60, 72],
                   [70, 95, 88]])
weights = np.array([0.2, 0.3, 0.5])

final = scores @ weights   # row 0: 80*0.2 + 70*0.3 + 65*0.5 = 69.5
print(final)
```

#### 67. **Transpose** the lap table so rows become laps and columns become swimmers. Print the shape before and after. (★★☆)
```python
import numpy as np
laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])
```

`hint:` `laps.T` flips rows and columns.

```python
import numpy as np

laps = np.array([[31.2, 33.0, 33.4, 32.1],
                 [29.8, 31.5, 32.0, 30.9],
                 [34.0, 35.2, 35.9, 34.4]])

print(laps.shape)    # (3, 4)
print(laps.T)
print(laps.T.shape)  # (4, 3): row i of laps.T is column i of laps
```

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

```python
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[1, 0],
              [0, 1],
              [2, 2]])

C = A @ B          # (2, 3) @ (3, 2) -> (2, 2)
print(C)           # C[0, 0] = row 0 of A dotted with column 0 of B = 1*1 + 2*0 + 3*2 = 7
print(C.shape)

try:
    A @ A          # (2, 3) @ (2, 3): inner sizes 3 and 2 do not match
except ValueError as e:
    print("Error:", e)
# A @ A.T would work: (2, 3) @ (3, 2) -> (2, 2)
```

#### 69. Make a 3x3 **identity matrix** (1s on the diagonal, 0s elsewhere). Show that multiplying a matrix by it changes nothing. (★★☆)
```python
import numpy as np
M = np.array([[2, 7, 1],
              [0, 3, 5],
              [4, 4, 9]])
```

`hint:` `np.eye(3)`. Then compare with `np.array_equal(M @ I, M)`. The identity matrix is the "multiply by 1" of matrices.

```python
import numpy as np

M = np.array([[2, 7, 1],
              [0, 3, 5],
              [4, 4, 9]])

I = np.eye(3)
print(I)
print(M @ I)
print(np.array_equal(M @ I, M))  # True: like multiplying a number by 1
```

#### 70. Compute the straight-line (**Euclidean**) distance between two points, first with the formula and then with `np.linalg.norm`. (★★☆)
```python
import numpy as np
p = np.array([1.0, 2.0])
q = np.array([4.0, 6.0])
```

`hint:` Formula: square root of the sum of squared differences, `np.sqrt(((p - q) ** 2).sum())`. `np.linalg.norm(p - q)` does the same.

```python
import numpy as np

p = np.array([1.0, 2.0])
q = np.array([4.0, 6.0])

d1 = np.sqrt(((p - q) ** 2).sum())  # sqrt(3^2 + 4^2) = sqrt(25) = 5 (Pythagoras)
d2 = np.linalg.norm(p - q)
print(d1, d2)
```

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

```python
import numpy as np

customer = np.array([2.0, 3.0])
atms = np.array([[0.0, 0.0],
                 [5.0, 4.0],
                 [2.5, 2.0],
                 [1.0, 7.0],
                 [3.0, 3.5]])

diffs = atms - customer                       # each ATM minus the customer, shape (5, 2)
dists = np.sqrt((diffs ** 2).sum(axis=1))     # one distance per ATM
print(dists.round(3))
print("nearest ATM:", dists.argmin(), "at", atms[dists.argmin()])
```

#### 72. Make the full **distance matrix** for 4 points: entry [i, j] is the distance between point i and point j. (★★☆)
```python
import numpy as np
pts = np.array([[0.0, 0.0],
                [3.0, 4.0],
                [6.0, 0.0],
                [3.0, 1.0]])
```

`hint:` Add a new axis so broadcasting pairs every point with every point: `pts[:, None, :] - pts[None, :, :]` has shape (4, 4, 2). Then norm over the last axis: `np.linalg.norm(..., axis=2)`.

```python
import numpy as np

pts = np.array([[0.0, 0.0],
                [3.0, 4.0],
                [6.0, 0.0],
                [3.0, 1.0]])

# (4, 1, 2) - (1, 4, 2) -> (4, 4, 2): every point minus every other point
diff = pts[:, None, :] - pts[None, :, :]
D = np.linalg.norm(diff, axis=2)  # length of each difference -> (4, 4)
print(D.round(2))
# The diagonal is 0 (distance from a point to itself) and D is symmetric: D[i, j] == D[j, i].
```

#### 73. Solve two equations with NumPy. At a swim meet, 2 adult tickets and 3 child tickets cost 31 EUR; 1 adult and 4 child tickets cost 28 EUR. What does each ticket cost? (★★☆)

`hint:` Write it as a matrix `A` (the numbers of tickets) times unknown prices `x` = totals `b`: `A = [[2, 3], [1, 4]]`, `b = [31, 28]`. Then `np.linalg.solve(A, b)`.

```python
import numpy as np

# 2*adult + 3*child = 31
# 1*adult + 4*child = 28
A = np.array([[2.0, 3.0],
              [1.0, 4.0]])
b = np.array([31.0, 28.0])

x = np.linalg.solve(A, b)  # finds x so that A @ x == b
print("adult:", x[0], "child:", x[1])  # 8.0 and 5.0
print(A @ x)               # check: [31. 28.]
```

#### 74. Save an array of simulated amounts to `outputs/amounts.npy`, load it back, and check that it is identical. (★★☆)
```python
import numpy as np
rng = np.random.default_rng(42)
amounts = rng.normal(60, 20, size=100).round(2)
```

`hint:` `os.makedirs("outputs", exist_ok=True)` creates the folder. Then `np.save(path, array)` and `np.load(path)`. Compare with `np.array_equal`.

```python
import os
import numpy as np

rng = np.random.default_rng(42)
amounts = rng.normal(60, 20, size=100).round(2)

os.makedirs("outputs", exist_ok=True)       # make the folder if it is not there
np.save("outputs/amounts.npy", amounts)     # .npy = NumPy's own fast file format
loaded = np.load("outputs/amounts.npy")
print(loaded[:5])
print(np.array_equal(amounts, loaded))      # True
```

#### 75. Load the real data: read the `amount_eur` and `is_fraud` columns of `../data/transactions.csv` (columns 6 and 7, counting from 0) into NumPy. Print the number of rows, the average amount and the fraud rate. (★★☆)

`hint:` `np.loadtxt("../data/transactions.csv", delimiter=",", skiprows=1, usecols=(6, 7))`. `skiprows=1` skips the header line. You get a 2D array: column 0 = amount, column 1 = is_fraud.

```python
import numpy as np

data = np.loadtxt("../data/transactions.csv", delimiter=",", skiprows=1, usecols=(6, 7))
amounts = data[:, 0]
is_fraud = data[:, 1]

print("rows:", data.shape[0])
print("average amount:", round(amounts.mean(), 2), "EUR")
print("fraud rate:", round(is_fraud.mean() * 100, 2), "%")
```


## Level 3: Hard

#### 76. **One-hot encoding** by hand. Payment channels are stored as codes: 0 = in_store, 1 = online, 2 = contactless. Turn them into a table with one column per channel, holding 1 where that row has that channel and 0 elsewhere. (★★★)
```python
import numpy as np
codes = np.array([1, 0, 2, 1, 1, 0])
```

`hint:` Each row of `np.eye(3)` is already a one-hot row (row 1 is `[0, 1, 0]`). So fancy-index it with the codes: `np.eye(3)[codes]`.

```python
import numpy as np

codes = np.array([1, 0, 2, 1, 1, 0])

one_hot = np.eye(3, dtype=int)[codes]  # pick row "code" of the identity matrix for each value
print(one_hot)
# Why: ML models need numbers, but "online = 1, contactless = 2" would wrongly suggest
# contactless is "twice" online. One-hot gives each channel its own 0/1 column instead.
print(one_hot.sum(axis=0))  # column totals = how often each channel appears
```

#### 77. One-hot encode the channel NAMES directly (strings). First turn the names into codes 0, 1, 2 with `np.unique`, then one-hot encode as before. Print the column names too. (★★★)
```python
import numpy as np
channel = np.array(["online", "in_store", "online", "contactless", "in_store"])
```

`hint:` `names, codes = np.unique(channel, return_inverse=True)`. `codes` says, for each row, the position of its value in `names`. Then `np.eye(len(names), dtype=int)[codes]`.

```python
import numpy as np

channel = np.array(["online", "in_store", "online", "contactless", "in_store"])

names, codes = np.unique(channel, return_inverse=True)
print(names)   # ['contactless' 'in_store' 'online'] (alphabetical)
print(codes)   # [2 1 2 0 1] -> "online" is names[2], etc.

one_hot = np.eye(len(names), dtype=int)[codes]
print(one_hot)
```

#### 78. Compute the 3-day **moving average** of daily spending (the average of each day and the two days before it). Use `np.convolve`. (★★★)
```python
import numpy as np
spend = np.array([20.0, 35.0, 5.0, 50.0, 10.0, 40.0, 25.0])
```

`hint:` `np.convolve(spend, np.ones(3) / 3, mode="valid")` slides a window of 3 weights (each 1/3) along the data and sums: that is the average of 3 neighbours. `mode="valid"` keeps only full windows, so you get 7 - 3 + 1 = 5 values.

```python
import numpy as np

spend = np.array([20.0, 35.0, 5.0, 50.0, 10.0, 40.0, 25.0])

window = np.ones(3) / 3                           # [1/3, 1/3, 1/3]
moving = np.convolve(spend, window, mode="valid")  # only places where all 3 days exist
print(moving.round(2))                            # first value = (20 + 35 + 5) / 3 = 20.0

# Check the first two by hand
print(spend[0:3].mean(), spend[1:4].mean())
```

#### 79. **Outlier detection** on the real transactions: compute the z-score of every amount and flag those with z > 3. How many are flagged? What is the fraud rate among flagged transactions compared with all transactions? (★★★)

`hint:` Load as in exercise 75. `z = (amounts - amounts.mean()) / amounts.std()`, `flag = z > 3`. Fraud rate in the flagged group: `is_fraud[flag].mean()`.

```python
import numpy as np

data = np.loadtxt("../data/transactions.csv", delimiter=",", skiprows=1, usecols=(6, 7))
amounts, is_fraud = data[:, 0], data[:, 1]

z = (amounts - amounts.mean()) / amounts.std()
flag = z > 3   # more than 3 standard deviations above average (only "too big" matters here)

print("flagged:", flag.sum(), "of", len(amounts))
print("fraud rate, flagged:", round(is_fraud[flag].mean() * 100, 1), "%")
print("fraud rate, all:    ", round(is_fraud.mean() * 100, 1), "%")
# Big outliers are far more likely to be fraud, but many frauds are NOT outliers:
print("share of all frauds caught:", round(is_fraud[flag].sum() / is_fraud.sum() * 100, 1), "%")
```

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

```python
import numpy as np

# BUG: amounts[:7] is a VIEW of the caller's array, and "/=" edits in place,
# so the caller's data is overwritten. Nothing crashes: the data is silently wrong.

def scale_first_week_fixed(amounts):
    week = amounts[:7].copy()   # fix 1: work on a copy
    week = week / week.max()    # fix 2 (either is enough): "x = x / y" makes a NEW array
    return week

raw = np.array([20.0, 50.0, 10.0, 40.0, 80.0, 30.0, 60.0, 90.0, 15.0])
scaled = scale_first_week_fixed(raw)
print(raw)     # unchanged
print(scaled.round(3))
```

#### 81. A fraud model made predictions (1 = fraud). Count the four cells of the **confusion matrix**: TP (true positive: predicted 1, really 1), FP (predicted 1, really 0), FN (predicted 0, really 1), TN (predicted 0, really 0). Then compute accuracy, precision and recall. (★★★)
```python
import numpy as np
y_true = np.array([0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0])
y_pred = np.array([0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0])
```

`hint:` Combine masks: `TP = ((y_pred == 1) & (y_true == 1)).sum()`, and so on. Accuracy = (TP + TN) / total. Precision = TP / (TP + FP): "of the alarms, how many were real?". Recall = TP / (TP + FN): "of the real frauds, how many did we catch?".

```python
import numpy as np

y_true = np.array([0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0])
y_pred = np.array([0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0])

TP = ((y_pred == 1) & (y_true == 1)).sum()
FP = ((y_pred == 1) & (y_true == 0)).sum()
FN = ((y_pred == 0) & (y_true == 1)).sum()
TN = ((y_pred == 0) & (y_true == 0)).sum()
print("TP", TP, "FP", FP, "FN", FN, "TN", TN)

accuracy = (TP + TN) / len(y_true)
precision = TP / (TP + FP)   # of the alarms raised, the share that were real fraud
recall = TP / (TP + FN)      # of the real frauds, the share we caught
print(f"accuracy {accuracy:.2f}, precision {precision:.2f}, recall {recall:.2f}")
```

#### 82. **Why is this misleading?** A colleague says: "My fraud model is 98% accurate on our transactions!" Their "model" predicts 0 (not fraud) for every transaction. Compute its accuracy and recall on the real data and explain in a comment why accuracy is the wrong number to report here. (★★★)

`hint:` Load `is_fraud` as in exercise 75. `y_pred = np.zeros_like(y_true)`. Accuracy = `(y_pred == y_true).mean()`. Recall = caught frauds / all frauds.

```python
import numpy as np

y_true = np.loadtxt("../data/transactions.csv", delimiter=",", skiprows=1, usecols=7)
y_pred = np.zeros_like(y_true)   # "nothing is ever fraud"

accuracy = (y_pred == y_true).mean()
recall = ((y_pred == 1) & (y_true == 1)).sum() / (y_true == 1).sum()
print(f"accuracy: {accuracy:.3f}")  # about 0.98
print(f"recall:   {recall:.3f}")    # 0.0 -> catches no fraud at all

# Fraud is only ~2% of transactions, so "always say no" is right 98% of the time.
# With such imbalanced classes, accuracy hides the failure. Report recall and precision
# (or the confusion matrix) and compare with this "always 0" baseline.
```

#### 83. **Train/test split by hand.** Shuffle the 10 rows below with a seeded random permutation, then put the first 80% into a training set and the rest into a test set. Keep `X` and `y` lined up. (★★★)
```python
import numpy as np
X = np.arange(20).reshape(10, 2)   # 10 rows, 2 features
y = np.array([0, 1, 0, 0, 1, 0, 1, 0, 0, 1])
```

`hint:` `idx = rng.permutation(10)` gives the numbers 0..9 in random order. Use the SAME `idx` for X and y: `X[idx]`, `y[idx]`. Then slice: the first 8 for training, the last 2 for testing.

```python
import numpy as np

X = np.arange(20).reshape(10, 2)
y = np.array([0, 1, 0, 0, 1, 0, 1, 0, 0, 1])

rng = np.random.default_rng(42)
idx = rng.permutation(len(X))      # shuffled row numbers
print(idx)

cut = int(0.8 * len(X))            # 8
train_idx, test_idx = idx[:cut], idx[cut:]
X_train, y_train = X[train_idx], y[train_idx]   # same positions for X and y -> rows stay matched
X_test, y_test = X[test_idx], y[test_idx]

print(X_train.shape, X_test.shape)  # (8, 2) (2, 2)
print(X_test, y_test)
```

#### 84. **Spot the bug.** Image pixels are often stored as `uint8` (whole numbers 0 to 255). Someone brightens an image by adding 100, and someone else adds up two big `int8` counts. Run the code, explain the strange results in comments, and fix them. (★★★)
```python
import numpy as np
pixels = np.array([100, 150, 200, 250], dtype=np.uint8)
print(pixels + 100)

counts = np.array([100, 90], dtype=np.int8)   # int8 holds -128..127
print(counts.sum(dtype=np.int8))
```

`hint:` Small integer types **overflow**: past the maximum they wrap around (like a car's odometer going from 999 back to 000). Convert to a bigger type first, e.g. `pixels.astype(np.int64) + 100`, then `np.clip` to 0..255 if needed.

```python
import numpy as np

pixels = np.array([100, 150, 200, 250], dtype=np.uint8)
print(pixels + 100)   # [200 250 44 94] -> 300 wrapped to 300-256 = 44! No error, just wrong.

counts = np.array([100, 90], dtype=np.int8)
print(counts.sum(dtype=np.int8))   # -66, not 190: wrapped past 127

# FIX: move to a bigger type before the maths, then limit the range if it matters
bright = np.clip(pixels.astype(np.int64) + 100, 0, 255).astype(np.uint8)
print(bright)                        # [200 250 255 255]
print(counts.astype(np.int64).sum()) # 190
```

#### 85. **Why is this misleading?** Load the real 50 m swim results (columns `distance_m` and `time_sec`, numbers 7 and 8). Disqualified swims have no time (NaN). A coach replaces the missing times with 0 before averaging. Compare that average with the correct one and explain the difference. (★★★)

`hint:` `np.genfromtxt("../data/swim_results.csv", delimiter=",", skip_header=1, usecols=(7, 8))` turns empty cells into NaN (`loadtxt` would crash on them). Keep rows where distance == 50, then compare `np.nan_to_num(t).mean()` (NaN -> 0) with `np.nanmean(t)`.

```python
import numpy as np

data = np.genfromtxt("../data/swim_results.csv", delimiter=",", skip_header=1, usecols=(7, 8))
t = data[data[:, 0] == 50, 1]   # times of 50 m races only

print("races:", len(t), "missing:", np.isnan(t).sum())
wrong = np.nan_to_num(t).mean()   # NaN replaced by 0 seconds
right = np.nanmean(t)             # missing values skipped
print("NaN as 0:", round(wrong, 2), "s")
print("correct: ", round(right, 2), "s")

# A DQ is "no time", not "0 seconds". Counting it as 0 drags the average down,
# so the squad looks faster than it is. Always decide on purpose what a missing value means.
```

#### 86. **Nearest neighbour** by hand. Each row of `X_train` is a past transaction: (amount in hundreds of EUR, hour / 24). `y_train` says if it was fraud. Classify the new transaction by copying the label of the closest past transaction. (★★★)
```python
import numpy as np
X_train = np.array([[0.2, 0.50], [0.4, 0.60], [3.5, 0.10],
                    [0.3, 0.45], [4.0, 0.05], [0.1, 0.70]])
y_train = np.array([0, 0, 1, 0, 1, 0])
new = np.array([3.2, 0.12])
```

`hint:` Distances from `new` to every row, as in exercise 71: `np.linalg.norm(X_train - new, axis=1)`. The prediction is `y_train[dists.argmin()]`.

```python
import numpy as np

X_train = np.array([[0.2, 0.50], [0.4, 0.60], [3.5, 0.10],
                    [0.3, 0.45], [4.0, 0.05], [0.1, 0.70]])
y_train = np.array([0, 0, 1, 0, 1, 0])
new = np.array([3.2, 0.12])

dists = np.linalg.norm(X_train - new, axis=1)  # distance to every past transaction
nearest = dists.argmin()
print(dists.round(3))
print("nearest row:", nearest, "-> predicted label:", y_train[nearest])  # 1 = fraud
```

#### 87. Now use **k = 3 nearest neighbours**: find the 3 closest training points and predict the label that appears most often among them (a majority vote). (★★★)
```python
import numpy as np
X_train = np.array([[1.0, 1.0], [1.5, 2.0], [3.0, 4.0],
                    [5.0, 7.0], [3.5, 5.0], [4.5, 5.0], [3.5, 4.5]])
y_train = np.array([0, 0, 1, 1, 1, 1, 0])
new = np.array([3.0, 3.5])
```

`hint:` `np.argsort(dists)[:3]` gives the positions of the 3 closest. `np.bincount(labels)` counts how many 0s, 1s, ... there are; `.argmax()` of that is the winning label.

```python
import numpy as np

X_train = np.array([[1.0, 1.0], [1.5, 2.0], [3.0, 4.0],
                    [5.0, 7.0], [3.5, 5.0], [4.5, 5.0], [3.5, 4.5]])
y_train = np.array([0, 0, 1, 1, 1, 1, 0])
new = np.array([3.0, 3.5])

dists = np.linalg.norm(X_train - new, axis=1)
k_idx = np.argsort(dists)[:3]          # the 3 closest rows
k_labels = y_train[k_idx]
votes = np.bincount(k_labels)          # votes[0] = number of 0s, votes[1] = number of 1s
print("closest rows:", k_idx, "labels:", k_labels, "votes:", votes)
print("prediction:", votes.argmax())
```

#### 88. Group statistics by hand: compute the total and average amount for each channel code (0, 1, 2) WITHOUT a loop. (★★★)
```python
import numpy as np
codes = np.array([0, 1, 1, 2, 0, 1, 2, 2, 1])
amounts = np.array([20.0, 150.0, 80.0, 12.0, 35.0, 300.0, 8.0, 15.0, 95.0])
```

`hint:` `np.bincount(codes)` counts rows per code. `np.bincount(codes, weights=amounts)` ADDS the amounts per code instead of counting. Average = sums / counts.

```python
import numpy as np

codes = np.array([0, 1, 1, 2, 0, 1, 2, 2, 1])
amounts = np.array([20.0, 150.0, 80.0, 12.0, 35.0, 300.0, 8.0, 15.0, 95.0])

counts = np.bincount(codes)                   # [2 4 3]
sums = np.bincount(codes, weights=amounts)    # amount added up per code
means = sums / counts
print("counts:", counts)
print("totals:", sums)
print("averages:", means.round(2))
# This is what pandas' groupby does for you later; here you see the idea underneath.
```

#### 89. **Spot the bug.** This code tries to standardise student marks in place, but every result comes out as a whole number. Explain why and fix it. (★★★)
```python
import numpy as np
marks = np.array([45, 60, 75, 90, 30])
marks[:] = (marks - marks.mean()) / marks.std()
print(marks)
```

`hint:` `marks` has dtype int64. Writing decimals INTO an int array chops off the decimal part (no warning). Make a new float array instead: `z = (marks - marks.mean()) / marks.std()`.

```python
import numpy as np

marks = np.array([45, 60, 75, 90, 30])
print(marks.dtype)            # int64
bad = marks.copy()
bad[:] = (bad - bad.mean()) / bad.std()
print(bad)                    # [0 0 0 1 -1]: decimals were silently cut off

# FIX: do not write floats into an integer array; create a new (float) array
z = (marks - marks.mean()) / marks.std()
print(z.round(3), z.dtype)    # proper z-scores, float64
# (or convert first: marks = marks.astype(float))
```

#### 90. A model gives each transaction a fraud **score** between 0 and 1. You flag a transaction when its score is at least a threshold. For thresholds 0.3, 0.5 and 0.7, print precision and recall. What happens as the threshold goes up? (★★★)
```python
import numpy as np
scores = np.array([0.05, 0.92, 0.40, 0.65, 0.10, 0.81, 0.33, 0.55, 0.20, 0.75])
y_true = np.array([0,    1,    0,    1,    0,    1,    0,    0,    0,    0])
```

`hint:` Loop over the thresholds. Inside: `y_pred = (scores >= t).astype(int)`, then TP, FP, FN as in exercise 81.

```python
import numpy as np

scores = np.array([0.05, 0.92, 0.40, 0.65, 0.10, 0.81, 0.33, 0.55, 0.20, 0.75])
y_true = np.array([0,    1,    0,    1,    0,    1,    0,    0,    0,    0])

for t in [0.3, 0.5, 0.7]:
    y_pred = (scores >= t).astype(int)
    TP = ((y_pred == 1) & (y_true == 1)).sum()
    FP = ((y_pred == 1) & (y_true == 0)).sum()
    FN = ((y_pred == 0) & (y_true == 1)).sum()
    print(f"threshold {t}: flagged {y_pred.sum()}, precision {TP / (TP + FP):.2f}, recall {TP / (TP + FN):.2f}")
# Higher threshold -> fewer alarms: precision goes up, recall goes down.
# A bank picks the threshold by weighing missed fraud against annoyed customers.
```

#### 91. A simple rule on the real data: flag every transaction above the 95th percentile of amount. Print how many are flagged, the precision and the recall of this rule. (★★★)

`hint:` Load as in exercise 75. `cut = np.percentile(amounts, 95)`, `y_pred = amounts > cut`. Then precision and recall as in exercise 81.

```python
import numpy as np

data = np.loadtxt("../data/transactions.csv", delimiter=",", skiprows=1, usecols=(6, 7))
amounts, y_true = data[:, 0], data[:, 1]

cut = np.percentile(amounts, 95)
y_pred = amounts > cut
TP = (y_pred & (y_true == 1)).sum()
FP = (y_pred & (y_true == 0)).sum()
FN = (~y_pred & (y_true == 1)).sum()

print(f"cut-off: {cut:.2f} EUR, flagged: {y_pred.sum()}")
print(f"precision: {TP / (TP + FP):.2f}  (baseline fraud rate is {y_true.mean():.2f})")
print(f"recall:    {TP / (TP + FN):.2f}")
# Much better precision than random flagging, but it misses the many small frauds.
```

#### 92. Fitting a line, step 1: the **mean squared error** (MSE). For the data below we guess the line `y = w * x`. Try every `w` from 0 to 4 in steps of 0.1, compute the MSE for each, and print the `w` with the smallest error. (★★★)
```python
import numpy as np
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])        # study hours (tens of hours)
y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])       # marks (tens of marks)
```

`hint:` MSE for one `w` = `((w * x - y) ** 2).mean()`: the average squared gap between prediction and truth. Make `ws = np.arange(0, 4.01, 0.1)`, compute a list of MSEs in a loop (or a list comprehension), then `ws[np.argmin(mses)]`.

```python
import numpy as np

x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])

ws = np.arange(0, 4.01, 0.1)                          # candidate slopes 0.0 .. 4.0
mses = np.array([((w * x - y) ** 2).mean() for w in ws])
best = ws[mses.argmin()]
print("best w:", round(best, 2), "MSE:", round(mses.min(), 4))
# Squaring makes every error positive and punishes big misses more.
# Trying every value works for 1 number, but is far too slow for models with thousands of numbers.
```

#### 93. Fitting a line, step 2: **gradient descent** with one number. Start at `w = 0`. Repeat 100 times: compute the slope of the error, `grad = 2 * ((w * x - y) * x).mean()`, and move `w` a small step DOWNHILL: `w = w - 0.01 * grad`. Print `w` every 20 steps. (★★★)
```python
import numpy as np
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])
```

`hint:` Use `for step in range(100):` and update `w` inside the loop. `if step % 20 == 0: print(...)`. The 0.01 is the **learning rate**: the size of each step.

```python
import numpy as np

x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])

w = 0.0
lr = 0.01                                   # learning rate: how big each step is
for step in range(100):
    grad = 2 * ((w * x - y) * x).mean()     # slope of the MSE at the current w
    w = w - lr * grad                       # positive slope -> go left, negative -> go right
    if step % 20 == 0:
        mse = ((w * x - y) ** 2).mean()
        print(f"step {step}: w = {w:.4f}, MSE = {mse:.4f}")
print("final w:", round(w, 4))
# Picture walking down a hill in fog: feel which way is downhill, take a small step, repeat.
# It ends near the best w from exercise 92 (about 2.0) without trying every value.
```

#### 94. Fitting a line, step 3: gradient descent with TWO numbers, slope `w` and intercept `b`, for `y = w * x + b` on simulated study-hours data. Compare your answer with `np.polyfit(x, y, 1)`. (★★★)
```python
import numpy as np
rng = np.random.default_rng(42)
x = rng.uniform(0, 10, size=50)                  # hours of study per week
y = 3.0 * x + 20 + rng.normal(0, 4, size=50)     # marks, with some noise
```

`hint:` Error = `pred - y` with `pred = w * x + b`. Gradients: `grad_w = 2 * (error * x).mean()`, `grad_b = 2 * error.mean()`. Update both each step. Learning rate 0.01, about 5,000 steps. `np.polyfit(x, y, 1)` returns `[slope, intercept]`.

```python
import numpy as np

rng = np.random.default_rng(42)
x = rng.uniform(0, 10, size=50)
y = 3.0 * x + 20 + rng.normal(0, 4, size=50)

w, b = 0.0, 0.0
lr = 0.01
for step in range(5000):
    error = (w * x + b) - y
    grad_w = 2 * (error * x).mean()   # how the MSE changes if w changes a little
    grad_b = 2 * error.mean()         # how the MSE changes if b changes a little
    w -= lr * grad_w
    b -= lr * grad_b

print(f"gradient descent: w = {w:.3f}, b = {b:.3f}")
slope, intercept = np.polyfit(x, y, 1)   # NumPy's exact least-squares answer
print(f"np.polyfit:       w = {slope:.3f}, b = {intercept:.3f}")
# Both are close to the true 3.0 and 20 (noise stops them being exact).
```

#### 95. **Spot the bug / why is this misleading?** Someone min-max scales the training and test amounts SEPARATELY, each with its own min and max. Show why that is wrong: the same amount (100 EUR) ends up with different scaled values. Then fix it using only the training min and max for both. (★★★)
```python
import numpy as np
train = np.array([10.0, 50.0, 100.0, 400.0])
test = np.array([100.0, 30.0, 150.0])
```

`hint:` Scale both with `(x - train.min()) / (train.max() - train.min())`. Test values may then fall outside 0..1, and that is fine. Learning anything (min, max, mean) from the test set is **data leakage**.

```python
import numpy as np

train = np.array([10.0, 50.0, 100.0, 400.0])
test = np.array([100.0, 30.0, 150.0])

def minmax(x, lo, hi):
    return (x - lo) / (hi - lo)

# WRONG: each set uses its own min/max
print(minmax(train, train.min(), train.max()))  # 100 -> 0.231
print(minmax(test, test.min(), test.max()))     # 100 -> 0.583  (same amount, different number!)

# RIGHT: learn min/max on train only, apply the same numbers to test
lo, hi = train.min(), train.max()
print(minmax(train, lo, hi).round(3))
print(minmax(test, lo, hi).round(3))            # 100 -> 0.231 in both now
# The test set stands for future, unseen data. In real life you will not know its min/max
# in advance, so using them makes results look better than they will be.
```

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

```python
import numpy as np

X = np.array([[0.3, 0, 0],
              [5.0, 1, 1],
              [1.2, 0, 1],
              [0.8, 1, 0],
              [9.0, 0, 0]])
w = np.array([0.6, 1.5, 2.0])
b = -4.0

s = X @ w + b                  # raw score: any number, negative = "probably fine"
p = 1 / (1 + np.exp(-s))       # sigmoid squashes it into 0..1
print("scores:", s.round(2))
print("probabilities:", p.round(3))
print("flagged:", (p > 0.5).astype(int))
# This is exactly how logistic regression predicts; training it means finding good w and b
# (with gradient descent, like exercise 94).
```

#### 97. **Cosine similarity**: each customer's spending is a vector of EUR per category [groceries, travel, electronics, restaurants]. Find the customer whose spending PATTERN is most similar to customer 0. Cosine similarity = `a @ b / (norm(a) * norm(b))`; 1 means same direction (same pattern), 0 means nothing in common. (★★★)
```python
import numpy as np
spend = np.array([[300.0,  20.0,  10.0, 120.0],   # customer 0
                  [ 30.0, 900.0, 200.0,  40.0],
                  [600.0,  50.0,  15.0, 230.0],
                  [ 50.0,  10.0, 800.0,  20.0]])
```

`hint:` Compute all at once: `spend @ spend[0]` gives the dot product of every row with customer 0. Divide by `np.linalg.norm(spend, axis=1) * np.linalg.norm(spend[0])`. Ignore customer 0 itself (it is always 1).

```python
import numpy as np

spend = np.array([[300.0,  20.0,  10.0, 120.0],
                  [ 30.0, 900.0, 200.0,  40.0],
                  [600.0,  50.0,  15.0, 230.0],
                  [ 50.0,  10.0, 800.0,  20.0]])

dots = spend @ spend[0]                                       # one dot product per customer
norms = np.linalg.norm(spend, axis=1) * np.linalg.norm(spend[0])
cos = dots / norms
print(cos.round(3))
cos[0] = -1                                                   # exclude customer 0 itself
print("most similar to customer 0:", cos.argmax())           # 2: spends about twice as much, same pattern
# Cosine looks at the PATTERN, not the size: customer 2 is "customer 0 times 2".
```

#### 98. How sure are we about an average? Use the **bootstrap**: resample the 12 swim times WITH replacement 2,000 times, compute the mean of each resample, and report the 2.5th and 97.5th percentiles of those means (a 95% confidence interval). (★★★)
```python
import numpy as np
times = np.array([29.4, 30.1, 28.7, 31.0, 29.9, 30.5, 29.2, 30.8, 28.9, 31.4, 30.0, 29.6])
```

`hint:` `rng.choice(times, size=(2000, 12), replace=True)` makes 2,000 resamples at once (one per row). Then `.mean(axis=1)` and `np.percentile(means, [2.5, 97.5])`.

```python
import numpy as np

times = np.array([29.4, 30.1, 28.7, 31.0, 29.9, 30.5, 29.2, 30.8, 28.9, 31.4, 30.0, 29.6])
rng = np.random.default_rng(42)

# each row = one "new sample" of 12 times drawn from the real ones (repeats allowed)
samples = rng.choice(times, size=(2000, len(times)), replace=True)
means = samples.mean(axis=1)            # 2,000 possible averages
low, high = np.percentile(means, [2.5, 97.5])
print(f"sample mean: {times.mean():.2f} s")
print(f"95% interval: {low:.2f} to {high:.2f} s")
# Meaning: given this data, the swimmer's true average is very likely in that range.
```

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

```python
import numpy as np

rng = np.random.default_rng(42)
X = np.arange(10).reshape(-1, 1) * 10
y = (X[:, 0] >= 60).astype(int)

# BUG: two permutations = two different orders -> labels are attached to the wrong rows
Xb, yb = rng.permutation(X), rng.permutation(y)
print("buggy: does every label still match its amount?", np.array_equal(yb, (Xb[:, 0] >= 60).astype(int)))

# FIX: shuffle the row numbers once and apply them to both
idx = rng.permutation(len(X))
X_shuffled, y_shuffled = X[idx], y[idx]
print(np.column_stack([X_shuffled[:, 0], y_shuffled]))   # big amounts still have label 1
print("fixed:", np.array_equal(y_shuffled, (X_shuffled[:, 0] >= 60).astype(int)))
```

#### 100. **Mini project.** On the real transactions: (1) split the rows 70/30 into train and test with a seeded permutation; (2) on TRAIN only, compute the 95th percentile of amount and use it as the cut-off; (3) on TEST, flag amounts above that cut-off and print TP, FP, FN, TN, precision and recall; (4) in a comment, say whether you would use this rule at a bank. (★★★)

`hint:` Combine exercises 75 (load), 83 (split), 91 (percentile rule) and 81 (confusion matrix). The cut-off comes from `amounts[train_idx]` only (exercise 95).

```python
import numpy as np

data = np.loadtxt("../data/transactions.csv", delimiter=",", skiprows=1, usecols=(6, 7))
amounts, is_fraud = data[:, 0], data[:, 1].astype(int)

# 1) split 70/30 with one permutation
rng = np.random.default_rng(42)
idx = rng.permutation(len(amounts))
cut = int(0.7 * len(amounts))
train_idx, test_idx = idx[:cut], idx[cut:]

# 2) learn the cut-off on TRAIN only (no peeking at test)
threshold = np.percentile(amounts[train_idx], 95)
print(f"train size {len(train_idx)}, test size {len(test_idx)}, cut-off {threshold:.2f} EUR")

# 3) evaluate on TEST
y_true = is_fraud[test_idx]
y_pred = (amounts[test_idx] > threshold).astype(int)
TP = ((y_pred == 1) & (y_true == 1)).sum()
FP = ((y_pred == 1) & (y_true == 0)).sum()
FN = ((y_pred == 0) & (y_true == 1)).sum()
TN = ((y_pred == 0) & (y_true == 0)).sum()
print("TP", TP, "FP", FP, "FN", FN, "TN", TN)
print(f"precision {TP / (TP + FP):.2f}, recall {TP / (TP + FN):.2f}, base fraud rate {y_true.mean():.3f}")

# 4) Not on its own. Precision (~0.07) is about 3-4x the ~2% base rate, so big amounts
# ARE a fraud signal, but recall (~0.17) means most frauds slip through, and most alarms
# are innocent customers. Amount alone is weak: a real system adds more features
# (country, channel, hour) and a trained model, and must beat this simple rule (a "baseline").
```
