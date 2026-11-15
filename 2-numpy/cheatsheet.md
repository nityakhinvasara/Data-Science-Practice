# NumPy cheatsheet

`import numpy as np` · `rng = np.random.default_rng(42)`

### Create
| Function | What it does | Tiny example |
|---|---|---|
| `np.array(list)` | list -> array | `np.array([1, 2, 3])` |
| `np.zeros(shape)` / `np.ones(shape)` | all 0s / all 1s | `np.zeros((3, 4))` |
| `np.full(n, v)` | all the same value | `np.full(6, 25.0)` |
| `np.arange(start, stop, step)` | counting, stop excluded | `np.arange(50, 401, 50)` |
| `np.linspace(a, b, n)` | n even points, b included | `np.linspace(0, 1, 5)` |
| `np.eye(n)` | identity matrix | `np.eye(3)[codes]` = one-hot |
| `rng.integers(lo, hi, size)` | random whole numbers, hi excluded | `rng.integers(1, 7, size=10)` |
| `rng.uniform / normal / choice / permutation` | random decimals / bell curve / pick / shuffle | `rng.permutation(10)` |

### Inspect and reshape
| Function | What it does | Tiny example |
|---|---|---|
| `.shape .size .ndim .dtype` | facts (no brackets) | `laps.shape` -> `(3, 4)` |
| `.astype(t)` | convert type (copy) | `a.astype(float)` |
| `.reshape(r, c)` | new shape, same values; `-1` = auto | `np.arange(12).reshape(4, -1)` |
| `.flatten()` / `.T` | to 1D / swap rows and columns | `laps.T` |
| `.copy()` | independent copy (slices are views!) | `a[:3].copy()` |

### Index and select
| Syntax | What it does | Tiny example |
|---|---|---|
| `a[i]`, `a[-1]` | one value (from 0; -1 = last) | `a[2]` |
| `a[start:stop:step]` | slice | `a[::-1]` reversed |
| `m[r, c]`, `m[:, c]` | 2D: row, column | `laps[:2, -2:]` |
| `a[mask]` | keep where True | `a[a > 100]` |
| `(c1) & (c2)`, `\|`, `~` | and, or, not (brackets!) | `a[(a > 50) & (a < 200)]` |
| `a[[i, j]]` | fancy indexing (copy) | `names[np.argsort(times)]` |

### Count, label, sort
| Function | What it does | Tiny example |
|---|---|---|
| `mask.sum()` / `mask.mean()` | how many / what fraction True | `(a > 100).sum()` |
| `np.where(c, x, y)` | if/else per element | `np.where(a > 100, "big", "small")` |
| `np.where(c)[0]` | positions where True | `np.where(y == 1)[0]` |
| `np.select(conds, choices, default)` | many labels, first True wins | bands of amounts |
| `np.any` / `np.all` | at least one / every | `np.all(t < 31)` |
| `np.sort(a)` / `np.argsort(a)` | sorted values / sorting positions | `np.argsort(a)[::-1][:3]` top 3 |
| `np.unique(a, return_counts=True)` | distinct values + counts | `return_inverse=True` -> codes |
| `np.bincount(codes, weights=w)` | count (or sum w) per code | group totals |

### Statistics (add `axis=0` per column, `axis=1` per row)
| Function | What it does | Tiny example |
|---|---|---|
| `.sum() .mean() .min() .max() .std()` | basic stats | `laps.sum(axis=1)` |
| `np.median(a)` | middle value | `np.median(t)` |
| `.argmax() / .argmin()` | position of max / min | `days[spend.argmax()]` |
| `np.percentile(a, [25, 75])` | percentiles | IQR = p75 - p25 |
| `np.cumsum(a)` / `np.diff(a)` | running total / neighbour differences | `np.diff(s, prepend=0)` |
| `keepdims=True` | keep shape for broadcasting | `m - m.mean(axis=1, keepdims=True)` |

### Clean and scale
| Function | What it does | Tiny example |
|---|---|---|
| `np.isnan(a)` | find NaN (never `== np.nan`) | `np.isnan(a).sum()` |
| `np.nanmean / nanmin / nanmax` | stats skipping NaN | `np.nanmean(t)` |
| `np.nan_to_num(a)` | NaN -> 0 (careful!) | |
| `np.clip(a, lo, hi)` | cap values | `np.clip(a, 1, 500)` |
| `np.round(a, 2)`, `np.floor`, `np.ceil` | rounding | `np.round(a * 90, 2)` |
| min-max | to 0..1 | `(x - x.min()) / (x.max() - x.min())` |
| z-score | mean 0, std 1 | `(x - x.mean()) / x.std()` |

### Combine, linear algebra, files
| Function | What it does | Tiny example |
|---|---|---|
| `np.concatenate([a, b])` | join 1D | `np.concatenate([jan, feb])` |
| `np.vstack` / `np.hstack` | add rows / add columns | `np.hstack([m, c.reshape(-1, 1)])` |
| `a @ b`, `np.dot` | dot / matrix product; (n,k)@(k,m)->(n,m) | `scores @ weights` |
| `np.linalg.norm(v, axis=1)` | length / distance | `np.linalg.norm(pts - p, axis=1)` |
| `np.linalg.solve(A, b)` | solve `A @ x = b` | ticket prices |
| `np.convolve(a, np.ones(3)/3, mode="valid")` | 3-point moving average | |
| `np.allclose` / `np.array_equal` | nearly equal / exactly equal | |
| `np.save` / `np.load` | `.npy` files (in `outputs/`) | `np.save("outputs/a.npy", a)` |
| `np.loadtxt` / `np.genfromtxt` | read CSV numbers (genfromtxt: empty -> NaN) | `usecols=(6, 7), skiprows=1` |

### ML by hand
| Idea | Code |
|---|---|
| Confusion matrix cell | `TP = ((y_pred == 1) & (y_true == 1)).sum()` |
| Precision / recall | `TP / (TP + FP)` / `TP / (TP + FN)` |
| Train/test split | `idx = rng.permutation(n)`; `X[idx[:cut]]`, `y[idx[:cut]]` (same idx!) |
| MSE | `((pred - y) ** 2).mean()` |
| Gradient step | `w -= lr * 2 * ((w * x + b - y) * x).mean()` |
| Sigmoid | `1 / (1 + np.exp(-s))` |
| Cosine similarity | `a @ b / (np.linalg.norm(a) * np.linalg.norm(b))` |

**Traps:** slices are views · `uint8`/`int8` overflow silently · floats written into an int array lose decimals · NaN is not 0 · learn scaling numbers on train only · `&` not `and`.
