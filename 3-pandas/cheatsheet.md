# pandas cheatsheet

`df` = a DataFrame (table), `s` = a Series (one column). `import pandas as pd`, `import numpy as np`.

### Make and load
| Function | What it does | Tiny example |
|---|---|---|
| `pd.Series(values, index=labels)` | one labelled column | `pd.Series([31.2, 29.8], index=["Aarav", "Diya"])` |
| `pd.DataFrame(dict)` | table from columns | `pd.DataFrame({"name": ["Asha"], "marks": [78]})` |
| `pd.DataFrame(rows, columns=[...])` | table from rows | `pd.DataFrame([["T1", 12.5]], columns=["id", "amt"])` |
| `pd.read_csv(path)` | load a CSV file | `pd.read_csv("../data/transactions.csv")` |
| `df.to_csv(path, index=False)` | save a CSV file | `df.to_csv("outputs/x.csv", index=False)` |

### First look
| Function | What it does | Tiny example |
|---|---|---|
| `head(n)` / `tail(n)` | first / last n rows | `df.head()` |
| `shape` | (rows, columns), no brackets | `df.shape` |
| `dtypes` / `info()` | types / types + missing | `df.info()` |
| `describe()` | summary statistics | `df["amount_eur"].describe()` |
| `value_counts()` | count each value | `df["channel"].value_counts(normalize=True)` |
| `nunique()` / `unique()` | how many / which distinct values | `df["country"].nunique()` |

### Select and filter
| Function | What it does | Tiny example |
|---|---|---|
| `df["col"]` / `df[["a", "b"]]` | one column (Series) / several (DataFrame) | `df[["customer_id", "amount_eur"]]` |
| `loc[rows, cols]` | by label, end included | `cust.loc["C0005", "segment"]` |
| `iloc[rows, cols]` | by position, end excluded | `df.iloc[10:15]` |
| `df[mask]` | keep rows where mask is True | `df[df["amount_eur"] > 500]` |
| `&`, `\|`, `~` | and, or, not (brackets around each!) | `df[(a > 1) & (b == "x")]` |
| `isin(list)` | value is in a list | `df["country"].isin(["NG", "RU"])` |
| `between(lo, hi)` | lo <= value <= hi | `cust["age"].between(18, 25)` |
| `query("text")` | filter written as text | `df.query("channel == 'online'")` |
| `sort_values(col, ascending=)` | sort rows | `df.sort_values(["event", "time_sec"])` |
| `nlargest(n, col)` | top n rows | `df.nlargest(5, "amount_eur")` |

### Change columns
| Function | What it does | Tiny example |
|---|---|---|
| `df["new"] = ...` | add a column | `df["inr"] = df["amount_eur"] * 95` |
| `rename(columns={})` | rename (save the result!) | `df.rename(columns={"name": "swimmer"})` |
| `drop(columns=[...])` | remove columns | `df.drop(columns=["coach"])` |
| `assign(new=lambda d: ...)` | add a column inside a chain | `df.assign(hour=lambda d: d["timestamp"].dt.hour)` |
| `astype(type)` | change dtype | `df["is_fraud"].astype(bool)` |
| `map(dict)` | replace values via a dict | `df["country"].map({"NL": "EU"})` |
| `apply(func)` | run a function on each value | `df["amount_eur"].apply(size_label)` |
| `np.select(conds, choices, default=)` | pick a label by first True condition | `np.select([a > 500], ["high"], default="low")` |

### Clean
| Function | What it does | Tiny example |
|---|---|---|
| `isna().sum()` | missing per column | `res.isna().sum()` |
| `fillna(value)` | fill missing | `s.fillna(s.median())` |
| `dropna(subset=[...])` | drop rows with missing | `marks.dropna(subset=["sleep_hours"])` |
| `duplicated()` / `drop_duplicates()` | find / remove repeated rows | `res.drop_duplicates()` |
| `replace(old, new)` | swap exact values | `s.replace({"50 free": "50 Free"})`, `s.replace(-1, np.nan)` |
| `.str.strip()/.lower()/.title()` | clean text | `res["stroke"].str.strip().str.title()` |
| `.str.contains/startswith` | text tests | `res["event"].str.startswith("50 ")` |
| `.str.split(" ", n=1, expand=True)` | split text into columns | `res["event"].str.split(" ", n=1, expand=True)` |
| `count()` vs `sum()` vs `mean()` | filled cells / total of values / share of 1s | `df["is_fraud"].sum()` = number of frauds |

### Group and summarise
| Function | What it does | Tiny example |
|---|---|---|
| `groupby(col)[col2].func()` | one number per group | `df.groupby("channel")["is_fraud"].mean()` |
| `.agg([...])` | several functions | `.agg(["mean", "count"])` |
| `.agg(name=(col, func))` | named aggregation | `.agg(n_fraud=("is_fraud", "sum"))` |
| `.transform(func)` | group answer on every row | `df.groupby("customer_id")["amount_eur"].transform("mean")` |
| `reset_index()` | group labels back to columns | `best.reset_index()` |
| `unstack()` | inner index level to columns | `df.groupby(["a", "b"])["x"].mean().unstack()` |
| `idxmin()` / `idxmax()` | label of min / max | `ok.groupby("event")["time_sec"].idxmin()` |
| `rank(method="min")` | 1 = smallest | `g["time_sec"].rank(method="min")` |
| `groupby(..., dropna=False)` | keep the NaN group | `df.groupby("merchant_category", dropna=False).size()` |

### Combine and reshape
| Function | What it does | Tiny example |
|---|---|---|
| `merge(other, on=, how=)` | join by key (inner/left/right/outer) | `df.merge(cust, on="customer_id", how="left")` |
| `merge(..., indicator=True)` | adds `_merge` column | find `left_only` rows |
| `merge(..., validate="many_to_one")` | error if right key repeats | catches duplicate-row bugs |
| `pd.concat([a, b], ignore_index=True)` | stack tables | `pd.concat([y2024, y2025], ignore_index=True)` |
| `pivot_table(index, columns, values, aggfunc)` | grid of a groupby | `df.pivot_table(index="channel", columns="country", values="is_fraud", aggfunc="mean")` |
| `pd.crosstab(a, b, normalize=)` | count pairs | `pd.crosstab(df["channel"], df["is_fraud"])` |
| `melt(id_vars, var_name, value_name)` | wide to long | `wide.reset_index().melt(id_vars="swimmer_id")` |
| `pd.get_dummies(df, columns=, dtype=int)` | one-hot encode | `pd.get_dummies(df, columns=["channel"], dtype=int)` |

### Dates and time series
| Function | What it does | Tiny example |
|---|---|---|
| `pd.to_datetime(s, format=)` | text to dates | `pd.to_datetime(s, format="%d/%m/%Y")` |
| `.dt.hour/.dt.month/.dt.day_name()` | date parts | `df["timestamp"].dt.hour` |
| date - date, `.dt.days`, `.dt.total_seconds()` | durations | `(ref - cust["open"]).dt.days` |
| `set_index(t).resample("W").size()` | count per week ("D", "MS") | weekly transactions |
| `groupby(...).diff()` | this row minus previous | time since previous payment |
| `rolling(n).mean()` | moving average | `daily.rolling(7).mean()` |
| `cumsum()/cummin()/cumcount()` | running total / best so far / row number | `g.cumcount() + 1` |
| `shift()` | previous row's value | `s.cummin().shift()` |

### Bins and charts
| Function | What it does | Tiny example |
|---|---|---|
| `pd.cut(s, bins=[...])` | your own ranges | `pd.cut(s, [0, 20, 50, float("inf")])` |
| `pd.qcut(s, q=4, labels=)` | equal-sized groups | `pd.qcut(s, 4, labels=["Q1", "Q2", "Q3", "Q4"])` |
| `s.plot(kind="bar")` | quick chart (returns `ax`) | `ax.set_title("..."); plt.show()` |

### Traps to remember
- `.count()` counts rows; `.sum()` counts the 1s.
- `df[mask]["col"] = x` does nothing: use `df.loc[mask, "col"] = x`.
- Check `len()` before and after a merge: it should not grow on a left merge to a lookup table.
- Average of averages is not the overall average: weight by counts.
- Sort by time before `diff`, `shift`, `cumsum`, `first`.
- A feature must only use information known **at the moment** of the event (no leakage).
- Accuracy is useless for rare events: look at precision and recall.
