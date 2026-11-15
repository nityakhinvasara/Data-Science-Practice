# pandas: 100 exercises (hints)

_Generated from `tools/source/pandas.ktx`. Don't edit this file; it gets rebuilt._


## Level 1: Easy

#### 1. Import pandas with its usual short name `pd` and print the version number. (★☆☆)

`hint:` `import pandas as pd`, then `pd.__version__` (two underscores on each side).

#### 2. A Series is one labelled column of data. Make a Series of five 50 m freestyle times, with the swimmers' names as the index (the labels), and print it. (★☆☆)

```python
times = [31.2, 29.8, 30.5, 32.1, 30.0]
names = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]
```

`hint:` `pd.Series(values, index=labels)`

#### 3. Using the Series from exercise 2, print (a) Diya's time, (b) the fastest time, and (c) the name of the fastest swimmer. (★☆☆)

```python
import pandas as pd
s = pd.Series([31.2, 29.8, 30.5, 32.1, 30.0], index=["Aarav", "Diya", "Kabir", "Meera", "Rohan"])
```

`hint:` `s["Diya"]`, `s.min()`, and `s.idxmin()` (gives the label of the smallest value).

#### 4. A DataFrame is a table: several Series side by side that share one index. Build this DataFrame from a dictionary (each key becomes a column) and print it. (★☆☆)

| name | subject | marks |
|---|---|---|
| Asha | Python | 78 |
| Bilal | Statistics | 64 |
| Chetan | Python | 91 |
| Divya | Databases | 55 |

`hint:` `pd.DataFrame({"name": [...], "subject": [...], "marks": [...]})`

#### 5. Now build a DataFrame from a list of rows (a list of lists). Use these three card transactions and name the columns `transaction_id`, `amount_eur`, `channel`. Print it. (★☆☆)

```python
rows = [["T1", 12.50, "in_store"], ["T2", 230.00, "online"], ["T3", 4.20, "contactless"]]
```

`hint:` `pd.DataFrame(rows, columns=[...])`. Each inner list is one row.

#### 6. Load `../data/transactions.csv` into a DataFrame called `df` and print the first 5 rows. (★☆☆)

`hint:` `pd.read_csv(path)` then `df.head()`.

#### 7. For the transactions file, print the last 3 rows, then print how many rows and columns it has. (★☆☆)

`hint:` `df.tail(3)` and `df.shape` (no brackets after shape: it is an attribute, not a function).

#### 8. Print the data type (dtype) of every column in the transactions file. Which column holds dates and times, and what type did pandas give it? (★☆☆)

`hint:` `df.dtypes`. `object` means "text" here.

#### 9. Load `../data/swim_results.csv` and call `.info()`. Use the output to answer: how many rows are there, and how many `time_sec` values are filled in (non-null)? (★☆☆)

`hint:` `.info()` prints its own table, so just call it (no `print` needed). Compare "Non-Null Count" for time_sec with the total rows.

#### 10. Use `.describe()` on the `amount_eur` column of the transactions. Then print just the mean and the maximum on their own lines. Is the mean bigger or smaller than the median (50%)? What does that tell you? (★☆☆)

`hint:` `df["amount_eur"].describe()`, `.mean()`, `.max()`, `.median()`.

#### 11. From the transactions, select (a) only the `channel` column and (b) the two columns `customer_id` and `amount_eur`. Print the `type()` of each result. Why are they different? (★☆☆)

`hint:` One name in single brackets `df["channel"]` gives a Series. A list of names, so double brackets `df[["a", "b"]]`, gives a DataFrame.

#### 12. How many transactions came through each channel? Then show the same as shares (fractions that add up to 1). (★☆☆)

`hint:` `df["channel"].value_counts()` and `value_counts(normalize=True)`.

#### 13. In the transactions: how many different countries appear, what are they, and which 3 countries have the most transactions? (★☆☆)

`hint:` `.nunique()` counts distinct values, `.unique()` lists them, `.value_counts().head(3)` gives the top 3.

#### 14. Load `../data/customers.csv`, make `customer_id` the index, and use `.loc` to print the full row for customer `C0005`. Then print only that customer's `segment`. (★☆☆)

`hint:` `cust = cust.set_index("customer_id")`, then `cust.loc["C0005"]` and `cust.loc["C0005", "segment"]`.

#### 15. Use `.iloc` (lookup by position, counting from 0) on the transactions to print: the first row, rows at positions 10 to 14, and the very last row. (★☆☆)

`hint:` `df.iloc[0]`, `df.iloc[10:15]` (the end is not included), `df.iloc[-1]`.

#### 16. On the customers file (default number index 0, 1, 2 ...), compare `cust.loc[0:4, ["age", "segment"]]` with `cust.iloc[0:4, [1, 5]]`. How many rows does each give, and why? (★☆☆)

`hint:` `.loc` slices by label and INCLUDES the end label. `.iloc` slices by position and EXCLUDES the end, like Python.

#### 17. Keep only the transactions above 500 EUR. How many are there? Print the first 5 of them. (★☆☆)

`hint:` Make a mask (a column of True/False): `mask = df["amount_eur"] > 500`, then `df[mask]`.

#### 18. Find transactions that are online AND above 200 EUR. How many are there? (★☆☆)

`hint:` Join two masks with `&`. Put each condition in its own round brackets: `(cond1) & (cond2)`.

#### 19. Count transactions from Nigeria (`NG`) OR Russia (`RU`) in two ways: once with `|`, and once with `.isin()`. Then use `.isin()` to count transactions from NG, RU or US. (★☆☆)

`hint:` `(df["country"] == "NG") | (df["country"] == "RU")` and `df["country"].isin(["NG", "RU"])`.

#### 20. How many customers are aged 18 to 25, including both 18 and 25? (★☆☆)

`hint:` `cust["age"].between(18, 25)` includes both ends by default.

#### 21. How many transactions happened outside the Netherlands? Use `~` to flip a mask. (★☆☆)

`hint:` `~(df["country"] == "NL")` turns every True into False and back. (`!=` also works.)

#### 22. Show the 5 biggest transactions, biggest first. Do it with `sort_values` and again with `nlargest`. (★☆☆)

`hint:` `df.sort_values("amount_eur", ascending=False).head(5)` and `df.nlargest(5, "amount_eur")`.

#### 23. Sort the swim results by `event` (A to Z) and, inside each event, by `time_sec` (fastest first). Print the first 8 rows of `event`, `swimmer_id`, `time_sec`. (★☆☆)

`hint:` Pass a list to `sort_values`: `sort_values(["event", "time_sec"])`.

#### 24. Add a column `amount_inr` to the transactions: the amount in Indian rupees, using 1 EUR = 95 INR. Print `amount_eur` and `amount_inr` for the first 5 rows. (★☆☆)

`hint:` `df["amount_inr"] = df["amount_eur"] * 95`. The maths happens on every row at once.

#### 25. Load `../data/swimmers.csv` and rename `name` to `swimmer_name` and `club` to `team`. Print the column names. (★☆☆)

`hint:` `swimmers.rename(columns={"old": "new", ...})` returns a NEW table, so save it.

#### 26. From the swimmers table, drop the `coach` and `joined_date` columns. Print the shape before and after. (★☆☆)

`hint:` `swimmers.drop(columns=["coach", "joined_date"])`.

#### 27. In the swim results, add a column `speed_mps` = distance in metres divided by time in seconds. Print the 5 fastest swims by speed (show `swimmer_id`, `event`, `time_sec`, `speed_mps`). Why can't we just compare `time_sec` across events? (★☆☆)

`hint:` Divide one column by another: `res["distance_m"] / res["time_sec"]`. Then `nlargest(5, "speed_mps")`.

#### 28. How many missing values (NaN) does each column have in the swim results? And in the transactions? (★☆☆)

`hint:` `.isna()` gives True where a value is missing; `.isna().sum()` counts the Trues per column.

#### 29. Look at the swim results where `time_sec` is missing. What is their `status`? Does that make sense? (★☆☆)

`hint:` Filter with `res[res["time_sec"].isna()]`, then `value_counts()` on `status`.

#### 30. In the transactions, fill the missing `merchant_category` values with the word `"unknown"`. Check with `value_counts()` that `unknown` now appears 30 times and nothing is missing. (★☆☆)

`hint:` `df["merchant_category"] = df["merchant_category"].fillna("unknown")`.

#### 31. Load `../data/student_marks.csv`. Drop the rows where `sleep_hours` is missing. Print the shape before and after. (★☆☆)

`hint:` `marks.dropna(subset=["sleep_hours"])`. `subset` means "only look at these columns".

#### 32. Instead of dropping, fill the missing `sleep_hours` with the median sleep. Print the median you used and the number still missing. (★☆☆)

`hint:` Work out `med = marks["sleep_hours"].median()` first, then `fillna(med)`.

#### 33. How many rows in the swim results are exact duplicates of an earlier row? Print all copies of those rows (both the original and the duplicate) sorted by `result_id`. (★☆☆)

`hint:` `res.duplicated().sum()`. To see every copy use `res[res.duplicated(keep=False)]`.

#### 34. Remove the duplicate rows from the swim results and save the result as `res`. Print the number of rows before and after. (★☆☆)

`hint:` `res = res.drop_duplicates()`.

#### 35. The `event` column is messy: `value_counts()` shows both `"50 Free"` and `"50 free"`. Someone suggests `res["event"].str.title()` to fix it. Try it and look at `value_counts()`. What goes wrong? Then fix only the bad value instead. (★☆☆)

`hint:` `"200 IM".title()` gives `"200 Im"`. Use `res["event"].replace({"50 free": "50 Free"})` instead.

#### 36. The `stroke` column has a messy value `" freestyle "` (spaces around it, lower case). Clean the whole column with `.str.strip()` and `.str.title()` so it matches `"Freestyle"`. Check with `value_counts()`. (★☆☆)

`hint:` `.str` lets you use string methods on every value: `res["stroke"].str.strip().str.title()`.

#### 37. Split the cleaned `event` column (e.g. `"100 Back"`) into two new columns: `dist_text` (`"100"`) and `stroke_code` (`"Back"`). Then turn `dist_text` into a number and check it always equals `distance_m`. (★☆☆)

`hint:` `res["event"].str.split(" ", n=1, expand=True)` gives two columns (0 and 1). Turn text into numbers with `.astype(int)`.

#### 38. In the transactions, convert `is_fraud` to `bool` (True/False) and `channel` to the `category` type. Print the dtypes of those two columns. (A category column stores each distinct text value only once, which saves memory.) (★☆☆)

`hint:` `df["is_fraud"].astype(bool)` and `df["channel"].astype("category")`.

#### 39. A classic trap. Your friend wants the number of fraud transactions and writes `df["is_fraud"].count()`. Run it, then run `df["is_fraud"].sum()` and `df["is_fraud"].mean()`. Which one answers the question, and what do the other two mean? (★☆☆)

`hint:` `count()` counts filled-in cells (any value, even 0). `sum()` adds the values, and since fraud = 1, it counts frauds.

#### 40. Without filtering into a new table, answer with one line each: (a) how many transactions are above 1,000 EUR, (b) what fraction of transactions are online, (c) how many swim results were disqualified (`status == "DQ"`). (★☆☆)

`hint:` A True/False column behaves like 1/0: `.sum()` counts the Trues, `.mean()` gives the fraction.


## Level 2: Medium

#### 41. `groupby` splits a table into groups, does a calculation on each group, and joins the answers. What is the average transaction amount for each channel? (★★☆)

`hint:` `df.groupby("channel")["amount_eur"].mean()`. Read it as: "group by channel, take amount, average it".

#### 42. How many transactions are there per `merchant_category`? Compare `groupby("merchant_category").size()` with `value_counts(dropna=False)`. Where did the 30 missing categories go in the groupby result, and how do you keep them? (★★☆)

`hint:` `groupby` leaves out NaN groups unless you pass `dropna=False`.

#### 43. What is the fraud rate (share of frauds) for each channel? Show it as a percentage with 2 decimals, highest first. (★★☆)

`hint:` The mean of a 0/1 column is the rate: `df.groupby("channel")["is_fraud"].mean()`, then `* 100`, `.round(2)`, `.sort_values(ascending=False)`.

#### 44. Show, for each country, the fraud rate AND the number of transactions, in one table. Why should you look at the count before trusting a country's rate? (★★☆)

`hint:` Pass a list to `.agg`: `df.groupby("country")["is_fraud"].agg(["mean", "count"])`.

#### 45. Which merchant categories have the highest fraud rate? Print all categories, highest rate first, as percentages with 1 decimal. (★★☆)

`hint:` Same pattern as exercise 43, grouped by `merchant_category`.

#### 46. For each channel, show the min, max, mean and median transaction amount in one table. (★★☆)

`hint:` `.agg(["min", "max", "mean", "median"])` on the grouped `amount_eur` column.

#### 47. Build one summary table per country with clear column names: `n_txn` (number of transactions), `n_fraud` (number of frauds), `fraud_rate`, and `avg_amount`. Sort by `fraud_rate`, highest first. (★★☆)

`hint:` Named aggregation: `.agg(new_name=("column", "function"), ...)`. For example `n_fraud=("is_fraud", "sum")`.

#### 48. Do fraud transactions have bigger amounts? Group by both `channel` and `is_fraud`, take the mean amount, and then use `.unstack()` to turn `is_fraud` into columns so it reads like a small table. (★★☆)

`hint:` `df.groupby(["channel", "is_fraud"])["amount_eur"].mean().unstack()`. `unstack` moves the last index level into the columns.

#### 49. Find each swimmer's best (fastest) time in each event. First clean the data: drop duplicates, fix `"50 free"`, and keep only `status == "OK"`. Print the first 10 rows as a normal table (not an index). (★★☆)

`hint:` `groupby(["swimmer_id", "event"])["time_sec"].min()`, then `.reset_index()` turns the group labels back into columns.

#### 50. Which 5 swimmers swam the most races (after dropping duplicates)? Also show how many different meets each of those swimmers attended. Remember the same meet name happens in different years, so count distinct dates. (★★☆)

`hint:` `.agg(races=("result_id", "count"), meets=("date", "nunique"))`, then `nlargest(5, "races")`.

#### 51. Who holds the fastest time in each event? Use `idxmin` to find the row number of the fastest swim per event, then use `.loc` to pull those rows. Show `event`, `swimmer_id`, `time_sec`, `meet`. (★★☆)

`hint:` `rows = ok.groupby("event")["time_sec"].idxmin()` gives index labels; then `ok.loc[rows, [...]]`.

#### 52. Using the student marks: (a) what is the average `final_marks` for students with and without a part-time job? (b) what is the pass rate per `favourite_subject`, highest first? (★★☆)

`hint:` Two separate groupbys: by `part_time_job` (mean of final_marks) and by `favourite_subject` (mean of passed).

#### 53. `merge` joins two tables on a shared key column. Join the swim results with the swimmers table on `swimmer_id` (keep every result: `how="left"`). Print the shape before and after, and the first 3 rows with `name`, `club`, `event`, `time_sec`. (★★☆)

`hint:` `res.merge(swimmers, on="swimmer_id", how="left")`. Each result row gets that swimmer's details added.

#### 54. Join the transactions with the customers and find the fraud rate for each customer `segment` (student / standard / premium). (★★☆)

`hint:` Merge on `customer_id`, then `groupby("segment")["is_fraud"].mean()`.

#### 55. See what each `how=` option does. Merge the two small tables below with `how="inner"`, `"left"`, `"right"` and `"outer"`, and print each result. Which swimmer or result disappears in each case? (★★☆)

```python
import pandas as pd
people = pd.DataFrame({"swimmer_id": ["S1", "S2", "S3"], "name": ["Asha", "Bilal", "Chetan"]})
races = pd.DataFrame({"swimmer_id": ["S1", "S1", "S2", "S9"], "time_sec": [31.0, 30.2, 33.5, 29.9]})
```

`hint:` inner = only keys in both; left = all of the left table; right = all of the right table; outer = everything. Missing partners become NaN.

#### 56. Which swimmers have NEVER swum the 50 Fly? Merge the swimmers table with the 50 Fly results using `how="left"` and `indicator=True`, then keep the rows marked `left_only`. Print how many and their names. (★★☆)

`hint:` `indicator=True` adds a `_merge` column saying `both`, `left_only` or `right_only`. Use only one row per swimmer from the results (`drop_duplicates("swimmer_id")`) so the merge does not repeat swimmers.

#### 57. Sometimes the key column has a different name in each table. Below, the customers table calls it `cust_id`. Merge the transactions with it using `left_on` and `right_on`, and print the first 3 rows of `customer_id`, `cust_id`, `segment`. (★★☆)

```python
import pandas as pd
df = pd.read_csv("../data/transactions.csv")
cust = pd.read_csv("../data/customers.csv").rename(columns={"customer_id": "cust_id"})
```

`hint:` `df.merge(cust, left_on="customer_id", right_on="cust_id", how="left")`. Both key columns are kept.

#### 58. `concat` stacks tables on top of each other. Split the swim results into a 2024 table and a 2025 table (use the `date` text: it starts with the year), then stack them back with `pd.concat`. Check the row count matches the original. What does `ignore_index=True` change? (★★☆)

`hint:` `res[res["date"].str.startswith("2024")]`, then `pd.concat([a, b], ignore_index=True)`.

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

#### 60. A pivot table is a groupby shown as a grid. Make a table of fraud rate (%) with channels as rows and countries as columns. (★★☆)

`hint:` `df.pivot_table(index="channel", columns="country", values="is_fraud", aggfunc="mean")`.

#### 61. Make a pivot table of the total amount spent (sum of `amount_eur`) per `merchant_category` (rows) and `channel` (columns), with row and column totals. (★★☆)

`hint:` `aggfunc="sum"` and `margins=True` adds an "All" row and column with totals.

#### 62. `pd.crosstab` counts how often each pair of values appears. Count transactions by `channel` and `is_fraud`. Then show it with `normalize="index"` so each row adds up to 1. (★★☆)

`hint:` `pd.crosstab(df["channel"], df["is_fraud"])` and add `normalize="index"`.

#### 63. How many boys and girls does each club have? Use `pd.crosstab` on the swimmers table with `club` as rows and `gender` as columns, plus totals. (★★☆)

`hint:` `pd.crosstab(swimmers["club"], swimmers["gender"], margins=True)`.

#### 64. Which club is fastest at 50 Free? Clean the results (drop duplicates, fix `"50 free"`, OK only), keep 50 Free, merge with swimmers, and make a pivot table of the best (minimum) time with `club` as rows and `gender` as columns. (★★☆)

`hint:` Filter, merge, then `pivot_table(index="club", columns="gender", values="time_sec", aggfunc="min")`.

#### 65. Convert the transaction `timestamp` column from text to real dates with `pd.to_datetime`. Print its new dtype, the first and last timestamp, and how many days the data covers. (★★☆)

`hint:` `df["timestamp"] = pd.to_datetime(df["timestamp"])`. Subtracting two dates gives a Timedelta with `.days`.

#### 66. Add two columns: `hour` (0–23) and `weekday` (e.g. "Monday"). How many transactions happen at each hour? (★★☆)

`hint:` After `to_datetime`, use `.dt.hour` and `.dt.day_name()`. Then `value_counts().sort_index()` to list hours in order.

#### 67. What is the fraud rate per hour of the day? Print the 5 riskiest hours. (★★☆)

`hint:` Make the `hour` column, then `groupby("hour")["is_fraud"].mean()` and `nlargest(5)`.

#### 68. For each month (January, February, March), show the number of transactions and the total amount. (★★☆)

`hint:` `df["month"] = df["timestamp"].dt.month`, then named agg with `("transaction_id", "count")` and `("amount_eur", "sum")`.

#### 69. Count transactions per week using `resample`. `resample("W")` groups rows by calendar week, but it needs the dates as the index. (★★☆)

`hint:` `df.set_index("timestamp").resample("W").size()`.

#### 70. How old is each customer's account on 2025-03-31? Add a column `account_age_days` to the customers table and print its min, mean and max. (★★☆)

`hint:` Convert `account_open_date` with `pd.to_datetime`, then `(pd.Timestamp("2025-03-31") - cust["account_open_date"]).dt.days`.

#### 71. `.map` replaces each value using a dictionary. Add a column `region` to the transactions: NL, DE, BE and FR are `"EU"`, everything else is `"non-EU"`. Then show the fraud rate per region. (★★☆)

`hint:` `df["country"].map(lookup)`. Any country missing from the dict becomes NaN, so fill those with `"non-EU"`.

#### 72. Write a function `size_label(amount)` that returns `"small"` below 20 EUR, `"medium"` from 20 up to (not including) 200, and `"large"` from 200. Use `.apply` to make a column `size` and print its counts. (★★☆)

`hint:` A normal `def` with `if / elif / else`, then `df["amount_eur"].apply(size_label)` (pass the function name, no brackets).

#### 73. `pd.cut` puts numbers into ranges (bins) you choose. Cut `amount_eur` into the bins 0–20, 20–50, 50–100, 100–500, 500 and more, and print the number of transactions and the fraud rate per bin. (★★☆)

`hint:` `pd.cut(df["amount_eur"], bins=[0, 20, 50, 100, 500, float("inf")])`. Group by the new column with `observed=True`.

#### 74. `pd.qcut` makes bins with (about) the same NUMBER of rows in each. Split the students into 4 equal groups by `study_hours_per_week`, labelled `"Q1"` to `"Q4"`, and print the average `final_marks` per group. (★★☆)

`hint:` `pd.qcut(marks["study_hours_per_week"], q=4, labels=["Q1", "Q2", "Q3", "Q4"])`.

#### 75. Make your first chart: a bar chart of the fraud rate (%) per channel. Give it a title and a y-axis label, save it to `outputs/fraud_by_channel.png`, and show it. (★★☆)

`hint:` `rate.plot(kind="bar")` returns an `ax` you can label: `ax.set_title(...)`, `ax.set_ylabel(...)`. Then `plt.savefig(...)` and `plt.show()`.


## Level 3: Hard

#### 76. Some customers have `age = -1`, a data-entry error. Count them, compare the average age with and without them, replace -1 with `NaN` (missing), and fill those with the median age of real values. Why replace with NaN first instead of filling directly? (★★★)

`hint:` `cust["age"].replace(-1, np.nan)` (import numpy as np). Then `median()` skips NaN automatically.

#### 77. Feature engineering means making new columns that help a model. Add a column `n_txn` to the transactions: how many transactions that customer has in total. Use `groupby(...).transform("count")`. Print the shape of `groupby().count()` vs `transform()` to see the difference. (★★★)

`hint:` `df.groupby("customer_id")["transaction_id"].transform("count")`. `transform` returns one value per ORIGINAL row (6,000), not one per group (800).

#### 78. A payment of 300 EUR is normal for some customers and strange for others. Add `cust_avg` (the customer's own average amount) and `amount_ratio` = amount / cust_avg. Compare the fraud rate for transactions with `amount_ratio > 3` versus the rest. (★★★)

`hint:` `transform("mean")` for the average, then divide. Group by the True/False column `df["amount_ratio"] > 3`.

#### 79. Add two 0/1 flag columns: `is_night` (hour 0 to 5) and `is_foreign` (country is not NL). Then show the fraud rate and count for every combination of the two flags. (★★★)

`hint:` `df["timestamp"].dt.hour.between(0, 5).astype(int)` and `(df["country"] != "NL").astype(int)`. Group by both flags.

#### 80. For each transaction, how many hours have passed since the same customer's previous transaction? Sort by customer and time, then use `groupby("customer_id")["timestamp"].diff()`. The first transaction of each customer has no previous one: what value does it get? (★★★)

`hint:` `diff()` gives a Timedelta; turn it into hours with `.dt.total_seconds() / 3600`. Sort with `sort_values(["customer_id", "timestamp"])` first.

#### 81. Spot the bug. A colleague wants to cap every amount above 1,000 EUR at 1,000 and writes the code below. Run it: did the table change? Explain why not, and fix it. (★★★)

```python
df[df["amount_eur"] > 1000]["amount_eur"] = 1000
print(df["amount_eur"].max())
```

`hint:` `df[mask]` makes a temporary copy, and the second `[...] =` changes the copy. Do it in one step: `df.loc[mask, "amount_eur"] = 1000`.

#### 82. Rank swimmers inside each race. For the 2024 Pune Open, rank every OK swim within its `event` (1 = fastest), and print the podium (ranks 1 to 3) of each event, sorted by event and rank. (★★★)

`hint:` `groupby("event")["time_sec"].rank(method="min")`. `method="min"` gives tied swimmers the same (best) rank.

#### 83. Spot the bug. This code is meant to show the number of frauds per channel, but the numbers look far too big. Find the mistake and fix it. (★★★)

```python
df.groupby("channel")["is_fraud"].count()
```

`hint:` Same trap as exercise 39, but inside a groupby. `count` counts rows; `sum` adds the 1s.

#### 84. Rolling windows smooth a noisy line. Work out the total amount spent per day, then a 7-day rolling average of it. Print the first 10 days of both side by side. Why are the first 6 rolling values NaN? (★★★)

`hint:` `daily = df.set_index("timestamp").resample("D")["amount_eur"].sum()`, then `daily.rolling(7).mean()`.

#### 85. Add two "history" features per customer: `txn_number` (1 for their first transaction, 2 for the second ...) and `spent_so_far` (running total of their amounts, including this one). Sort by customer and time first. (★★★)

`hint:` `groupby("customer_id").cumcount() + 1` (cumcount starts at 0), and `groupby("customer_id")["amount_eur"].cumsum()`.

#### 86. Who improved most at 100 Free? Using clean OK results sorted by date, find for each swimmer their FIRST 100 Free time and their BEST 100 Free time. Add `improvement = first - best` (seconds dropped) and print the top 5 improvers with their names. (★★★)

`hint:` After sorting by date: `groupby("swimmer_id")["time_sec"].agg(first="first", best="min")`. Then merge with swimmers for the names.

#### 87. A personal best (PB) is a swimmer's fastest time so far in an event. For clean OK results, sorted by date, mark `is_pb = True` when a swim beats that swimmer's best time from all EARLIER races in the same event (a first-ever swim does not count). Which 5 swimmers set the most PBs? (★★★)

`hint:` Inside each (swimmer, event) group: `prev_best = transform(lambda s: s.cummin().shift())`. `cummin` = best so far, `shift` moves it down one row so it only uses earlier races.

#### 88. Spot the bug. Below, a customers table accidentally contains 5 customers twice. After merging it onto the transactions, the row count goes UP. Show it, explain why, use `validate="many_to_one"` to catch it, and fix it. (★★★)

```python
import pandas as pd
df = pd.read_csv("../data/transactions.csv")
cust = pd.read_csv("../data/customers.csv")
cust_bad = pd.concat([cust, cust.head(5)])   # 5 customers appear twice
```

`hint:` If a key appears twice in the right table, every matching left row is copied twice. `validate="many_to_one"` raises a `MergeError` when the right keys are not unique. Fix with `drop_duplicates("customer_id")`.

#### 89. Why is this misleading? A report says "the average fraud rate across our countries is X%", computed as the mean of the per-country fraud rates. Compute that number, the true overall fraud rate, and explain why they differ so much. (★★★)

`hint:` Compare `df.groupby("country")["is_fraud"].mean().mean()` with `df["is_fraud"].mean()`. Think about how many transactions each country has.

#### 90. Method chaining means writing steps one after another, joined by dots, without saving in-between tables. Rewrite this as ONE chain, using `.assign` (adds a column and returns the table) and `.query` (filters with a text condition): (★★★)

```python
df = pd.read_csv("../data/transactions.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["hour"] = df["timestamp"].dt.hour
online = df[df["channel"] == "online"]
out = online.groupby("hour")["is_fraud"].mean().sort_values(ascending=False).head(3)
```

`hint:` `.assign(hour=lambda d: d["timestamp"].dt.hour)` (the `d` is the table at that point in the chain), and `.query("channel == 'online'")`. Wrap the chain in round brackets so you can put one step per line.

#### 91. Reshaping. Make a WIDE table of best 50 Back time per swimmer (rows) per year (columns 2024, 2025) for clean OK results. Then turn it back into a LONG table (one row per swimmer per year) with `melt`. Print the head of both. (★★★)

`hint:` Wide: `pivot_table(index="swimmer_id", columns="year", values="time_sec", aggfunc="min")`. Long: `wide.reset_index().melt(id_vars="swimmer_id", var_name="year", value_name="best_time")`.

#### 92. Build a customer-level table (one row per customer) from the transactions with: `n_txn`, `total_eur`, `avg_eur`, `max_eur`, `share_online` (fraction of their transactions that are online), `n_countries` (distinct countries), and `had_fraud` (1 if any of their transactions is fraud). Print the shape and head. (★★★)

`hint:` Make an 0/1 `is_online` column first, then one named `.agg` with `("is_online", "mean")`, `("country", "nunique")` and `("is_fraud", "max")`.

#### 93. Join the customer-level table from exercise 92 to a CLEANED customers table (age -1 replaced by the median real age, plus `account_age_days` on 2025-03-31). Use `validate="one_to_one"` and check: 800 rows, no missing values. Then compare the average features of customers with and without fraud. (★★★)

`hint:` Rebuild both tables, merge on `customer_id` with `validate="one_to_one"`, check `isna().sum().sum()`, then `groupby("had_fraud").mean(numeric_only=True)`.

#### 94. Models need numbers, not text. One-hot encoding turns a text column into several 0/1 columns, one per value. Use `pd.get_dummies` on the transactions for `channel` and `merchant_category` (missing filled as `"unknown"`), and print the new column names and the shape. (★★★)

`hint:` `pd.get_dummies(df, columns=["channel", "merchant_category"], dtype=int)`.

#### 95. Build a model-ready table for fraud detection. Write a function `make_features(path)` that returns `X` (features) and `y` (the `is_fraud` target). Features: `amount_eur`, `hour`, `is_night`, `is_foreign`, `amount_ratio` (vs customer average), `n_txn`, `hours_since_prev` (fill the first transaction with -1), plus one-hot `channel` columns. Check `X` has no missing values and print its shape, the fraud rate of `y`, and `X.head()`. (★★★)

`hint:` Put the steps from exercises 77–80 and 94 inside one function. At the end: `y = df["is_fraud"]`, `X = df[feature_list]`, `return X, y`.

#### 96. Why is this misleading? Someone adds a feature `cust_fraud_rate` = the customer's fraud rate over ALL their transactions, and says it predicts fraud almost perfectly. Show how strong it looks, explain the problem (this is called "target leakage"), and build an honest version that only uses the customer's EARLIER transactions. (★★★)

`hint:` The feature is made from `is_fraud` itself, including the current row. Honest version: sort by time, then per customer `cumsum()` of `is_fraud` minus the current row (or `.shift()` then `cumsum`) = frauds seen BEFORE this transaction.

#### 97. Why is this misleading? A model that says "never fraud" for every transaction gets very high accuracy. Compute its accuracy with pandas. Then test a simple rule, "fraud if night AND foreign, OR amount above 500", and compute its accuracy, precision (of the flagged, how many are fraud) and recall (of the frauds, how many were flagged). (★★★)

`hint:` Accuracy = `(pred == y).mean()`. Precision = `(pred & y).sum() / pred.sum()`. Recall = `(pred & y).sum() / y.sum()`. Use booleans for `pred` and `y`.

#### 98. Spot the bug. These meet dates are stored as text in day/month/year form. The code finds the "latest" meet and sorts by date, but both answers are wrong. Why? Fix it. (★★★)

```python
import pandas as pd
meets = pd.DataFrame({"meet": ["Winter", "Spring", "Summer", "Diwali"],
                      "date": ["20/01/2025", "15/03/2025", "10/05/2025", "26/10/2024"]})
print(meets["date"].max())
print(meets.sort_values("date"))
```

`hint:` Text is compared letter by letter, so `"26/..."` beats `"20/..."` regardless of year. Convert with `pd.to_datetime(meets["date"], format="%d/%m/%Y")`.

#### 99. A full swim season report in one script. From the raw files: drop duplicates, clean `event` and `stroke`, drop DQ swims, find each swimmer's best time per event, merge in `name` and `gender`, rank swimmers within each (event, gender) by best time, and print the top 3 per event and gender for the 50 m events only. (★★★)

`hint:` Steps you already know: `drop_duplicates`, `replace`, `.str.strip().str.title()`, filter OK, `groupby([...]).min().reset_index()`, merge, `groupby(["event", "gender"])["best"].rank(method="min")`. Filter 50 m events with `.str.startswith("50 ")`.

#### 100. Capstone. Write a function `fraud_report(path)` that loads the transactions, adds `is_night`, `is_foreign` and `amount_ratio`, assigns each transaction a `risk_group`: `"high"` if (night and foreign) or amount_ratio > 3, `"medium"` if night or foreign, else `"low"`. It should save the table with these columns to `outputs/transactions_features.csv` and return a summary per risk group: number of transactions, number of frauds, fraud rate, and share of ALL frauds caught in that group. Print the summary. (★★★)

`hint:` Use `np.select([cond_high, cond_medium], ["high", "medium"], default="low")` for the groups (conditions are checked in order). Share of frauds = `n_fraud / n_fraud.sum()`.
