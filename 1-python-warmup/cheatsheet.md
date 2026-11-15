# Python warm-up cheatsheet

### Values and text
| Function / syntax | What it does | Tiny example |
|---|---|---|
| `type(x)` | kind of value | `type(31.4)` -> `float` |
| `int()`, `float()`, `str()` | convert type | `float("75.3")` -> `75.3` |
| `//`, `%` | whole division, remainder | `75 // 60` -> `1`, `75 % 60` -> `15` |
| `round(x, n)` | round to n decimals | `round(3.14159, 2)` -> `3.14` |
| `f"{x:.2f}"` | value in text, 2 decimals | `f"{28.9:.2f}"` -> `"28.90"` |

### Lists and tuples
| Function / syntax | What it does | Tiny example |
|---|---|---|
| `lst[0]`, `lst[-1]` | first, last item | `[5, 6, 7][-1]` -> `7` |
| `lst[a:b]` | slice, b not included | `[5, 6, 7][:2]` -> `[5, 6]` |
| `lst.append(x)` | add to end | `t.append(30.1)` |
| `len`, `sum`, `min`, `max` | count, total, smallest, largest | `sum([1, 2])` -> `3` |
| `x in lst` | is x in the list? | `"a" in ("a", "b")` -> `True` |
| `a, b = pair` | unpack a tuple | `name, t = ("Kabir", 28.9)` |

### Loops and decisions
| Function / syntax | What it does | Tiny example |
|---|---|---|
| `for x in lst:` | repeat for each item | `for t in times: print(t)` |
| `range(a, b)` | a up to b-1 | `range(1, 4)` -> 1, 2, 3 |
| `if / elif / else` | first True branch runs | `if m >= 75: ... elif m >= 50: ...` |
| `enumerate(lst, start=1)` | position + item | `for i, n in enumerate(names, start=1):` |
| `zip(a, b)` | pair two lists | `dict(zip(names, times))` |
| `[f(x) for x in lst if cond]` | list comprehension | `[a for a in amts if a > 500]` |

### Dictionaries
| Function / syntax | What it does | Tiny example |
|---|---|---|
| `d[key]` | look up (KeyError if missing) | `best["Kabir"]` |
| `d[key] = v` | add or change | `best["Rohan"] = 29.6` |
| `d.get(key, default)` | safe look-up | `best.get("Meera", 0)` |
| `d.items()` | (key, value) pairs | `for k, v in d.items():` |
| count pattern | count things | `c[x] = c.get(x, 0) + 1` |

### Functions, sorting, None, errors
| Function / syntax | What it does | Tiny example |
|---|---|---|
| `def f(x, rate=100): return ...` | function with default | `f(25)`, `f(25, rate=104)` |
| `sorted(lst, key=..., reverse=...)` | new sorted list | `sorted(res, key=lambda r: r[1])` |
| `lambda r: r[1]` | tiny one-line function | "give me item 1 of r" |
| `x is None` | check for "no value" | `if t is None: ...` |
| `try: ... except ValueError: ...` | catch bad conversions | `try: float("DQ") except ValueError: pass` |

### Modules and files
| Function / syntax | What it does | Tiny example |
|---|---|---|
| `import statistics` | load a module | `statistics.mean([2, 4])` -> `3` |
| `statistics.median / stdev` | middle value / spread | `statistics.median([1, 5, 9])` -> `5` |
| `import math` | maths functions | `math.sqrt(16)` -> `4.0` |
| `with open(path, newline="") as f:` | open a file safely | `open("../data/swimmers.csv", newline="")` |
| `list(csv.DictReader(f))` | CSV rows as dicts (all text) | `rows[0]["club"]` |

### Three bugs to remember
| Bug | Fix |
|---|---|
| removing from a list while looping over it | build a new list: `[t for t in times if t != 0]` |
| `def f(x, items=[])` | `items=None`, then `if items is None: items = []` |
| `if c == "a" or "b":` | `if c in ("a", "b"):` (and `==` compares, `=` stores) |
