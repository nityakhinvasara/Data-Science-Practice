# pandas: the guide

pandas is the Python library for working with tables of data: loading them, cleaning them, summarising them and turning them into features for a model. Almost every data science job uses it every day.

## How to use this guide

- Each Part matches one day of exercises (about 45 minutes). Read only that day's Part first (about 10 minutes).
- Type the small examples yourself in a notebook cell. The output is shown after `#` so you can check.
- Then do the exercises listed at the end of the Part. Use `hint(n)` before `answer(n)`.
- The data files live in `../data/` (one folder up from this lesson folder).

The five datasets you will use again and again:

| File | Rows | What one row is |
|---|---|---|
| `transactions.csv` | 6,000 | one card payment (with `is_fraud` = 1 if it was fraud) |
| `customers.csv` | 800 | one bank customer |
| `swim_results.csv` | 942 | one swim in one race at a meet |
| `swimmers.csv` | 60 | one swimmer |
| `student_marks.csv` | 300 | one student |

---

## Part 1: Series, DataFrames and a first look at data (exercises 1–13)

**What it is.**
- A **Series** is one column of values with a label for each value. The labels are called the **index**.
- A **DataFrame** is a table: several Series side by side that share the same index. Each column has a name.
- A **dtype** (data type) is the kind of value in a column: `int64` (whole numbers), `float64` (decimal numbers), `object` (text), `bool` (True/False), `datetime64` (dates).
- **NaN** ("not a number") is how pandas shows a missing value.

**Why it matters at work.** The first five minutes with any new dataset are always the same: load it, look at the top rows, check the size, types and gaps. A fraud analyst does this before touching anything else.

### Making a Series and a DataFrame

```python
import pandas as pd

s = pd.Series([31.2, 29.8, 30.5], index=["Aarav", "Diya", "Kabir"])
print(s["Diya"])      # 29.8      (look up by label)
print(s.min())        # 29.8      (smallest value)
print(s.idxmin())     # Diya      (the LABEL of the smallest value)

# From a dictionary: key = column name, value = list of values
df = pd.DataFrame({"name": ["Asha", "Bilal"], "marks": [78, 64]})
print(df)
#     name  marks
# 0   Asha     78
# 1  Bilal     64

# From a list of rows: you must give the column names
df2 = pd.DataFrame([["T1", 12.5], ["T2", 230.0]], columns=["id", "amount"])
```

The numbers `0, 1` on the left are the index. If you don't give one, pandas uses 0, 1, 2, ...

### Loading a CSV and looking at it

A **CSV** ("comma-separated values") file is a plain text table: one row per line, values separated by commas.

```python
df = pd.read_csv("../data/transactions.csv")

df.head()        # first 5 rows (head(10) for 10)
df.tail(3)       # last 3 rows
df.shape         # (6000, 8)  -> (rows, columns). No brackets: it is an attribute
df.dtypes        # the type of each column
df.info()        # rows, columns, types and non-missing counts in one go
df.describe()    # count, mean, std, min, quartiles, max of number columns
```

`describe()` shows the **median** as `50%`: the middle value when you sort them. If the mean is much bigger than the median, a few very large values are pulling the mean up (the data is "skewed"). Card payments are like that: most are small, a few are huge.

### Selecting columns

```python
df["channel"]                      # one name  -> a Series
df[["customer_id", "amount_eur"]]  # a LIST of names (double brackets) -> a DataFrame
```

### Counting values

```python
df["channel"].value_counts()
# channel
# in_store       2407
# online         2109
# contactless    1484

df["channel"].value_counts(normalize=True)   # shares that add up to 1 (0.40, 0.35, 0.25)
df["country"].nunique()                       # 7    (how many different values)
df["country"].unique()                        # the different values themselves
```

**Common mistakes**
- Writing `df.shape()` with brackets. `shape` is not a function, so this gives an error.
- Using `df["a", "b"]` for two columns. You need a list inside: `df[["a", "b"]]`.
- Forgetting the path: the notebook runs inside `3-pandas/`, so the file is `../data/transactions.csv`, not `data/transactions.csv`.
- Thinking `object` means something special. In these files it just means "text".

**Now do exercises 1–13.**

---

## Part 2: Picking rows, filtering, sorting and new columns (exercises 14–27)

**What it is.**
- `.loc` picks rows and columns by **label** (the index value and the column name).
- `.iloc` picks rows and columns by **position** (0 = first, 1 = second, -1 = last), like a Python list.
- A **mask** (or boolean mask) is a column of True/False values. `df[mask]` keeps only the rows where the mask is True. This is how you filter.

**Why it matters at work.** "Show me all online payments above 200 EUR from abroad" is a filter. Analysts write dozens of these a day.

### loc and iloc

```python
cust = pd.read_csv("../data/customers.csv")
cust = cust.set_index("customer_id")     # make customer_id the row labels

cust.loc["C0005"]                 # the row with label C0005
cust.loc["C0005", "segment"]      # one cell: [row label, column name]
cust.iloc[0]                      # first row
cust.iloc[10:15]                  # positions 10,11,12,13,14
cust.iloc[-1]                     # last row
```

The big difference when slicing:

| | `cust.loc[0:4]` | `cust.iloc[0:4]` |
|---|---|---|
| Works by | label | position |
| Includes the end (4)? | **yes** -> 5 rows | **no** -> 4 rows |

### Filtering with masks

```python
mask = df["amount_eur"] > 500
print(mask.head(3))     # False, False, False   (one True/False per row)
big = df[mask]          # only rows where mask is True
print(mask.sum())       # 72  -> True counts as 1, so sum() counts the rows
```

Combining conditions:

| Symbol | Meaning | Example |
|---|---|---|
| `&` | and | `(df["channel"] == "online") & (df["amount_eur"] > 200)` |
| `\|` | or | `(df["country"] == "NG") \| (df["country"] == "RU")` |
| `~` | not | `~(df["country"] == "NL")` |

**Put each condition in round brackets.** Python works out `&` before `==`, so without brackets you get an error or a wrong answer.

Two helpers that save typing:

```python
df["country"].isin(["NG", "RU", "US"])   # True if the value is in the list
cust["age"].between(18, 25)              # 18 <= age <= 25 (both ends included)
```

### Sorting

```python
df.sort_values("amount_eur", ascending=False).head(5)   # biggest first
df.nlargest(5, "amount_eur")                            # same thing, shorter
res.sort_values(["event", "time_sec"])                  # by event, then by time inside each event
```

### Adding, renaming and dropping columns

```python
df["amount_inr"] = df["amount_eur"] * 95          # new column, maths on every row at once
res["speed_mps"] = res["distance_m"] / res["time_sec"]   # column / column, row by row

swimmers = swimmers.rename(columns={"name": "swimmer_name"})
swimmers = swimmers.drop(columns=["coach", "joined_date"])
```

`rename` and `drop` give back a **new** table. If you don't save it (`swimmers = ...`), nothing changes.

**Common mistakes**
- Using `and` / `or` instead of `&` / `|`. Python's `and` does not work on whole columns: you get "The truth value of a Series is ambiguous".
- Forgetting brackets around each condition.
- Expecting `loc[0:4]` and `iloc[0:4]` to give the same rows.
- Calling `rename` or `drop` without saving the result.

**Now do exercises 14–27.**

---

## Part 3: Missing values, duplicates, messy text and types (exercises 28–40)

**What it is.** Real data is dirty. This part is about **data cleaning**:
- **Missing values** (NaN): cells with no value.
- **Duplicates**: the same row twice.
- **Messy text**: the same thing written differently (`"50 Free"` vs `"50 free"`, `"Freestyle"` vs `" freestyle "`).
- **Types**: a column stored as the wrong dtype.

**Why it matters at work.** Data scientists often say 70% of the job is cleaning. A duplicated payment counted twice, or a category written two ways, quietly changes every number after it.

### Missing values

```python
res = pd.read_csv("../data/swim_results.csv")
res.isna()            # True where missing (same shape as the table)
res.isna().sum()      # number of missing values per column -> time_sec: 25
res["time_sec"].notna().sum()   # number of filled-in values
```

Three ways to deal with them:

```python
df["merchant_category"] = df["merchant_category"].fillna("unknown")   # fill text
marks = marks.dropna(subset=["sleep_hours"])                          # drop those rows
med = marks["sleep_hours"].median()
marks["sleep_hours"] = marks["sleep_hours"].fillna(med)               # fill with median
```

Always ask **why** it is missing first. In the swim results, `time_sec` is missing exactly when the swimmer was disqualified (DQ). That NaN is correct; filling it with 0 would invent a world record.

### Duplicates

```python
res.duplicated().sum()             # 6 -> rows that repeat an earlier row
res[res.duplicated(keep=False)]    # show EVERY copy (original + repeat)
res = res.drop_duplicates()        # keep the first copy of each
```

### Cleaning text with `.str`

`.str` lets you use Python string methods on every value of a text column.

```python
s = pd.Series([" freestyle ", "Backstroke", "50 free"])
s.str.strip()      # removes spaces at both ends -> "freestyle"
s.str.lower()      # all small letters
s.str.title()      # First Letter Of Each Word Capital -> "Freestyle", "50 Free"
s.str.contains("free")       # True/False per value
s.str.startswith("50")       # True/False per value
"100 Back".split(" ", 1)     # ['100', 'Back']  (plain Python)
s.str.split(" ", n=1, expand=True)   # same for a column; expand=True -> separate columns
```

Careful: `.str.title()` changes **every** value. `"200 IM"` becomes `"200 Im"`. When only one value is wrong, replace just that value:

```python
res["event"] = res["event"].replace({"50 free": "50 Free"})
```

### Changing types

```python
df["is_fraud"].astype(bool)          # 0/1 -> False/True
df["channel"].astype("category")     # text -> category (stores each value once, saves memory)
parts[0].astype(int)                 # text "100" -> number 100
```

### The sum vs count trap

| Method | What it counts | On `is_fraud` |
|---|---|---|
| `.count()` | how many cells are **filled in** (0s included) | 6000 |
| `.sum()` | adds the values (each 1 adds one) | 112 frauds |
| `.mean()` | sum / count = share of 1s | 0.0187 = 1.87% fraud rate |

The same works for any True/False mask: `(df["amount_eur"] > 1000).sum()` counts rows, `.mean()` gives the share.

**Common mistakes**
- Using `.count()` to count frauds (it counts rows).
- Filling a NaN that has a meaning (like DQ) with a number.
- `.str.title()` on a column that has abbreviations like "IM".
- Forgetting to save: `res["event"].replace(...)` alone changes nothing; write `res["event"] = ...`.

**Now do exercises 28–40.**

---

## Part 4: groupby: summaries per group (exercises 41–52)

**What it is.** `groupby` does three steps, often called **split–apply–combine**:
1. **Split** the rows into groups (for example, one group per channel).
2. **Apply** a calculation to each group (for example, the mean amount).
3. **Combine** the answers into one small table.

**Why it matters at work.** "What is the fraud rate per channel / per country / per merchant type?" is the first question in any fraud analysis, and it is one line of groupby.

### The basic pattern

```python
df.groupby("channel")["amount_eur"].mean()
#   group by this ^    take this ^   do this ^
# channel
# contactless    ...
# in_store       ...
# online         ...
```

Because the mean of a 0/1 column is the share of 1s, the **fraud rate** per group is:

```python
df.groupby("channel")["is_fraud"].mean()
```

### Several calculations at once

```python
df.groupby("channel")["amount_eur"].agg(["min", "max", "mean", "median"])
df.groupby("country")["is_fraud"].agg(["mean", "count"])   # rate AND how many rows
```

**Named aggregation** lets you choose the column names yourself. The pattern is `new_name=("column", "function")`:

```python
df.groupby("country").agg(
    n_txn=("transaction_id", "count"),
    n_fraud=("is_fraud", "sum"),
    fraud_rate=("is_fraud", "mean"),
)
```

Useful functions: `"count"`, `"sum"`, `"mean"`, `"median"`, `"min"`, `"max"`, `"nunique"` (number of distinct values), `"first"`, `"last"`.

### Grouping by two columns, and tidying the result

```python
best = ok.groupby(["swimmer_id", "event"])["time_sec"].min()   # index has two levels
best = best.reset_index()       # turns the group labels back into normal columns

long = df.groupby(["channel", "is_fraud"])["amount_eur"].mean()
wide = long.unstack()           # moves the last index level (is_fraud) into the columns
```

### Finding WHICH row is best in each group

`idxmin()` gives the index label of the smallest value. Use it with `.loc` to pull out whole rows:

```python
rows = ok.groupby("event")["time_sec"].idxmin()
ok.loc[rows, ["event", "swimmer_id", "time_sec"]]   # the fastest swim of each event
```

### Small groups lie

A rate from 63 transactions (Russia) can jump a lot with one or two extra frauds. A rate from 4,945 transactions (Netherlands) is steady. Always show the count next to a rate.

**Common mistakes**
- `groupby(...).count()` when you wanted the number of frauds (use `sum`).
- Forgetting that groupby **drops NaN groups** by default. Use `groupby(..., dropna=False)` to keep them.
- Comparing rates without looking at group sizes.
- Grouping swim results without cleaning first: `"50 Free"` and `"50 free"` become two different events.

**Now do exercises 41–52.**

---

## Part 5: Joining tables, stacking, pivot tables and crosstabs (exercises 53–64)

**What it is.**
- **merge** (also called a **join**) puts two tables side by side by matching a **key** column, like `customer_id`. This is the same as SQL `JOIN`.
- **concat** stacks tables on top of each other (more rows).
- A **pivot table** is a groupby shown as a grid: one variable down the side, one across the top.
- A **crosstab** is a pivot table that counts how often each pair of values appears.

**Why it matters at work.** Transactions and customer details live in different tables at a bank. To ask "are students more often victims of fraud?" you must join them first.

### merge and the `how=` options

```python
people = pd.DataFrame({"swimmer_id": ["S1", "S2", "S3"], "name": ["Asha", "Bilal", "Chetan"]})
races = pd.DataFrame({"swimmer_id": ["S1", "S1", "S2", "S9"], "time_sec": [31.0, 30.2, 33.5, 29.9]})

people.merge(races, on="swimmer_id", how="inner")
#   swimmer_id   name  time_sec
# 0         S1   Asha      31.0
# 1         S1   Asha      30.2
# 2         S2  Bilal      33.5
```

| `how=` | Keeps | In the example |
|---|---|---|
| `"inner"` | only keys found in **both** tables | S3 and S9 disappear |
| `"left"` | every row of the **left** table | S3 kept (time = NaN), S9 gone |
| `"right"` | every row of the **right** table | S9 kept (name = NaN), S3 gone |
| `"outer"` | everything from both | all kept, gaps are NaN |

Notice: Asha appears twice because she has two races. A merge copies a row once **for every match**.

Extra options:

```python
res.merge(swimmers, on="swimmer_id", how="left")                     # most common
df.merge(cust, left_on="customer_id", right_on="cust_id")            # key has different names
swimmers.merge(fly, on="swimmer_id", how="left", indicator=True)     # adds a _merge column:
                                                                     # "both", "left_only", "right_only"
```

`indicator=True` is a quick way to find "who is in table A but not in table B".

### concat

```python
both_years = pd.concat([y2024, y2025], ignore_index=True)
```

`ignore_index=True` gives the result a fresh index 0, 1, 2, ... instead of keeping the old row numbers (which would repeat). The column names must match.

### pivot_table and crosstab

```python
df.pivot_table(index="channel", columns="country", values="is_fraud", aggfunc="mean")
# rows = channels, columns = countries, each cell = fraud rate of that pair

df.pivot_table(index="merchant_category", columns="channel",
               values="amount_eur", aggfunc="sum", margins=True)   # margins=True adds "All" totals

pd.crosstab(df["channel"], df["is_fraud"])                       # counts of each pair
pd.crosstab(df["channel"], df["is_fraud"], normalize="index")    # each row adds up to 1
```

**Common mistakes**
- Forgetting `how=`: the default is `"inner"`, which can silently drop rows.
- Merging on a key that is **not unique** in the lookup table: rows get copied (you will meet this as a bug in Part 8).
- Using `concat` when you meant `merge` (or the other way round). Stack = concat, match = merge.
- Forgetting `aggfunc=` in `pivot_table`. The default is mean, which is wrong if you wanted counts or sums.

**Now do exercises 53–64.**

---

## Part 6: Dates, apply/map, bins and a first chart (exercises 65–75)

**What it is.**
- `pd.to_datetime` turns date text like `"2025-01-01 00:09:34"` into real dates, so you can take out the hour, the weekday and do maths with them.
- A **Timedelta** is a length of time (the answer to date minus date).
- `.map` replaces values using a dictionary. `.apply` runs your own function on every value.
- **Binning** puts numbers into ranges: `pd.cut` (you choose the edges) and `pd.qcut` (equal-sized groups).
- `.plot()` draws a chart using the **matplotlib** library.

**Why it matters at work.** Time is one of the strongest fraud signals: payments at 3 a.m. are rarer and riskier. You cannot use it until the column is a real date.

### Dates

```python
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["timestamp"].dt.hour          # 0..23
df["timestamp"].dt.day_name()    # "Monday", ...
df["timestamp"].dt.month         # 1..12
df["timestamp"].max() - df["timestamp"].min()   # a Timedelta: 89 days 23:37:44
(pd.Timestamp("2025-03-31") - cust["account_open_date"]).dt.days   # whole days, per row
```

`.dt` is like `.str`, but for dates: it unlocks the date parts.

**resample** groups by time periods. It needs the dates as the index:

```python
df.set_index("timestamp").resample("W").size()   # rows per week ("D" = day, "MS" = month)
```

### map and apply

```python
lookup = {"NL": "EU", "DE": "EU", "BE": "EU", "FR": "EU"}
df["region"] = df["country"].map(lookup).fillna("non-EU")   # values not in the dict become NaN

def size_label(amount):
    if amount < 20:
        return "small"
    elif amount < 200:
        return "medium"
    else:
        return "large"

df["size"] = df["amount_eur"].apply(size_label)   # pass the function name, no ()
```

### Bins with cut and qcut

```python
pd.cut(pd.Series([5, 25, 700]), bins=[0, 20, 50, float("inf")])
# 0      (0.0, 20.0]
# 1     (20.0, 50.0]
# 2      (50.0, inf]
```

`(0, 20]` means "more than 0, up to and including 20". `float("inf")` is infinity, so the last bin has no top.

```python
pd.qcut(marks["study_hours_per_week"], q=4, labels=["Q1", "Q2", "Q3", "Q4"])
# 4 groups with about the same number of students each
```

When you group by a binned column, add `observed=True` so pandas shows only the bins that exist (and avoids a warning).

### A first chart

```python
import matplotlib.pyplot as plt

rate = df.groupby("channel")["is_fraud"].mean() * 100
ax = rate.plot(kind="bar")        # kind can be "bar", "line", "hist", "barh"...
ax.set_title("Fraud rate by channel")
ax.set_ylabel("Fraud rate (%)")
plt.tight_layout()                # stops labels being cut off
plt.savefig("outputs/fraud_by_channel.png")   # create the folder first with os.makedirs
plt.show()
```

**Common mistakes**
- Using `.dt.hour` before `pd.to_datetime`: you get "Can only use .dt accessor with datetimelike values".
- Writing `.apply(size_label())` with brackets. That calls the function once with nothing; pass the name only.
- Using `resample` without setting the date as the index first.
- Reading partial weeks at the start and end of the data as real drops.

**Now do exercises 65–75.**

---

## Part 7: Feature engineering for fraud, and first bugs (exercises 76–83)

**What it is.** **Feature engineering** means creating new columns (features) that help a model see patterns. A model only sees one row at a time, so useful context, like "is this much more than this customer usually spends?", must be built into the row.

The key new tool is **`groupby(...).transform(...)`**. It works like groupby, but instead of one answer per group, it gives one answer **per original row**, so you can save it as a new column.

**Why it matters at work.** Fraud teams at banks spend most of their time on features like these: how many payments this customer made, how unusual the amount is, how long since the last payment.

### agg vs transform

```python
toy = pd.DataFrame({"cust": ["A", "A", "B"], "amount": [10, 30, 100]})
toy.groupby("cust")["amount"].mean()
# cust
# A     20.0
# B    100.0           -> 2 rows (one per group)

toy["cust_avg"] = toy.groupby("cust")["amount"].transform("mean")
print(toy)
#   cust  amount  cust_avg
# 0    A      10      20.0
# 1    A      30      20.0
# 2    B     100     100.0      -> 3 rows (one per original row)

toy["ratio"] = toy["amount"] / toy["cust_avg"]   # 0.5, 1.5, 1.0
```

### Flags

A **flag** is a 0/1 column that says yes or no.

```python
df["is_night"] = df["timestamp"].dt.hour.between(0, 5).astype(int)
df["is_foreign"] = (df["country"] != "NL").astype(int)
```

### Time since the previous transaction

`diff()` subtracts the previous row from this row. Inside a groupby, it only looks inside each customer. Sort first so "previous" means "earlier in time":

```python
df = df.sort_values(["customer_id", "timestamp"])
gap = df.groupby("customer_id")["timestamp"].diff()       # Timedelta, NaN for the first one
df["hours_since_prev"] = gap.dt.total_seconds() / 3600
```

### Cleaning impossible values

`age = -1` is not a real age; it is a data-entry error. Turn it into NaN first, so it doesn't pull down the mean or median, then fill it:

```python
import numpy as np
cust["age"] = cust["age"].replace(-1, np.nan)
cust["age"] = cust["age"].fillna(cust["age"].median())
```

### Ranking

```python
meet["place"] = meet.groupby("event")["time_sec"].rank(method="min")
# 1 = fastest; method="min" gives tied swimmers the same (best) place
```

### Bug 1: chained assignment

```python
df[df["amount_eur"] > 1000]["amount_eur"] = 1000     # BUG: changes a temporary copy
df.loc[df["amount_eur"] > 1000, "amount_eur"] = 1000 # FIX: one .loc with [rows, column]
```

Two square brackets in a row on the left of `=` is called **chained assignment**. The first `[...]` makes a copy, the second writes into the copy, and the copy is thrown away. pandas shows a `SettingWithCopyWarning`. Never ignore that warning.

### Bug 2: count vs sum inside groupby

`df.groupby("channel")["is_fraud"].count()` counts rows, not frauds. Use `.sum()`.

**Common mistakes**
- Using `groupby().mean()` and then trying to save it as a column: the lengths don't match. Use `transform`.
- Forgetting to sort by time before `diff()`.
- Filling `-1` ages with the median of a column that still contains the `-1`s.
- Ignoring `SettingWithCopyWarning`.

**Now do exercises 76–83.**

---

## Part 8: Rolling windows, swim progress, and misleading numbers (exercises 84–91)

**What it is.**
- A **rolling window** calculates something over the last N rows, moving one row at a time (for example, a 7-day average). It smooths a noisy line.
- **Cumulative** functions run from the first row to the current row: `cumsum` (running total), `cummin` (best so far), `cumcount` (row number inside a group, starting at 0).
- `shift()` moves values down one row, so each row sees the previous row's value.
- **Method chaining** writes steps one after another with dots, without saving tables in between.
- **Reshaping**: a **wide** table has one column per category (2024, 2025); a **long** table has one row per item and category. `pivot_table` goes long to wide, `melt` goes wide to long.

**Why it matters at work.** "Is this swimmer improving?" and "has this customer suddenly started spending more?" are both questions about history, answered with cumulative and rolling functions.

### Rolling and cumulative

```python
s = pd.Series([4, 8, 6, 2])
s.rolling(2).mean()   # NaN, 6.0, 7.0, 4.0   (first value has no partner yet)
s.cumsum()            # 4, 12, 18, 20
s.cummin()            # 4, 4, 4, 2
s.shift()             # NaN, 4, 8, 6
s.cummin().shift()    # NaN, 4, 4, 4   -> "best BEFORE this row"
```

With groups:

```python
df["txn_number"] = df.groupby("customer_id").cumcount() + 1
df["spent_so_far"] = df.groupby("customer_id")["amount_eur"].cumsum()
```

When a calculation is more than one step (like `cummin` then `shift`), give `transform` a small **lambda** (a one-line nameless function):

```python
g = ok.groupby(["swimmer_id", "event"])["time_sec"]
ok["prev_best"] = g.transform(lambda s: s.cummin().shift())
```

### Misleading number 1: a merge that adds rows

If a customer appears twice in the customers table, each of their transactions is copied twice after the merge. Check with `validate=`:

```python
df.merge(cust, on="customer_id", how="left", validate="many_to_one")
# raises MergeError if customer_id is not unique in cust
```

| `validate=` | Means |
|---|---|
| `"one_to_one"` | key unique in both tables |
| `"many_to_one"` | key may repeat on the left, must be unique on the right |

Always compare `len()` before and after a left merge. It should not grow.

### Misleading number 2: the average of averages

The mean of per-country fraud rates treats Russia (63 rows) the same as the Netherlands (4,945 rows). The true overall rate is `df["is_fraud"].mean()`. To combine rates correctly, weight each by its count.

### Method chaining

```python
out = (
    pd.read_csv("../data/transactions.csv")
    .assign(timestamp=lambda d: pd.to_datetime(d["timestamp"]))
    .assign(hour=lambda d: d["timestamp"].dt.hour)    # d = the table at this step
    .query("channel == 'online'")                      # filter with a text condition
    .groupby("hour")["is_fraud"].mean()
)
```

- `.assign(new_col=...)` adds a column and returns the whole table.
- `.query("...")` filters, like a mask, but written as text. Text values need quotes inside: `'online'`.
- The round brackets around the whole chain let you put one step per line.

### Reshaping

```python
wide = back.pivot_table(index="swimmer_id", columns="year", values="time_sec", aggfunc="min")
long = wide.reset_index().melt(id_vars="swimmer_id", var_name="year", value_name="best_time")
```

`id_vars` are the columns that stay as they are; every other column is folded into two columns: its name (`var_name`) and its value (`value_name`).

**Common mistakes**
- Forgetting to sort by date before `first`, `cumsum`, `cummin` or `shift`: "first" then means "first in the file", not "earliest".
- Merging without checking row counts.
- Averaging rates of groups with very different sizes.
- In `query`, forgetting the inner quotes around text: `"channel == online"` looks for a column called `online`.

**Now do exercises 84–91.**

---

## Part 9: Building model-ready tables and judging results (exercises 92–100)

**What it is.**
- A **model-ready table** (also called a feature table) has one row per thing you want to predict, only number columns, no missing values, and the answer column (the **target**, here `is_fraud`) kept separate. People call the features `X` and the target `y`.
- **One-hot encoding** turns a text column into several 0/1 columns, one per value, because models only understand numbers.
- **Target leakage** is when a feature secretly contains the answer. The model looks brilliant in testing and fails in real life.
- **Accuracy** is the share of predictions that are right. **Precision** is "of the payments I flagged, how many were really fraud?". **Recall** is "of all the frauds, how many did I flag?".

**Why it matters at work.** This is exactly what a junior data scientist hands to the modelling step at a bank. In the next lesson (scikit-learn) you will feed `X` and `y` into a model.

### One-hot encoding

```python
toy = pd.DataFrame({"channel": ["online", "in_store", "online"]})
pd.get_dummies(toy, columns=["channel"], dtype=int)
#    channel_in_store  channel_online
# 0                 0               1
# 1                 1               0
# 2                 0               1
```

### Putting the steps in a function

Wrapping your cleaning and feature steps in a function means you can run the same steps on next month's data with one line:

```python
def make_features(path):
    df = pd.read_csv(path)
    # ... all the steps from Parts 6-8 ...
    return df[feature_columns], df["is_fraud"]

X, y = make_features("../data/transactions.csv")
X.isna().sum().sum()     # should be 0
```

`.isna().sum().sum()`: the first `sum` counts per column, the second adds those up into one number.

### Choosing between conditions: `np.select`

```python
import numpy as np
conditions = [df["amount_eur"] > 500, df["amount_eur"] > 50]
choices = ["high", "medium"]
df["level"] = np.select(conditions, choices, default="low")
# checks the conditions in order; the first True one wins
```

### Target leakage

A feature like "this customer's fraud rate over all their transactions" uses `is_fraud`, including the current row and future rows. At the moment a payment happens, you don't know that yet. The honest version only uses the past:

```python
df = df.sort_values(["customer_id", "timestamp"])
df["past_frauds"] = df.groupby("customer_id")["is_fraud"].cumsum() - df["is_fraud"]
```

Rule of thumb: for every feature, ask "could I know this at the moment the payment happens?"

### Why accuracy misleads with rare events

Only about 1.9% of payments are fraud. A "model" that always says "not fraud" is about 98% accurate and catches nothing. With pandas booleans:

```python
accuracy  = (pred == y).mean()
precision = (pred & y).sum() / pred.sum()
recall    = (pred & y).sum() / y.sum()
```

### Dates stored as day/month/year text

Text is compared letter by letter, so `"26/10/2024"` comes after `"20/01/2025"` (because 6 > 0). Convert with an explicit format:

```python
pd.to_datetime(meets["date"], format="%d/%m/%Y")   # %d day, %m month, %Y 4-digit year
```

**Common mistakes**
- Leaving text columns or NaN in `X`. Models will refuse them.
- Building features from the target (leakage).
- Reporting accuracy on rare-event problems.
- Trusting `max()` or `sort_values()` on dates that are still text.

**Now do exercises 92–100.**
