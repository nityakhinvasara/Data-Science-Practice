# pandas: 100 exercises (hints and answers)

_Generated from `tools/source/pandas.ktx`. Don't edit this file; it gets rebuilt._


## Level 1: Easy

#### 1. Import pandas with its usual short name `pd` and print the version number. (★☆☆)

`hint:` `import pandas as pd`, then `pd.__version__` (two underscores on each side).

```python
import pandas as pd

# Everyone writes "pd" so code is easy to read and share
print(pd.__version__)
```

#### 2. A Series is one labelled column of data. Make a Series of five 50 m freestyle times, with the swimmers' names as the index (the labels), and print it. (★☆☆)

```python
times = [31.2, 29.8, 30.5, 32.1, 30.0]
names = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]
```

`hint:` `pd.Series(values, index=labels)`

```python
import pandas as pd

times = [31.2, 29.8, 30.5, 32.1, 30.0]
names = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]

# The index gives each value a name, so we can look things up by name later
s = pd.Series(times, index=names)
print(s)
```

#### 3. Using the Series from exercise 2, print (a) Diya's time, (b) the fastest time, and (c) the name of the fastest swimmer. (★☆☆)

```python
import pandas as pd
s = pd.Series([31.2, 29.8, 30.5, 32.1, 30.0], index=["Aarav", "Diya", "Kabir", "Meera", "Rohan"])
```

`hint:` `s["Diya"]`, `s.min()`, and `s.idxmin()` (gives the label of the smallest value).

```python
import pandas as pd

s = pd.Series([31.2, 29.8, 30.5, 32.1, 30.0], index=["Aarav", "Diya", "Kabir", "Meera", "Rohan"])

print("Diya:", s["Diya"])          # look up by label
print("Fastest time:", s.min())     # smallest number = fastest in swimming
print("Fastest swimmer:", s.idxmin())  # idxmin returns the LABEL, not the value
```

#### 4. A DataFrame is a table: several Series side by side that share one index. Build this DataFrame from a dictionary (each key becomes a column) and print it. (★☆☆)

| name | subject | marks |
|---|---|---|
| Asha | Python | 78 |
| Bilal | Statistics | 64 |
| Chetan | Python | 91 |
| Divya | Databases | 55 |

`hint:` `pd.DataFrame({"name": [...], "subject": [...], "marks": [...]})`

```python
import pandas as pd

# Dictionary: key = column name, value = list of that column's values (same length)
marks = pd.DataFrame({
    "name": ["Asha", "Bilal", "Chetan", "Divya"],
    "subject": ["Python", "Statistics", "Python", "Databases"],
    "marks": [78, 64, 91, 55],
})
print(marks)
```

#### 5. Now build a DataFrame from a list of rows (a list of lists). Use these three card transactions and name the columns `transaction_id`, `amount_eur`, `channel`. Print it. (★☆☆)

```python
rows = [["T1", 12.50, "in_store"], ["T2", 230.00, "online"], ["T3", 4.20, "contactless"]]
```

`hint:` `pd.DataFrame(rows, columns=[...])`. Each inner list is one row.

```python
import pandas as pd

rows = [["T1", 12.50, "in_store"], ["T2", 230.00, "online"], ["T3", 4.20, "contactless"]]

# A list of rows has no column names, so we pass them with columns=
df = pd.DataFrame(rows, columns=["transaction_id", "amount_eur", "channel"])
print(df)
```

#### 6. Load `../data/transactions.csv` into a DataFrame called `df` and print the first 5 rows. (★☆☆)

`hint:` `pd.read_csv(path)` then `df.head()`.

```python
import pandas as pd

# The notebook runs inside 3-pandas/, so the data folder is one level up: ../data
df = pd.read_csv("../data/transactions.csv")
print(df.head())   # head() shows the first 5 rows by default
```

#### 7. For the transactions file, print the last 3 rows, then print how many rows and columns it has. (★☆☆)

`hint:` `df.tail(3)` and `df.shape` (no brackets after shape: it is an attribute, not a function).

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
print(df.tail(3))
# shape is a pair: (number of rows, number of columns)
print(df.shape)
print("rows:", df.shape[0], "columns:", df.shape[1])
```

#### 8. Print the data type (dtype) of every column in the transactions file. Which column holds dates and times, and what type did pandas give it? (★☆☆)

`hint:` `df.dtypes`. `object` means "text" here.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
print(df.dtypes)
# timestamp is "object" (text). read_csv does not turn text into dates by itself.
# We will convert it with pd.to_datetime in Part 6.
print("timestamp dtype:", df["timestamp"].dtype)
```

#### 9. Load `../data/swim_results.csv` and call `.info()`. Use the output to answer: how many rows are there, and how many `time_sec` values are filled in (non-null)? (★☆☆)

`hint:` `.info()` prints its own table, so just call it (no `print` needed). Compare "Non-Null Count" for time_sec with the total rows.

```python
import pandas as pd

res = pd.read_csv("../data/swim_results.csv")
res.info()
# info() shows rows (RangeIndex: 942 entries) and the non-null count per column.
print("rows:", len(res))
print("time_sec filled in:", res["time_sec"].notna().sum())
```

#### 10. Use `.describe()` on the `amount_eur` column of the transactions. Then print just the mean and the maximum on their own lines. Is the mean bigger or smaller than the median (50%)? What does that tell you? (★☆☆)

`hint:` `df["amount_eur"].describe()`, `.mean()`, `.max()`, `.median()`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
print(df["amount_eur"].describe())
print("mean:", round(df["amount_eur"].mean(), 2))
print("max:", df["amount_eur"].max())
print("median:", df["amount_eur"].median())
# Mean (about 63) is much bigger than the median (about 32):
# a few very large payments pull the mean up. The data is "right-skewed".
```

#### 11. From the transactions, select (a) only the `channel` column and (b) the two columns `customer_id` and `amount_eur`. Print the `type()` of each result. Why are they different? (★☆☆)

`hint:` One name in single brackets `df["channel"]` gives a Series. A list of names, so double brackets `df[["a", "b"]]`, gives a DataFrame.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
one = df["channel"]                       # one column -> Series
two = df[["customer_id", "amount_eur"]]    # a LIST of columns -> DataFrame
print(type(one))
print(type(two))
print(two.head(3))
```

#### 12. How many transactions came through each channel? Then show the same as shares (fractions that add up to 1). (★☆☆)

`hint:` `df["channel"].value_counts()` and `value_counts(normalize=True)`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
print(df["channel"].value_counts())
# normalize=True divides each count by the total
print(df["channel"].value_counts(normalize=True).round(3))
```

#### 13. In the transactions: how many different countries appear, what are they, and which 3 countries have the most transactions? (★☆☆)

`hint:` `.nunique()` counts distinct values, `.unique()` lists them, `.value_counts().head(3)` gives the top 3.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
print("number of countries:", df["country"].nunique())
print("countries:", df["country"].unique())
# value_counts is already sorted from most to least common
print(df["country"].value_counts().head(3))
```

#### 14. Load `../data/customers.csv`, make `customer_id` the index, and use `.loc` to print the full row for customer `C0005`. Then print only that customer's `segment`. (★☆☆)

`hint:` `cust = cust.set_index("customer_id")`, then `cust.loc["C0005"]` and `cust.loc["C0005", "segment"]`.

```python
import pandas as pd

cust = pd.read_csv("../data/customers.csv")
# set_index turns a column into the row labels
cust = cust.set_index("customer_id")
print(cust.loc["C0005"])               # .loc looks up by LABEL
print(cust.loc["C0005", "segment"])    # [row label, column name]
```

#### 15. Use `.iloc` (lookup by position, counting from 0) on the transactions to print: the first row, rows at positions 10 to 14, and the very last row. (★☆☆)

`hint:` `df.iloc[0]`, `df.iloc[10:15]` (the end is not included), `df.iloc[-1]`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
print(df.iloc[0])        # position 0 = first row
print(df.iloc[10:15])    # positions 10, 11, 12, 13, 14 (15 is NOT included)
print(df.iloc[-1])       # -1 = last row, like Python lists
```

#### 16. On the customers file (default number index 0, 1, 2 ...), compare `cust.loc[0:4, ["age", "segment"]]` with `cust.iloc[0:4, [1, 5]]`. How many rows does each give, and why? (★☆☆)

`hint:` `.loc` slices by label and INCLUDES the end label. `.iloc` slices by position and EXCLUDES the end, like Python.

```python
import pandas as pd

cust = pd.read_csv("../data/customers.csv")
a = cust.loc[0:4, ["age", "segment"]]   # labels 0..4 -> 5 rows (end included)
b = cust.iloc[0:4, [1, 5]]               # positions 0..3 -> 4 rows (end excluded)
print(a)
print(len(a), "rows with loc")
print(b)
print(len(b), "rows with iloc")
```

#### 17. Keep only the transactions above 500 EUR. How many are there? Print the first 5 of them. (★☆☆)

`hint:` Make a mask (a column of True/False): `mask = df["amount_eur"] > 500`, then `df[mask]`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
mask = df["amount_eur"] > 500        # True where the condition holds
big = df[mask]                       # keeps only the True rows
print("count:", len(big))
print(big.head())
```

#### 18. Find transactions that are online AND above 200 EUR. How many are there? (★☆☆)

`hint:` Join two masks with `&`. Put each condition in its own round brackets: `(cond1) & (cond2)`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
# The brackets matter: without them Python mixes up the order of & and ==
mask = (df["channel"] == "online") & (df["amount_eur"] > 200)
print("online and > 200 EUR:", mask.sum())   # True counts as 1, so sum() counts rows
print(df[mask].head())
```

#### 19. Count transactions from Nigeria (`NG`) OR Russia (`RU`) in two ways: once with `|`, and once with `.isin()`. Then use `.isin()` to count transactions from NG, RU or US. (★☆☆)

`hint:` `(df["country"] == "NG") | (df["country"] == "RU")` and `df["country"].isin(["NG", "RU"])`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
way1 = (df["country"] == "NG") | (df["country"] == "RU")   # | means OR
way2 = df["country"].isin(["NG", "RU"])                     # neater for many values
print(way1.sum(), way2.sum())
print("NG/RU/US:", df["country"].isin(["NG", "RU", "US"]).sum())
```

#### 20. How many customers are aged 18 to 25, including both 18 and 25? (★☆☆)

`hint:` `cust["age"].between(18, 25)` includes both ends by default.

```python
import pandas as pd

cust = pd.read_csv("../data/customers.csv")
young = cust["age"].between(18, 25)   # same as (age >= 18) & (age <= 25)
print("aged 18-25:", young.sum())
```

#### 21. How many transactions happened outside the Netherlands? Use `~` to flip a mask. (★☆☆)

`hint:` `~(df["country"] == "NL")` turns every True into False and back. (`!=` also works.)

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
in_nl = df["country"] == "NL"
abroad = df[~in_nl]          # ~ means NOT
print("abroad:", len(abroad))
print("check with != :", (df["country"] != "NL").sum())
```

#### 22. Show the 5 biggest transactions, biggest first. Do it with `sort_values` and again with `nlargest`. (★☆☆)

`hint:` `df.sort_values("amount_eur", ascending=False).head(5)` and `df.nlargest(5, "amount_eur")`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
cols = ["transaction_id", "amount_eur", "country", "is_fraud"]
print(df.sort_values("amount_eur", ascending=False).head(5)[cols])
print(df.nlargest(5, "amount_eur")[cols])   # shortcut for "top n by a column"
```

#### 23. Sort the swim results by `event` (A to Z) and, inside each event, by `time_sec` (fastest first). Print the first 8 rows of `event`, `swimmer_id`, `time_sec`. (★☆☆)

`hint:` Pass a list to `sort_values`: `sort_values(["event", "time_sec"])`.

```python
import pandas as pd

res = pd.read_csv("../data/swim_results.csv")
# First sort key = event, second key = time (used to break ties inside an event)
out = res.sort_values(["event", "time_sec"])
print(out[["event", "swimmer_id", "time_sec"]].head(8))
```

#### 24. Add a column `amount_inr` to the transactions: the amount in Indian rupees, using 1 EUR = 95 INR. Print `amount_eur` and `amount_inr` for the first 5 rows. (★☆☆)

`hint:` `df["amount_inr"] = df["amount_eur"] * 95`. The maths happens on every row at once.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
# Assigning to a new column name creates the column; maths applies to every row
df["amount_inr"] = (df["amount_eur"] * 95).round(2)
print(df[["amount_eur", "amount_inr"]].head())
```

#### 25. Load `../data/swimmers.csv` and rename `name` to `swimmer_name` and `club` to `team`. Print the column names. (★☆☆)

`hint:` `swimmers.rename(columns={"old": "new", ...})` returns a NEW table, so save it.

```python
import pandas as pd

swimmers = pd.read_csv("../data/swimmers.csv")
# rename gives back a new DataFrame; the old one is unchanged unless we save it
swimmers = swimmers.rename(columns={"name": "swimmer_name", "club": "team"})
print(swimmers.columns.tolist())
```

#### 26. From the swimmers table, drop the `coach` and `joined_date` columns. Print the shape before and after. (★☆☆)

`hint:` `swimmers.drop(columns=["coach", "joined_date"])`.

```python
import pandas as pd

swimmers = pd.read_csv("../data/swimmers.csv")
print("before:", swimmers.shape)
small = swimmers.drop(columns=["coach", "joined_date"])
print("after:", small.shape)
print(small.head(3))
```

#### 27. In the swim results, add a column `speed_mps` = distance in metres divided by time in seconds. Print the 5 fastest swims by speed (show `swimmer_id`, `event`, `time_sec`, `speed_mps`). Why can't we just compare `time_sec` across events? (★☆☆)

`hint:` Divide one column by another: `res["distance_m"] / res["time_sec"]`. Then `nlargest(5, "speed_mps")`.

```python
import pandas as pd

res = pd.read_csv("../data/swim_results.csv")
# Column / column works row by row. DQ rows have no time, so their speed is NaN.
res["speed_mps"] = (res["distance_m"] / res["time_sec"]).round(3)
print(res.nlargest(5, "speed_mps")[["swimmer_id", "event", "time_sec", "speed_mps"]])
# A 50 m time and a 200 m time are not comparable; speed puts them on one scale.
```

#### 28. How many missing values (NaN) does each column have in the swim results? And in the transactions? (★☆☆)

`hint:` `.isna()` gives True where a value is missing; `.isna().sum()` counts the Trues per column.

```python
import pandas as pd

res = pd.read_csv("../data/swim_results.csv")
df = pd.read_csv("../data/transactions.csv")
print(res.isna().sum())
print(df.isna().sum())
```

#### 29. Look at the swim results where `time_sec` is missing. What is their `status`? Does that make sense? (★☆☆)

`hint:` Filter with `res[res["time_sec"].isna()]`, then `value_counts()` on `status`.

```python
import pandas as pd

res = pd.read_csv("../data/swim_results.csv")
no_time = res[res["time_sec"].isna()]
print(no_time["status"].value_counts())
# All of them are DQ (disqualified). A DQ swim has no official time,
# so the NaN is correct: we must NOT fill it with 0 or an average.
```

#### 30. In the transactions, fill the missing `merchant_category` values with the word `"unknown"`. Check with `value_counts()` that `unknown` now appears 30 times and nothing is missing. (★☆☆)

`hint:` `df["merchant_category"] = df["merchant_category"].fillna("unknown")`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
# For a text column, "unknown" is more honest than guessing a category
df["merchant_category"] = df["merchant_category"].fillna("unknown")
print(df["merchant_category"].value_counts())
print("still missing:", df["merchant_category"].isna().sum())
```

#### 31. Load `../data/student_marks.csv`. Drop the rows where `sleep_hours` is missing. Print the shape before and after. (★☆☆)

`hint:` `marks.dropna(subset=["sleep_hours"])`. `subset` means "only look at these columns".

```python
import pandas as pd

marks = pd.read_csv("../data/student_marks.csv")
print("before:", marks.shape)
clean = marks.dropna(subset=["sleep_hours"])   # only drop rows missing sleep_hours
print("after:", clean.shape)
```

#### 32. Instead of dropping, fill the missing `sleep_hours` with the median sleep. Print the median you used and the number still missing. (★☆☆)

`hint:` Work out `med = marks["sleep_hours"].median()` first, then `fillna(med)`.

```python
import pandas as pd

marks = pd.read_csv("../data/student_marks.csv")
med = marks["sleep_hours"].median()   # median ignores NaN by default
marks["sleep_hours"] = marks["sleep_hours"].fillna(med)
print("filled with:", med)
print("still missing:", marks["sleep_hours"].isna().sum())
```

#### 33. How many rows in the swim results are exact duplicates of an earlier row? Print all copies of those rows (both the original and the duplicate) sorted by `result_id`. (★☆☆)

`hint:` `res.duplicated().sum()`. To see every copy use `res[res.duplicated(keep=False)]`.

```python
import pandas as pd

res = pd.read_csv("../data/swim_results.csv")
# duplicated() marks the 2nd, 3rd... copy of a row as True (the first copy stays False)
print("duplicate rows:", res.duplicated().sum())
# keep=False marks EVERY copy, so we can see the pairs side by side
both = res[res.duplicated(keep=False)].sort_values("result_id")
print(both[["result_id", "meet", "swimmer_id", "event", "time_sec"]])
```

#### 34. Remove the duplicate rows from the swim results and save the result as `res`. Print the number of rows before and after. (★☆☆)

`hint:` `res = res.drop_duplicates()`.

```python
import pandas as pd

res = pd.read_csv("../data/swim_results.csv")
print("before:", len(res))
res = res.drop_duplicates()     # keeps the first copy of each row
print("after:", len(res))
```

#### 35. The `event` column is messy: `value_counts()` shows both `"50 Free"` and `"50 free"`. Someone suggests `res["event"].str.title()` to fix it. Try it and look at `value_counts()`. What goes wrong? Then fix only the bad value instead. (★☆☆)

`hint:` `"200 IM".title()` gives `"200 Im"`. Use `res["event"].replace({"50 free": "50 Free"})` instead.

```python
import pandas as pd

res = pd.read_csv("../data/swim_results.csv")
print(res["event"].str.title().value_counts())
# Problem: title() also changes "200 IM" into "200 Im" -> a NEW wrong label.

# Better: replace exactly the bad value and nothing else
res["event"] = res["event"].replace({"50 free": "50 Free"})
print(res["event"].value_counts())
```

#### 36. The `stroke` column has a messy value `" freestyle "` (spaces around it, lower case). Clean the whole column with `.str.strip()` and `.str.title()` so it matches `"Freestyle"`. Check with `value_counts()`. (★☆☆)

`hint:` `.str` lets you use string methods on every value: `res["stroke"].str.strip().str.title()`.

```python
import pandas as pd

res = pd.read_csv("../data/swim_results.csv")
print(res["stroke"].value_counts())
# strip() removes spaces at the start and end; title() makes "freestyle" -> "Freestyle"
res["stroke"] = res["stroke"].str.strip().str.title()
print(res["stroke"].value_counts())
```

#### 37. Split the cleaned `event` column (e.g. `"100 Back"`) into two new columns: `dist_text` (`"100"`) and `stroke_code` (`"Back"`). Then turn `dist_text` into a number and check it always equals `distance_m`. (★☆☆)

`hint:` `res["event"].str.split(" ", n=1, expand=True)` gives two columns (0 and 1). Turn text into numbers with `.astype(int)`.

```python
import pandas as pd

res = pd.read_csv("../data/swim_results.csv")
res["event"] = res["event"].replace({"50 free": "50 Free"})
# expand=True puts the pieces in separate columns instead of a list
parts = res["event"].str.split(" ", n=1, expand=True)
res["dist_text"] = parts[0]
res["stroke_code"] = parts[1]
print(res[["event", "dist_text", "stroke_code"]].head())
# Text "100" and number 100 are different things; astype converts the type
same = res["dist_text"].astype(int) == res["distance_m"]
print("all match:", same.all())
```

#### 38. In the transactions, convert `is_fraud` to `bool` (True/False) and `channel` to the `category` type. Print the dtypes of those two columns. (A category column stores each distinct text value only once, which saves memory.) (★☆☆)

`hint:` `df["is_fraud"].astype(bool)` and `df["channel"].astype("category")`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
df["is_fraud"] = df["is_fraud"].astype(bool)
df["channel"] = df["channel"].astype("category")
print(df[["is_fraud", "channel"]].dtypes)
print(df["channel"].cat.categories)   # the distinct values it stores
```

#### 39. A classic trap. Your friend wants the number of fraud transactions and writes `df["is_fraud"].count()`. Run it, then run `df["is_fraud"].sum()` and `df["is_fraud"].mean()`. Which one answers the question, and what do the other two mean? (★☆☆)

`hint:` `count()` counts filled-in cells (any value, even 0). `sum()` adds the values, and since fraud = 1, it counts frauds.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
print("count():", df["is_fraud"].count())  # 6000 = number of NON-MISSING values, 0s included
print("sum():  ", df["is_fraud"].sum())    # adds the 1s -> number of frauds (correct)
print("mean(): ", round(df["is_fraud"].mean(), 4))  # share of 1s = fraud RATE
```

#### 40. Without filtering into a new table, answer with one line each: (a) how many transactions are above 1,000 EUR, (b) what fraction of transactions are online, (c) how many swim results were disqualified (`status == "DQ"`). (★☆☆)

`hint:` A True/False column behaves like 1/0: `.sum()` counts the Trues, `.mean()` gives the fraction.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
res = pd.read_csv("../data/swim_results.csv")
print("above 1000 EUR:", (df["amount_eur"] > 1000).sum())
print("share online:", round((df["channel"] == "online").mean(), 3))
print("DQ swims:", (res["status"] == "DQ").sum())
```


## Level 2: Medium

#### 41. `groupby` splits a table into groups, does a calculation on each group, and joins the answers. What is the average transaction amount for each channel? (★★☆)

`hint:` `df.groupby("channel")["amount_eur"].mean()`. Read it as: "group by channel, take amount, average it".

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
avg = df.groupby("channel")["amount_eur"].mean().round(2)
print(avg)
```

#### 42. How many transactions are there per `merchant_category`? Compare `groupby("merchant_category").size()` with `value_counts(dropna=False)`. Where did the 30 missing categories go in the groupby result, and how do you keep them? (★★☆)

`hint:` `groupby` leaves out NaN groups unless you pass `dropna=False`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
print(df.groupby("merchant_category").size())   # NaN group is silently left out
print("total:", df.groupby("merchant_category").size().sum())  # 5970, not 6000
print(df.groupby("merchant_category", dropna=False).size())   # NaN group kept
print(df["merchant_category"].value_counts(dropna=False))
```

#### 43. What is the fraud rate (share of frauds) for each channel? Show it as a percentage with 2 decimals, highest first. (★★☆)

`hint:` The mean of a 0/1 column is the rate: `df.groupby("channel")["is_fraud"].mean()`, then `* 100`, `.round(2)`, `.sort_values(ascending=False)`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
rate = df.groupby("channel")["is_fraud"].mean() * 100   # mean of 0/1 = share of 1s
print(rate.round(2).sort_values(ascending=False))
```

#### 44. Show, for each country, the fraud rate AND the number of transactions, in one table. Why should you look at the count before trusting a country's rate? (★★☆)

`hint:` Pass a list to `.agg`: `df.groupby("country")["is_fraud"].agg(["mean", "count"])`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
out = df.groupby("country")["is_fraud"].agg(["mean", "count"])
print(out.sort_values("mean", ascending=False).round(3))
# A rate from 63 transactions (RU) is much less certain than one from 4,945 (NL):
# one or two extra frauds would change it a lot.
```

#### 45. Which merchant categories have the highest fraud rate? Print all categories, highest rate first, as percentages with 1 decimal. (★★☆)

`hint:` Same pattern as exercise 43, grouped by `merchant_category`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
rate = df.groupby("merchant_category")["is_fraud"].mean().sort_values(ascending=False)
print((rate * 100).round(1))
```

#### 46. For each channel, show the min, max, mean and median transaction amount in one table. (★★☆)

`hint:` `.agg(["min", "max", "mean", "median"])` on the grouped `amount_eur` column.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
stats = df.groupby("channel")["amount_eur"].agg(["min", "max", "mean", "median"])
print(stats.round(2))
```

#### 47. Build one summary table per country with clear column names: `n_txn` (number of transactions), `n_fraud` (number of frauds), `fraud_rate`, and `avg_amount`. Sort by `fraud_rate`, highest first. (★★☆)

`hint:` Named aggregation: `.agg(new_name=("column", "function"), ...)`. For example `n_fraud=("is_fraud", "sum")`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
# Named aggregation: new_column=(column_to_use, function_to_apply)
summary = df.groupby("country").agg(
    n_txn=("transaction_id", "count"),
    n_fraud=("is_fraud", "sum"),        # sum, not count! (see exercise 39)
    fraud_rate=("is_fraud", "mean"),
    avg_amount=("amount_eur", "mean"),
)
print(summary.sort_values("fraud_rate", ascending=False).round(3))
```

#### 48. Do fraud transactions have bigger amounts? Group by both `channel` and `is_fraud`, take the mean amount, and then use `.unstack()` to turn `is_fraud` into columns so it reads like a small table. (★★☆)

`hint:` `df.groupby(["channel", "is_fraud"])["amount_eur"].mean().unstack()`. `unstack` moves the last index level into the columns.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
long = df.groupby(["channel", "is_fraud"])["amount_eur"].mean()
print(long)                      # two-level index: (channel, is_fraud)
wide = long.unstack()            # is_fraud values 0 and 1 become columns
print(wide.round(2))
```

#### 49. Find each swimmer's best (fastest) time in each event. First clean the data: drop duplicates, fix `"50 free"`, and keep only `status == "OK"`. Print the first 10 rows as a normal table (not an index). (★★☆)

`hint:` `groupby(["swimmer_id", "event"])["time_sec"].min()`, then `.reset_index()` turns the group labels back into columns.

```python
import pandas as pd

res = pd.read_csv("../data/swim_results.csv")
res = res.drop_duplicates()
res["event"] = res["event"].replace({"50 free": "50 Free"})
ok = res[res["status"] == "OK"]

# Best = smallest time. Group by BOTH swimmer and event.
best = ok.groupby(["swimmer_id", "event"])["time_sec"].min().reset_index()
best = best.rename(columns={"time_sec": "best_time"})
print(best.head(10))
print("rows:", len(best))
```

#### 50. Which 5 swimmers swam the most races (after dropping duplicates)? Also show how many different meets each of those swimmers attended. Remember the same meet name happens in different years, so count distinct dates. (★★☆)

`hint:` `.agg(races=("result_id", "count"), meets=("date", "nunique"))`, then `nlargest(5, "races")`.

```python
import pandas as pd

res = pd.read_csv("../data/swim_results.csv").drop_duplicates()
per = res.groupby("swimmer_id").agg(
    races=("result_id", "count"),
    meets=("date", "nunique"),   # each meet has its own date, even with the same name
)
print(per.nlargest(5, "races"))
```

#### 51. Who holds the fastest time in each event? Use `idxmin` to find the row number of the fastest swim per event, then use `.loc` to pull those rows. Show `event`, `swimmer_id`, `time_sec`, `meet`. (★★☆)

`hint:` `rows = ok.groupby("event")["time_sec"].idxmin()` gives index labels; then `ok.loc[rows, [...]]`.

```python
import pandas as pd

res = pd.read_csv("../data/swim_results.csv").drop_duplicates()
res["event"] = res["event"].replace({"50 free": "50 Free"})
ok = res[res["status"] == "OK"]

# idxmin gives the index LABEL of the smallest time in each group
rows = ok.groupby("event")["time_sec"].idxmin()
print(ok.loc[rows, ["event", "swimmer_id", "time_sec", "meet"]])
```

#### 52. Using the student marks: (a) what is the average `final_marks` for students with and without a part-time job? (b) what is the pass rate per `favourite_subject`, highest first? (★★☆)

`hint:` Two separate groupbys: by `part_time_job` (mean of final_marks) and by `favourite_subject` (mean of passed).

```python
import pandas as pd

marks = pd.read_csv("../data/student_marks.csv")
print(marks.groupby("part_time_job")["final_marks"].mean().round(1))
# passed is 0/1, so its mean is the pass rate
print(marks.groupby("favourite_subject")["passed"].mean().sort_values(ascending=False).round(3))
```

#### 53. `merge` joins two tables on a shared key column. Join the swim results with the swimmers table on `swimmer_id` (keep every result: `how="left"`). Print the shape before and after, and the first 3 rows with `name`, `club`, `event`, `time_sec`. (★★☆)

`hint:` `res.merge(swimmers, on="swimmer_id", how="left")`. Each result row gets that swimmer's details added.

```python
import pandas as pd

res = pd.read_csv("../data/swim_results.csv")
swimmers = pd.read_csv("../data/swimmers.csv")
full = res.merge(swimmers, on="swimmer_id", how="left")
# One swimmer row matches many result rows, so the row count stays the same as res
print("results:", res.shape, "after merge:", full.shape)
print(full[["name", "club", "event", "time_sec"]].head(3))
```

#### 54. Join the transactions with the customers and find the fraud rate for each customer `segment` (student / standard / premium). (★★☆)

`hint:` Merge on `customer_id`, then `groupby("segment")["is_fraud"].mean()`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
cust = pd.read_csv("../data/customers.csv")
both = df.merge(cust, on="customer_id", how="left")
print(both.groupby("segment")["is_fraud"].agg(["mean", "count"]).round(4))
```

#### 55. See what each `how=` option does. Merge the two small tables below with `how="inner"`, `"left"`, `"right"` and `"outer"`, and print each result. Which swimmer or result disappears in each case? (★★☆)

```python
import pandas as pd
people = pd.DataFrame({"swimmer_id": ["S1", "S2", "S3"], "name": ["Asha", "Bilal", "Chetan"]})
races = pd.DataFrame({"swimmer_id": ["S1", "S1", "S2", "S9"], "time_sec": [31.0, 30.2, 33.5, 29.9]})
```

`hint:` inner = only keys in both; left = all of the left table; right = all of the right table; outer = everything. Missing partners become NaN.

```python
import pandas as pd

people = pd.DataFrame({"swimmer_id": ["S1", "S2", "S3"], "name": ["Asha", "Bilal", "Chetan"]})
races = pd.DataFrame({"swimmer_id": ["S1", "S1", "S2", "S9"], "time_sec": [31.0, 30.2, 33.5, 29.9]})

for how in ["inner", "left", "right", "outer"]:
    print(f"--- how='{how}' ---")
    print(people.merge(races, on="swimmer_id", how=how))
# inner: S3 (no races) and S9 (unknown swimmer) both disappear
# left:  S3 kept with NaN time; S9 gone
# right: S9 kept with NaN name; S3 gone
# outer: everyone kept
```

#### 56. Which swimmers have NEVER swum the 50 Fly? Merge the swimmers table with the 50 Fly results using `how="left"` and `indicator=True`, then keep the rows marked `left_only`. Print how many and their names. (★★☆)

`hint:` `indicator=True` adds a `_merge` column saying `both`, `left_only` or `right_only`. Use only one row per swimmer from the results (`drop_duplicates("swimmer_id")`) so the merge does not repeat swimmers.

```python
import pandas as pd

res = pd.read_csv("../data/swim_results.csv")
swimmers = pd.read_csv("../data/swimmers.csv")

fly = res[res["event"] == "50 Fly"][["swimmer_id"]].drop_duplicates()
m = swimmers.merge(fly, on="swimmer_id", how="left", indicator=True)
print(m["_merge"].value_counts())
# (Two different swimmers are both called "Arjun Kulkarni": that is why we join on IDs, not names.)
missing = m[m["_merge"] == "left_only"]   # in swimmers but not in the 50 Fly results
print("never swam 50 Fly:", len(missing))
print(missing["name"].tolist())
```

#### 57. Sometimes the key column has a different name in each table. Below, the customers table calls it `cust_id`. Merge the transactions with it using `left_on` and `right_on`, and print the first 3 rows of `customer_id`, `cust_id`, `segment`. (★★☆)

```python
import pandas as pd
df = pd.read_csv("../data/transactions.csv")
cust = pd.read_csv("../data/customers.csv").rename(columns={"customer_id": "cust_id"})
```

`hint:` `df.merge(cust, left_on="customer_id", right_on="cust_id", how="left")`. Both key columns are kept.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
cust = pd.read_csv("../data/customers.csv").rename(columns={"customer_id": "cust_id"})

both = df.merge(cust, left_on="customer_id", right_on="cust_id", how="left")
print(both[["customer_id", "cust_id", "segment"]].head(3))
both = both.drop(columns="cust_id")   # the two key columns are the same, keep one
print(both.shape)
```

#### 58. `concat` stacks tables on top of each other. Split the swim results into a 2024 table and a 2025 table (use the `date` text: it starts with the year), then stack them back with `pd.concat`. Check the row count matches the original. What does `ignore_index=True` change? (★★☆)

`hint:` `res[res["date"].str.startswith("2024")]`, then `pd.concat([a, b], ignore_index=True)`.

```python
import pandas as pd

res = pd.read_csv("../data/swim_results.csv")
y2024 = res[res["date"].str.startswith("2024")]
y2025 = res[res["date"].str.startswith("2025")]
print(len(y2024), len(y2025))

stacked = pd.concat([y2024, y2025], ignore_index=True)
print("same rows as original:", len(stacked) == len(res))
# ignore_index=True gives a fresh index 0..n-1 instead of keeping the old row numbers
print(stacked.index[:5].tolist(), stacked.index[-3:].tolist())
```

#### 59. Two new transactions arrive. Add them to the bottom of the transactions table with `pd.concat` and print the new shape and the last 3 rows. (★★☆)

```python
new = pd.DataFrame({
    "transaction_id": ["T90001", "T90002"], "customer_id": ["C0001", "C0002"],
    "timestamp": ["2025-04-01 09:15:00", "2025-04-01 03:02:00"],
    "merchant_category": ["groceries", "gift_cards"], "channel": ["in_store", "online"],
    "country": ["NL", "NG"], "amount_eur": [23.10, 480.00], "is_fraud": [0, 1],
})
```

`hint:` `pd.concat([df, new], ignore_index=True)`. The column names must match.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
new = pd.DataFrame({
    "transaction_id": ["T90001", "T90002"], "customer_id": ["C0001", "C0002"],
    "timestamp": ["2025-04-01 09:15:00", "2025-04-01 03:02:00"],
    "merchant_category": ["groceries", "gift_cards"], "channel": ["in_store", "online"],
    "country": ["NL", "NG"], "amount_eur": [23.10, 480.00], "is_fraud": [0, 1],
})
df = pd.concat([df, new], ignore_index=True)
print(df.shape)
print(df.tail(3))
```

#### 60. A pivot table is a groupby shown as a grid. Make a table of fraud rate (%) with channels as rows and countries as columns. (★★☆)

`hint:` `df.pivot_table(index="channel", columns="country", values="is_fraud", aggfunc="mean")`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
grid = df.pivot_table(index="channel", columns="country", values="is_fraud", aggfunc="mean")
print((grid * 100).round(1))
```

#### 61. Make a pivot table of the total amount spent (sum of `amount_eur`) per `merchant_category` (rows) and `channel` (columns), with row and column totals. (★★☆)

`hint:` `aggfunc="sum"` and `margins=True` adds an "All" row and column with totals.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
grid = df.pivot_table(index="merchant_category", columns="channel",
                      values="amount_eur", aggfunc="sum", margins=True)
print(grid.round(0))
```

#### 62. `pd.crosstab` counts how often each pair of values appears. Count transactions by `channel` and `is_fraud`. Then show it with `normalize="index"` so each row adds up to 1. (★★☆)

`hint:` `pd.crosstab(df["channel"], df["is_fraud"])` and add `normalize="index"`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
print(pd.crosstab(df["channel"], df["is_fraud"]))
# normalize="index" divides each row by its row total -> column 1 is the fraud rate
print(pd.crosstab(df["channel"], df["is_fraud"], normalize="index").round(4))
```

#### 63. How many boys and girls does each club have? Use `pd.crosstab` on the swimmers table with `club` as rows and `gender` as columns, plus totals. (★★☆)

`hint:` `pd.crosstab(swimmers["club"], swimmers["gender"], margins=True)`.

```python
import pandas as pd

swimmers = pd.read_csv("../data/swimmers.csv")
print(pd.crosstab(swimmers["club"], swimmers["gender"], margins=True))
```

#### 64. Which club is fastest at 50 Free? Clean the results (drop duplicates, fix `"50 free"`, OK only), keep 50 Free, merge with swimmers, and make a pivot table of the best (minimum) time with `club` as rows and `gender` as columns. (★★☆)

`hint:` Filter, merge, then `pivot_table(index="club", columns="gender", values="time_sec", aggfunc="min")`.

```python
import pandas as pd

res = pd.read_csv("../data/swim_results.csv").drop_duplicates()
swimmers = pd.read_csv("../data/swimmers.csv")
res["event"] = res["event"].replace({"50 free": "50 Free"})

free50 = res[(res["status"] == "OK") & (res["event"] == "50 Free")]
free50 = free50.merge(swimmers, on="swimmer_id", how="left")
grid = free50.pivot_table(index="club", columns="gender", values="time_sec", aggfunc="min")
print(grid)
```

#### 65. Convert the transaction `timestamp` column from text to real dates with `pd.to_datetime`. Print its new dtype, the first and last timestamp, and how many days the data covers. (★★☆)

`hint:` `df["timestamp"] = pd.to_datetime(df["timestamp"])`. Subtracting two dates gives a Timedelta with `.days`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
print(df["timestamp"].dtype)               # datetime64[ns]
print("first:", df["timestamp"].min())
print("last: ", df["timestamp"].max())
span = df["timestamp"].max() - df["timestamp"].min()   # a Timedelta
print("days covered:", span.days)
```

#### 66. Add two columns: `hour` (0–23) and `weekday` (e.g. "Monday"). How many transactions happen at each hour? (★★☆)

`hint:` After `to_datetime`, use `.dt.hour` and `.dt.day_name()`. Then `value_counts().sort_index()` to list hours in order.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["hour"] = df["timestamp"].dt.hour            # .dt unlocks date parts
df["weekday"] = df["timestamp"].dt.day_name()
print(df[["timestamp", "hour", "weekday"]].head(3))
print(df["hour"].value_counts().sort_index())   # sort by hour, not by count
```

#### 67. What is the fraud rate per hour of the day? Print the 5 riskiest hours. (★★☆)

`hint:` Make the `hour` column, then `groupby("hour")["is_fraud"].mean()` and `nlargest(5)`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["hour"] = df["timestamp"].dt.hour
rate = df.groupby("hour")["is_fraud"].mean()
print((rate.nlargest(5) * 100).round(1))
# Night hours (0-5) stand out: few people shop then, but fraudsters do.
```

#### 68. For each month (January, February, March), show the number of transactions and the total amount. (★★☆)

`hint:` `df["month"] = df["timestamp"].dt.month`, then named agg with `("transaction_id", "count")` and `("amount_eur", "sum")`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["month"] = df["timestamp"].dt.month
out = df.groupby("month").agg(n_txn=("transaction_id", "count"),
                              total_eur=("amount_eur", "sum"))
print(out.round(2))
```

#### 69. Count transactions per week using `resample`. `resample("W")` groups rows by calendar week, but it needs the dates as the index. (★★☆)

`hint:` `df.set_index("timestamp").resample("W").size()`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
# resample works on a date index: each label is the END of that week (a Sunday)
weekly = df.set_index("timestamp").resample("W").size()
print(weekly)
# Careful: the first and last "weeks" are only partly inside the data (Jan 1 is a
# Wednesday, the data stops on Mar 31), so their counts look low. That is not a real drop.
```

#### 70. How old is each customer's account on 2025-03-31? Add a column `account_age_days` to the customers table and print its min, mean and max. (★★☆)

`hint:` Convert `account_open_date` with `pd.to_datetime`, then `(pd.Timestamp("2025-03-31") - cust["account_open_date"]).dt.days`.

```python
import pandas as pd

cust = pd.read_csv("../data/customers.csv")
cust["account_open_date"] = pd.to_datetime(cust["account_open_date"])
ref = pd.Timestamp("2025-03-31")
# date - date = a duration; .dt.days turns it into a whole number of days
cust["account_age_days"] = (ref - cust["account_open_date"]).dt.days
print(cust["account_age_days"].agg(["min", "mean", "max"]).round(1))
```

#### 71. `.map` replaces each value using a dictionary. Add a column `region` to the transactions: NL, DE, BE and FR are `"EU"`, everything else is `"non-EU"`. Then show the fraud rate per region. (★★☆)

`hint:` `df["country"].map(lookup)`. Any country missing from the dict becomes NaN, so fill those with `"non-EU"`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
lookup = {"NL": "EU", "DE": "EU", "BE": "EU", "FR": "EU"}
# Countries not in the dict become NaN; fillna turns them into "non-EU"
df["region"] = df["country"].map(lookup).fillna("non-EU")
print(df["region"].value_counts())
print(df.groupby("region")["is_fraud"].mean().round(4))
```

#### 72. Write a function `size_label(amount)` that returns `"small"` below 20 EUR, `"medium"` from 20 up to (not including) 200, and `"large"` from 200. Use `.apply` to make a column `size` and print its counts. (★★☆)

`hint:` A normal `def` with `if / elif / else`, then `df["amount_eur"].apply(size_label)` (pass the function name, no brackets).

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")

def size_label(amount):
    if amount < 20:
        return "small"
    elif amount < 200:
        return "medium"
    else:
        return "large"

# apply calls the function once for every value in the column
df["size"] = df["amount_eur"].apply(size_label)
print(df["size"].value_counts())
```

#### 73. `pd.cut` puts numbers into ranges (bins) you choose. Cut `amount_eur` into the bins 0–20, 20–50, 50–100, 100–500, 500 and more, and print the number of transactions and the fraud rate per bin. (★★☆)

`hint:` `pd.cut(df["amount_eur"], bins=[0, 20, 50, 100, 500, float("inf")])`. Group by the new column with `observed=True`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
bins = [0, 20, 50, 100, 500, float("inf")]
df["amount_bin"] = pd.cut(df["amount_eur"], bins=bins)   # (0, 20] means >0 and <=20
# observed=True: only show bins that actually occur (and avoids a warning)
out = df.groupby("amount_bin", observed=True)["is_fraud"].agg(["count", "mean"])
print(out.round(4))
```

#### 74. `pd.qcut` makes bins with (about) the same NUMBER of rows in each. Split the students into 4 equal groups by `study_hours_per_week`, labelled `"Q1"` to `"Q4"`, and print the average `final_marks` per group. (★★☆)

`hint:` `pd.qcut(marks["study_hours_per_week"], q=4, labels=["Q1", "Q2", "Q3", "Q4"])`.

```python
import pandas as pd

marks = pd.read_csv("../data/student_marks.csv")
marks["study_q"] = pd.qcut(marks["study_hours_per_week"], q=4, labels=["Q1", "Q2", "Q3", "Q4"])
print(marks["study_q"].value_counts().sort_index())   # about 75 students each
print(marks.groupby("study_q", observed=True)["final_marks"].mean().round(1))
```

#### 75. Make your first chart: a bar chart of the fraud rate (%) per channel. Give it a title and a y-axis label, save it to `outputs/fraud_by_channel.png`, and show it. (★★☆)

`hint:` `rate.plot(kind="bar")` returns an `ax` you can label: `ax.set_title(...)`, `ax.set_ylabel(...)`. Then `plt.savefig(...)` and `plt.show()`.

```python
import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/transactions.csv")
rate = df.groupby("channel")["is_fraud"].mean().sort_values() * 100

ax = rate.plot(kind="bar", color="steelblue")   # pandas draws with matplotlib
ax.set_title("Fraud rate by channel")
ax.set_ylabel("Fraud rate (%)")
ax.set_xlabel("")
plt.tight_layout()                               # stops labels being cut off

os.makedirs("outputs", exist_ok=True)
plt.savefig("outputs/fraud_by_channel.png")
plt.show()
print("saved outputs/fraud_by_channel.png")
```


## Level 3: Hard

#### 76. Some customers have `age = -1`, a data-entry error. Count them, compare the average age with and without them, replace -1 with `NaN` (missing), and fill those with the median age of real values. Why replace with NaN first instead of filling directly? (★★★)

`hint:` `cust["age"].replace(-1, np.nan)` (import numpy as np). Then `median()` skips NaN automatically.

```python
import numpy as np
import pandas as pd

cust = pd.read_csv("../data/customers.csv")
bad = cust["age"] == -1
print("age = -1:", bad.sum())
print("mean age with errors:", round(cust["age"].mean(), 2))

# Step 1: mark the errors as missing, so no calculation treats -1 as a real age
cust["age"] = cust["age"].replace(-1, np.nan)
print("mean age without errors:", round(cust["age"].mean(), 2))

# Step 2: fill with the median of the REAL ages (if we had used the column with -1s,
# the -1s would have pulled the median down)
cust["age"] = cust["age"].fillna(cust["age"].median())
print("min age now:", cust["age"].min(), "missing:", cust["age"].isna().sum())
```

#### 77. Feature engineering means making new columns that help a model. Add a column `n_txn` to the transactions: how many transactions that customer has in total. Use `groupby(...).transform("count")`. Print the shape of `groupby().count()` vs `transform()` to see the difference. (★★★)

`hint:` `df.groupby("customer_id")["transaction_id"].transform("count")`. `transform` returns one value per ORIGINAL row (6,000), not one per group (800).

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
per_customer = df.groupby("customer_id")["transaction_id"].count()
print("agg result:", per_customer.shape)        # (800,) one row per customer

# transform repeats each customer's result on every one of their rows
df["n_txn"] = df.groupby("customer_id")["transaction_id"].transform("count")
print("transform result:", df["n_txn"].shape)   # (6000,) lines up with df
print(df[["customer_id", "amount_eur", "n_txn"]].head())
```

#### 78. A payment of 300 EUR is normal for some customers and strange for others. Add `cust_avg` (the customer's own average amount) and `amount_ratio` = amount / cust_avg. Compare the fraud rate for transactions with `amount_ratio > 3` versus the rest. (★★★)

`hint:` `transform("mean")` for the average, then divide. Group by the True/False column `df["amount_ratio"] > 3`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
df["cust_avg"] = df.groupby("customer_id")["amount_eur"].transform("mean")
df["amount_ratio"] = df["amount_eur"] / df["cust_avg"]

unusual = df["amount_ratio"] > 3      # 3x more than this customer usually spends
print(df.groupby(unusual)["is_fraud"].agg(["count", "mean"]).round(4))
```

#### 79. Add two 0/1 flag columns: `is_night` (hour 0 to 5) and `is_foreign` (country is not NL). Then show the fraud rate and count for every combination of the two flags. (★★★)

`hint:` `df["timestamp"].dt.hour.between(0, 5).astype(int)` and `(df["country"] != "NL").astype(int)`. Group by both flags.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
# astype(int) turns True/False into 1/0, which models like
df["is_night"] = df["timestamp"].dt.hour.between(0, 5).astype(int)
df["is_foreign"] = (df["country"] != "NL").astype(int)

out = df.groupby(["is_night", "is_foreign"])["is_fraud"].agg(["count", "mean"])
print(out.round(4))
# Night + foreign together (about 4.3%) is riskier than either one alone.
```

#### 80. For each transaction, how many hours have passed since the same customer's previous transaction? Sort by customer and time, then use `groupby("customer_id")["timestamp"].diff()`. The first transaction of each customer has no previous one: what value does it get? (★★★)

`hint:` `diff()` gives a Timedelta; turn it into hours with `.dt.total_seconds() / 3600`. Sort with `sort_values(["customer_id", "timestamp"])` first.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values(["customer_id", "timestamp"])   # diff needs time order inside each customer

gap = df.groupby("customer_id")["timestamp"].diff()   # this time minus the previous time
df["hours_since_prev"] = gap.dt.total_seconds() / 3600
print(df[["customer_id", "timestamp", "hours_since_prev"]].head(8))
# Each customer's first transaction gets NaN (nothing to compare with).
print("NaN count:", df["hours_since_prev"].isna().sum(), "= number of customers")
```

#### 81. Spot the bug. A colleague wants to cap every amount above 1,000 EUR at 1,000 and writes the code below. Run it: did the table change? Explain why not, and fix it. (★★★)

```python
df[df["amount_eur"] > 1000]["amount_eur"] = 1000
print(df["amount_eur"].max())
```

`hint:` `df[mask]` makes a temporary copy, and the second `[...] =` changes the copy. Do it in one step: `df.loc[mask, "amount_eur"] = 1000`.

```python
import warnings
import pandas as pd

df = pd.read_csv("../data/transactions.csv")

# BUG: "chained assignment" -- two [] in a row. df[mask] builds a temporary copy,
# the value is written into that copy, and the copy is thrown away.
with warnings.catch_warnings():
    warnings.simplefilter("ignore")          # pandas warns here (SettingWithCopyWarning)
    df[df["amount_eur"] > 1000]["amount_eur"] = 1000
print("max after buggy code:", df["amount_eur"].max())   # still above 1000

# FIX: one .loc call with [rows, column] writes into df itself
df.loc[df["amount_eur"] > 1000, "amount_eur"] = 1000
print("max after fix:", df["amount_eur"].max())
# (df["amount_eur"].clip(upper=1000) is another clean way)
```

#### 82. Rank swimmers inside each race. For the 2024 Pune Open, rank every OK swim within its `event` (1 = fastest), and print the podium (ranks 1 to 3) of each event, sorted by event and rank. (★★★)

`hint:` `groupby("event")["time_sec"].rank(method="min")`. `method="min"` gives tied swimmers the same (best) rank.

```python
import pandas as pd

res = pd.read_csv("../data/swim_results.csv").drop_duplicates()
res["event"] = res["event"].replace({"50 free": "50 Free"})
meet = res[(res["meet"] == "Pune Open") & (res["date"].str.startswith("2024")) & (res["status"] == "OK")].copy()

# rank inside each event; smallest time gets rank 1
meet["place"] = meet.groupby("event")["time_sec"].rank(method="min").astype(int)
podium = meet[meet["place"] <= 3].sort_values(["event", "place"])
print(podium[["event", "place", "swimmer_id", "time_sec"]])
```

#### 83. Spot the bug. This code is meant to show the number of frauds per channel, but the numbers look far too big. Find the mistake and fix it. (★★★)

```python
df.groupby("channel")["is_fraud"].count()
```

`hint:` Same trap as exercise 39, but inside a groupby. `count` counts rows; `sum` adds the 1s.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
print("buggy (count):")
print(df.groupby("channel")["is_fraud"].count())   # = number of transactions per channel
print("fixed (sum):")
print(df.groupby("channel")["is_fraud"].sum())     # = number of frauds per channel
# Tip: if your "number of frauds" equals the value_counts of the group, you used count.
print(df["channel"].value_counts())
```

#### 84. Rolling windows smooth a noisy line. Work out the total amount spent per day, then a 7-day rolling average of it. Print the first 10 days of both side by side. Why are the first 6 rolling values NaN? (★★★)

`hint:` `daily = df.set_index("timestamp").resample("D")["amount_eur"].sum()`, then `daily.rolling(7).mean()`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
daily = df.set_index("timestamp").resample("D")["amount_eur"].sum()

# rolling(7).mean(): average of this day and the 6 days before it
smooth = daily.rolling(7).mean()
out = pd.DataFrame({"daily": daily, "rolling_7d": smooth}).round(1)
print(out.head(10))
# The first 6 days do not have 7 days of history yet, so they are NaN.
```

#### 85. Add two "history" features per customer: `txn_number` (1 for their first transaction, 2 for the second ...) and `spent_so_far` (running total of their amounts, including this one). Sort by customer and time first. (★★★)

`hint:` `groupby("customer_id").cumcount() + 1` (cumcount starts at 0), and `groupby("customer_id")["amount_eur"].cumsum()`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values(["customer_id", "timestamp"])

df["txn_number"] = df.groupby("customer_id").cumcount() + 1       # 0,1,2.. -> 1,2,3..
df["spent_so_far"] = df.groupby("customer_id")["amount_eur"].cumsum()  # running total
print(df[["customer_id", "timestamp", "amount_eur", "txn_number", "spent_so_far"]].head(8))
```

#### 86. Who improved most at 100 Free? Using clean OK results sorted by date, find for each swimmer their FIRST 100 Free time and their BEST 100 Free time. Add `improvement = first - best` (seconds dropped) and print the top 5 improvers with their names. (★★★)

`hint:` After sorting by date: `groupby("swimmer_id")["time_sec"].agg(first="first", best="min")`. Then merge with swimmers for the names.

```python
import pandas as pd

res = pd.read_csv("../data/swim_results.csv").drop_duplicates()
swimmers = pd.read_csv("../data/swimmers.csv")
res["date"] = pd.to_datetime(res["date"])

free100 = res[(res["event"] == "100 Free") & (res["status"] == "OK")].sort_values("date")
# "first" takes the first row in each group, which is the earliest because we sorted
prog = free100.groupby("swimmer_id")["time_sec"].agg(first="first", best="min", races="count")
prog["improvement"] = prog["first"] - prog["best"]
prog = prog.reset_index().merge(swimmers[["swimmer_id", "name"]], on="swimmer_id")
print(prog.nlargest(5, "improvement").round(2))
```

#### 87. A personal best (PB) is a swimmer's fastest time so far in an event. For clean OK results, sorted by date, mark `is_pb = True` when a swim beats that swimmer's best time from all EARLIER races in the same event (a first-ever swim does not count). Which 5 swimmers set the most PBs? (★★★)

`hint:` Inside each (swimmer, event) group: `prev_best = transform(lambda s: s.cummin().shift())`. `cummin` = best so far, `shift` moves it down one row so it only uses earlier races.

```python
import pandas as pd

res = pd.read_csv("../data/swim_results.csv").drop_duplicates()
res["event"] = res["event"].replace({"50 free": "50 Free"})
res["date"] = pd.to_datetime(res["date"])
ok = res[res["status"] == "OK"].sort_values("date").copy()

g = ok.groupby(["swimmer_id", "event"])["time_sec"]
# cummin(): best time up to and INCLUDING this race; shift(): use only EARLIER races
ok["prev_best"] = g.transform(lambda s: s.cummin().shift())
ok["is_pb"] = ok["time_sec"] < ok["prev_best"]     # NaN prev_best -> False (first swim)

print(ok[["swimmer_id", "event", "date", "time_sec", "prev_best", "is_pb"]].head(6))
print(ok.groupby("swimmer_id")["is_pb"].sum().nlargest(5))
```

#### 88. Spot the bug. Below, a customers table accidentally contains 5 customers twice. After merging it onto the transactions, the row count goes UP. Show it, explain why, use `validate="many_to_one"` to catch it, and fix it. (★★★)

```python
import pandas as pd
df = pd.read_csv("../data/transactions.csv")
cust = pd.read_csv("../data/customers.csv")
cust_bad = pd.concat([cust, cust.head(5)])   # 5 customers appear twice
```

`hint:` If a key appears twice in the right table, every matching left row is copied twice. `validate="many_to_one"` raises a `MergeError` when the right keys are not unique. Fix with `drop_duplicates("customer_id")`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
cust = pd.read_csv("../data/customers.csv")
cust_bad = pd.concat([cust, cust.head(5)])   # 5 customers appear twice

bad = df.merge(cust_bad, on="customer_id", how="left")
print("transactions:", len(df), "after merge:", len(bad))   # more rows than we started with!

# validate= checks the key relationship and stops with an error if it is wrong
try:
    df.merge(cust_bad, on="customer_id", how="left", validate="many_to_one")
except pd.errors.MergeError as e:
    print("caught:", e)

fixed = df.merge(cust_bad.drop_duplicates("customer_id"), on="customer_id",
                 how="left", validate="many_to_one")
print("after fix:", len(fixed))
```

#### 89. Why is this misleading? A report says "the average fraud rate across our countries is X%", computed as the mean of the per-country fraud rates. Compute that number, the true overall fraud rate, and explain why they differ so much. (★★★)

`hint:` Compare `df.groupby("country")["is_fraud"].mean().mean()` with `df["is_fraud"].mean()`. Think about how many transactions each country has.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
by_country = df.groupby("country")["is_fraud"].agg(["mean", "count"])
avg_of_avgs = by_country["mean"].mean()
overall = df["is_fraud"].mean()
print(by_country.round(4))
print("average of country rates:", round(avg_of_avgs * 100, 2), "%")
print("true overall rate:       ", round(overall * 100, 2), "%")
# Average of averages gives RU (63 rows) the same weight as NL (4,945 rows).
# Weighting each rate by its count gets back the true rate:
weighted = (by_country["mean"] * by_country["count"]).sum() / by_country["count"].sum()
print("weighted average:        ", round(weighted * 100, 2), "%")
```

#### 90. Method chaining means writing steps one after another, joined by dots, without saving in-between tables. Rewrite this as ONE chain, using `.assign` (adds a column and returns the table) and `.query` (filters with a text condition): (★★★)

```python
df = pd.read_csv("../data/transactions.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["hour"] = df["timestamp"].dt.hour
online = df[df["channel"] == "online"]
out = online.groupby("hour")["is_fraud"].mean().sort_values(ascending=False).head(3)
```

`hint:` `.assign(hour=lambda d: d["timestamp"].dt.hour)` (the `d` is the table at that point in the chain), and `.query("channel == 'online'")`. Wrap the chain in round brackets so you can put one step per line.

```python
import pandas as pd

out = (
    pd.read_csv("../data/transactions.csv")
    .assign(timestamp=lambda d: pd.to_datetime(d["timestamp"]))
    .assign(hour=lambda d: d["timestamp"].dt.hour)   # d = the table so far
    .query("channel == 'online'")                     # text condition, same as a mask
    .groupby("hour")["is_fraud"].mean()
    .sort_values(ascending=False)
    .head(3)
)
print(out.round(3))
```

#### 91. Reshaping. Make a WIDE table of best 50 Back time per swimmer (rows) per year (columns 2024, 2025) for clean OK results. Then turn it back into a LONG table (one row per swimmer per year) with `melt`. Print the head of both. (★★★)

`hint:` Wide: `pivot_table(index="swimmer_id", columns="year", values="time_sec", aggfunc="min")`. Long: `wide.reset_index().melt(id_vars="swimmer_id", var_name="year", value_name="best_time")`.

```python
import pandas as pd

res = pd.read_csv("../data/swim_results.csv").drop_duplicates()
back = res[(res["event"] == "50 Back") & (res["status"] == "OK")].copy()
back["year"] = back["date"].str[:4]          # first 4 characters of the date text

wide = back.pivot_table(index="swimmer_id", columns="year", values="time_sec", aggfunc="min")
print(wide.head())          # one row per swimmer, one column per year

# melt does the opposite: column names become values in a "year" column
long = wide.reset_index().melt(id_vars="swimmer_id", var_name="year", value_name="best_time")
print(long.sort_values("swimmer_id").head(6))
print(wide.shape, "->", long.shape)
```

#### 92. Build a customer-level table (one row per customer) from the transactions with: `n_txn`, `total_eur`, `avg_eur`, `max_eur`, `share_online` (fraction of their transactions that are online), `n_countries` (distinct countries), and `had_fraud` (1 if any of their transactions is fraud). Print the shape and head. (★★★)

`hint:` Make an 0/1 `is_online` column first, then one named `.agg` with `("is_online", "mean")`, `("country", "nunique")` and `("is_fraud", "max")`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
df["is_online"] = (df["channel"] == "online").astype(int)

per_cust = df.groupby("customer_id").agg(
    n_txn=("transaction_id", "count"),
    total_eur=("amount_eur", "sum"),
    avg_eur=("amount_eur", "mean"),
    max_eur=("amount_eur", "max"),
    share_online=("is_online", "mean"),     # mean of 0/1 = share
    n_countries=("country", "nunique"),
    had_fraud=("is_fraud", "max"),          # max of 0/1 = 1 if ANY row is 1
).reset_index()
print(per_cust.shape)
print(per_cust.head().round(2))
```

#### 93. Join the customer-level table from exercise 92 to a CLEANED customers table (age -1 replaced by the median real age, plus `account_age_days` on 2025-03-31). Use `validate="one_to_one"` and check: 800 rows, no missing values. Then compare the average features of customers with and without fraud. (★★★)

`hint:` Rebuild both tables, merge on `customer_id` with `validate="one_to_one"`, check `isna().sum().sum()`, then `groupby("had_fraud").mean(numeric_only=True)`.

```python
import numpy as np
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
df["is_online"] = (df["channel"] == "online").astype(int)
per_cust = df.groupby("customer_id").agg(
    n_txn=("transaction_id", "count"), avg_eur=("amount_eur", "mean"),
    share_online=("is_online", "mean"), had_fraud=("is_fraud", "max"),
).reset_index()

cust = pd.read_csv("../data/customers.csv")
cust["age"] = cust["age"].replace(-1, np.nan)
cust["age"] = cust["age"].fillna(cust["age"].median())
cust["account_open_date"] = pd.to_datetime(cust["account_open_date"])
cust["account_age_days"] = (pd.Timestamp("2025-03-31") - cust["account_open_date"]).dt.days

table = cust.merge(per_cust, on="customer_id", how="left", validate="one_to_one")
print("shape:", table.shape)
print("missing values:", table.isna().sum().sum())
cols = ["age", "credit_limit_eur", "account_age_days", "n_txn", "avg_eur", "share_online"]
print(table.groupby("had_fraud")[cols].mean().round(2).to_string())  # to_string shows every column
```

#### 94. Models need numbers, not text. One-hot encoding turns a text column into several 0/1 columns, one per value. Use `pd.get_dummies` on the transactions for `channel` and `merchant_category` (missing filled as `"unknown"`), and print the new column names and the shape. (★★★)

`hint:` `pd.get_dummies(df, columns=["channel", "merchant_category"], dtype=int)`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
df["merchant_category"] = df["merchant_category"].fillna("unknown")
# each distinct value becomes its own 0/1 column, e.g. channel_online
encoded = pd.get_dummies(df, columns=["channel", "merchant_category"], dtype=int)
print(encoded.shape)
print([c for c in encoded.columns if c.startswith(("channel_", "merchant_category_"))])
print(encoded.filter(like="channel_").head(3))
```

#### 95. Build a model-ready table for fraud detection. Write a function `make_features(path)` that returns `X` (features) and `y` (the `is_fraud` target). Features: `amount_eur`, `hour`, `is_night`, `is_foreign`, `amount_ratio` (vs customer average), `n_txn`, `hours_since_prev` (fill the first transaction with -1), plus one-hot `channel` columns. Check `X` has no missing values and print its shape, the fraud rate of `y`, and `X.head()`. (★★★)

`hint:` Put the steps from exercises 77–80 and 94 inside one function. At the end: `y = df["is_fraud"]`, `X = df[feature_list]`, `return X, y`.

```python
import pandas as pd

def make_features(path):
    df = pd.read_csv(path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values(["customer_id", "timestamp"])

    df["hour"] = df["timestamp"].dt.hour
    df["is_night"] = df["hour"].between(0, 5).astype(int)
    df["is_foreign"] = (df["country"] != "NL").astype(int)
    g = df.groupby("customer_id")
    df["amount_ratio"] = df["amount_eur"] / g["amount_eur"].transform("mean")
    df["n_txn"] = g["transaction_id"].transform("count")
    gap = g["timestamp"].diff().dt.total_seconds() / 3600
    df["hours_since_prev"] = gap.fillna(-1)       # -1 = "no earlier transaction"

    df = pd.get_dummies(df, columns=["channel"], dtype=int)
    features = ["amount_eur", "hour", "is_night", "is_foreign", "amount_ratio",
                "n_txn", "hours_since_prev"] + [c for c in df.columns if c.startswith("channel_")]
    return df[features], df["is_fraud"]

X, y = make_features("../data/transactions.csv")
print("X shape:", X.shape)
print("missing in X:", X.isna().sum().sum())
print("fraud rate in y:", round(y.mean(), 4))
print(X.head().round(2))
```

#### 96. Why is this misleading? Someone adds a feature `cust_fraud_rate` = the customer's fraud rate over ALL their transactions, and says it predicts fraud almost perfectly. Show how strong it looks, explain the problem (this is called "target leakage"), and build an honest version that only uses the customer's EARLIER transactions. (★★★)

`hint:` The feature is made from `is_fraud` itself, including the current row. Honest version: sort by time, then per customer `cumsum()` of `is_fraud` minus the current row (or `.shift()` then `cumsum`) = frauds seen BEFORE this transaction.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values(["customer_id", "timestamp"])

# LEAKY: uses the answer (is_fraud) of this very row, and of FUTURE rows
df["cust_fraud_rate"] = df.groupby("customer_id")["is_fraud"].transform("mean")
print("leaky feature, mean value by class:")
print(df.groupby("is_fraud")["cust_fraud_rate"].mean().round(3))
print("fraud rate when leaky feature is 0:", df.loc[df["cust_fraud_rate"] == 0, "is_fraud"].mean())
# When it is 0 there is NEVER fraud -- by construction. At prediction time we
# do not know is_fraud yet, so this feature cannot exist in real life.

# HONEST: frauds seen BEFORE this transaction (cumsum includes this row, so subtract it)
df["past_frauds"] = df.groupby("customer_id")["is_fraud"].cumsum() - df["is_fraud"]
print("honest feature, mean value by class:")
print(df.groupby("is_fraud")["past_frauds"].mean().round(3))
```

#### 97. Why is this misleading? A model that says "never fraud" for every transaction gets very high accuracy. Compute its accuracy with pandas. Then test a simple rule, "fraud if night AND foreign, OR amount above 500", and compute its accuracy, precision (of the flagged, how many are fraud) and recall (of the frauds, how many were flagged). (★★★)

`hint:` Accuracy = `(pred == y).mean()`. Precision = `(pred & y).sum() / pred.sum()`. Recall = `(pred & y).sum() / y.sum()`. Use booleans for `pred` and `y`.

```python
import pandas as pd

df = pd.read_csv("../data/transactions.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
y = df["is_fraud"] == 1

never = pd.Series(False, index=df.index)          # predict "not fraud" for everyone
print("'never fraud' accuracy:", round((never == y).mean(), 4))  # ~98%, yet catches 0 frauds

night = df["timestamp"].dt.hour.between(0, 5)
foreign = df["country"] != "NL"
pred = (night & foreign) | (df["amount_eur"] > 500)

caught = (pred & y).sum()                         # true positives
print("rule accuracy: ", round((pred == y).mean(), 4))
print("rule precision:", round(caught / pred.sum(), 3))
print("rule recall:   ", round(caught / y.sum(), 3))
# The rule has LOWER accuracy than "never fraud", yet it is the only one that catches
# any fraud (about 1 in 6). With rare fraud, accuracy hides everything;
# precision and recall tell the real story.
```

#### 98. Spot the bug. These meet dates are stored as text in day/month/year form. The code finds the "latest" meet and sorts by date, but both answers are wrong. Why? Fix it. (★★★)

```python
import pandas as pd
meets = pd.DataFrame({"meet": ["Winter", "Spring", "Summer", "Diwali"],
                      "date": ["20/01/2025", "15/03/2025", "10/05/2025", "26/10/2024"]})
print(meets["date"].max())
print(meets.sort_values("date"))
```

`hint:` Text is compared letter by letter, so `"26/..."` beats `"20/..."` regardless of year. Convert with `pd.to_datetime(meets["date"], format="%d/%m/%Y")`.

```python
import pandas as pd

meets = pd.DataFrame({"meet": ["Winter", "Spring", "Summer", "Diwali"],
                      "date": ["20/01/2025", "15/03/2025", "10/05/2025", "26/10/2024"]})
print("buggy max:", meets["date"].max())   # "26/10/2024": text compares the day first!
print(meets.sort_values("date"))           # sorted by day number, not by real date

# FIX: tell pandas the format, so 20/01 is read as 20 January (not month 20)
meets["date"] = pd.to_datetime(meets["date"], format="%d/%m/%Y")
print("fixed max:", meets["date"].max().date())
print(meets.sort_values("date"))
```

#### 99. A full swim season report in one script. From the raw files: drop duplicates, clean `event` and `stroke`, drop DQ swims, find each swimmer's best time per event, merge in `name` and `gender`, rank swimmers within each (event, gender) by best time, and print the top 3 per event and gender for the 50 m events only. (★★★)

`hint:` Steps you already know: `drop_duplicates`, `replace`, `.str.strip().str.title()`, filter OK, `groupby([...]).min().reset_index()`, merge, `groupby(["event", "gender"])["best"].rank(method="min")`. Filter 50 m events with `.str.startswith("50 ")`.

```python
import pandas as pd

res = pd.read_csv("../data/swim_results.csv")
swimmers = pd.read_csv("../data/swimmers.csv")

res = res.drop_duplicates()
res["event"] = res["event"].replace({"50 free": "50 Free"})
res["stroke"] = res["stroke"].str.strip().str.title()
ok = res[res["status"] == "OK"]

best = (ok.groupby(["swimmer_id", "event"])["time_sec"].min()
          .reset_index(name="best"))
best = best.merge(swimmers[["swimmer_id", "name", "gender"]], on="swimmer_id",
                  how="left", validate="many_to_one")
best["rank"] = best.groupby(["event", "gender"])["best"].rank(method="min").astype(int)

top = best[(best["rank"] <= 3) & best["event"].str.startswith("50 ")]
print(top.sort_values(["event", "gender", "rank"])[["event", "gender", "rank", "name", "best"]]
         .to_string(index=False))
```

#### 100. Capstone. Write a function `fraud_report(path)` that loads the transactions, adds `is_night`, `is_foreign` and `amount_ratio`, assigns each transaction a `risk_group`: `"high"` if (night and foreign) or amount_ratio > 3, `"medium"` if night or foreign, else `"low"`. It should save the table with these columns to `outputs/transactions_features.csv` and return a summary per risk group: number of transactions, number of frauds, fraud rate, and share of ALL frauds caught in that group. Print the summary. (★★★)

`hint:` Use `np.select([cond_high, cond_medium], ["high", "medium"], default="low")` for the groups (conditions are checked in order). Share of frauds = `n_fraud / n_fraud.sum()`.

```python
import os
import numpy as np
import pandas as pd

def fraud_report(path):
    df = pd.read_csv(path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["is_night"] = df["timestamp"].dt.hour.between(0, 5).astype(int)
    df["is_foreign"] = (df["country"] != "NL").astype(int)
    df["amount_ratio"] = df["amount_eur"] / df.groupby("customer_id")["amount_eur"].transform("mean")

    high = ((df["is_night"] == 1) & (df["is_foreign"] == 1)) | (df["amount_ratio"] > 3)
    medium = (df["is_night"] == 1) | (df["is_foreign"] == 1)
    # np.select checks the conditions in order: the first True one wins
    df["risk_group"] = np.select([high, medium], ["high", "medium"], default="low")

    os.makedirs("outputs", exist_ok=True)
    df.to_csv("outputs/transactions_features.csv", index=False)

    summary = df.groupby("risk_group").agg(
        n_txn=("transaction_id", "count"),
        n_fraud=("is_fraud", "sum"),
        fraud_rate=("is_fraud", "mean"),
    )
    summary["share_of_all_frauds"] = summary["n_fraud"] / summary["n_fraud"].sum()
    return summary.loc[["high", "medium", "low"]]

print(fraud_report("../data/transactions.csv").round(3))
```
