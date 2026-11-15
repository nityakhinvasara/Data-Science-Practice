# scikit-learn: the guide

scikit-learn (imported as `sklearn`) is the standard Python library for machine learning on tables of data. Almost every junior data scientist job uses it, and interviewers expect you to know it well.

## How to use this guide

- Each Part matches one day of exercises (about 1 hour). Read the Part first (about 10 minutes), then do the exercises it names.
- Type the small examples yourself and run them. The output is shown as `# comments`.
- You already know NumPy and pandas. Here you use them to feed data into models.
- No heavy maths: every idea is explained in words. If a word is new, it is explained the first time it appears.

---

## Part 1: What machine learning is, and your first models (exercises 1–13)

### What is machine learning?

Normal programming: **you** write the rules. "If the amount is over €1,000 and the country is not NL, flag it."

Machine learning (ML): you give the computer **many examples with the right answer**, and it **finds the rules itself**.

**The fraud example.** A bank has 6,000 past card payments. For each one it knows the amount, the time, the country, the shop type... and whether it later turned out to be fraud. An ML model studies these examples and learns patterns like "big online payments at 3 a.m. from abroad are often fraud". Then, when a **new** payment comes in, the model gives its best guess: fraud or not.

### The words you need

| Word | Meaning | Fraud example |
|---|---|---|
| **feature** | one piece of information the model looks at (a column) | amount, hour, country |
| **X** | the table of all features (rows = examples, columns = features). Always 2-D. | 6,000 rows x 5 columns |
| **target** / **label**, **y** | the answer you want to predict (one per row). 1-D. | `is_fraud` (0 or 1) |
| **sample** | one row | one payment |
| **training** / **fitting** | the model studies X and y to learn patterns | `model.fit(X, y)` |
| **predicting** | the trained model guesses y for rows it has not seen | `model.predict(X_new)` |
| **model** | the thing that learns. In sklearn, a Python object | `LogisticRegression()` |

### Two kinds of problems

| Type | y is... | Examples |
|---|---|---|
| **Classification** | a category (a class) | fraud yes/no; flower species; pass/fail |
| **Regression** | a number on a scale | final marks (0–100); a swim time; house price |

Quick test: can you list all possible answers? Then it is classification. Otherwise regression.

### Built-in practice datasets

sklearn ships small datasets that work offline:

```python
from sklearn.datasets import load_iris
iris = load_iris()
print(iris.data.shape)       # (150, 4)  -> X: 150 flowers, 4 measurements
print(iris.target.shape)     # (150,)    -> y: species as 0, 1, 2
print(iris.target_names)     # ['setosa' 'versicolor' 'virginica']

X, y = load_iris(return_X_y=True)        # shortcut: just the arrays
df = load_iris(as_frame=True).frame      # or a pandas DataFrame with a "target" column
```

Others you will use: `load_breast_cancer` (classification: 0 = malignant, 1 = benign) and `load_diabetes` (regression).

From your own CSV, X and y are just pandas selections:

```python
import pandas as pd
df = pd.read_csv("../data/student_marks.csv")
X = df[["study_hours_per_week", "attendance_pct", "previous_cgpa"]]   # double brackets -> DataFrame (2-D)
y = df["final_marks"]                                                # single brackets -> Series (1-D)
```

### Train/test split: never grade a model on its own homework

If you test a model on the same rows it learned from, it can just remember them. So you hide some rows (the **test set**), train on the rest (the **training set**), and only then check on the hidden rows.

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
```

- `test_size=0.25`: keep 25% for testing.
- `random_state=42`: the rows are shuffled before splitting; fixing the number gives the same shuffle every time (so your results are repeatable).
- `stratify=y`: keep the class proportions the same in train and test. Important when one class is rare (fraud!).
- The order of the four outputs is always `X_train, X_test, y_train, y_test`.

### Every sklearn model works the same way

```python
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()        # 1. create
model.fit(X_train, y_train)           # 2. train
y_pred = model.predict(X_test)        # 3. predict
print(model.score(X_test, y_test))    # 4. score -> 1.0 on this iris split
```

Three first models:

| Model | Kind | Idea in plain words |
|---|---|---|
| `KNeighborsClassifier` | classification | find the 5 most similar training rows ("nearest neighbours") and take a vote |
| `LogisticRegression` | classification (despite the name!) | gives each feature a weight, adds them up, turns the total into a probability between 0 and 1 |
| `LinearRegression` | regression | prediction = a starting number + weight x each feature (a straight-line rule) |

`.score` means **accuracy** (share correct) for classifiers and **R²** for regressors (1 = perfect, 0 = no better than always guessing the average).

A linear regression is easy to read:

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(X_train, y_train)    # fit returns the model, so you can chain
print(model.coef_)        # [0.99 0.17 2.69] -> +1 study hour/week ≈ +1 mark
print(model.intercept_)   # 44.87 -> the starting number
```

To predict for a new student, build a one-row DataFrame with the **same column names**:

```python
new = pd.DataFrame([[15, 90, 8.0]], columns=X.columns)
print(model.predict(new))   # [96.6...]
```

**Why it matters at work:** every model you build, from fraud scoring to churn, follows exactly this split -> fit -> predict -> score pattern.

### Common mistakes
- Passing a 1-D X (`df["hours"]`) instead of 2-D (`df[["hours"]]`). sklearn wants X as a table.
- Swapping the order of the outputs of `train_test_split`.
- Forgetting `random_state`, then wondering why results change every run.
- Calling `.score` on the training data and thinking the model is great.

**Now do exercises 1–13.**

---

## Part 2: Measuring a model: metrics (exercises 14–27)

A **metric** is a number that says how good a model is. Choosing the right one is half the job.

### Accuracy and its trap

**Accuracy** = share of predictions that are correct.

```python
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)    # same as (y_pred == y_test).mean()
```

**The fraud trap.** In `transactions.csv` only 1.9% of payments are fraud. A "model" that **always says "not fraud"** is right 98.1% of the time... and catches zero fraud. So accuracy is useless when one class is rare.

A **baseline** is a dumb model you must beat. sklearn has them built in:

```python
from sklearn.dummy import DummyClassifier, DummyRegressor
DummyClassifier(strategy="most_frequent")   # always predicts the most common class
DummyRegressor(strategy="mean")             # always predicts the average
```

### The confusion matrix

A 2x2 table of right and wrong answers. With fraud = 1 ("positive"):

|  | predicted 0 (normal) | predicted 1 (fraud) |
|---|---|---|
| **truly 0** | **TN** true negative: normal, said normal | **FP** false positive: a false alarm |
| **truly 1** | **FN** false negative: missed fraud | **TP** true positive: caught fraud |

```python
from sklearn.metrics import confusion_matrix
y_true = [0, 0, 0, 1, 0, 1, 0, 0, 1, 0]
y_pred = [0, 1, 0, 1, 0, 0, 0, 0, 1, 1]
print(confusion_matrix(y_true, y_pred))
# [[5 2]
#  [1 2]]
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()   # 5 2 1 2
```

Rows are the truth, columns are the prediction. The diagonal is "correct".

### Precision, recall, F1

| Metric | Question it answers | From the table |
|---|---|---|
| **precision** | Of the payments I flagged, how many were really fraud? | TP / (TP + FP) |
| **recall** | Of all the real frauds, how many did I catch? | TP / (TP + FN) |
| **F1** | One number that is only high if both are high | a special average of the two |

For the example above: precision = 2/4 = 0.5, recall = 2/3 = 0.67, F1 = 0.57.

```python
from sklearn.metrics import precision_score, recall_score, f1_score, classification_report
print(classification_report(y_test, y_pred))   # precision, recall, f1 for every class at once
```

In the report, **support** = how many true rows of that class there are.

There is always a **trade-off**: flag more payments and you catch more fraud (recall up) but bother more innocent customers (precision down).

### Regression metrics

| Metric | Meaning | sklearn |
|---|---|---|
| **MAE** mean absolute error | on average, how far off is the prediction (in marks, seconds, euros) | `mean_absolute_error` |
| **RMSE** root mean squared error | like MAE, but big misses count extra. Always ≥ MAE | `root_mean_squared_error` |
| **R²** | share of the variation explained. 1 = perfect, 0 = as good as guessing the average, can be negative | `r2_score` |

```python
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score
print(mean_absolute_error(y_test, y_pred))      # 4.12  -> off by about 4 marks on average
print(root_mean_squared_error(y_test, y_pred))  # 5.46
print(r2_score(y_test, y_pred))                 # 0.549
```

MAE is the easiest to explain to a manager: "we are off by about 4 marks".

**Why it matters at work:** a bank does not care about accuracy; it cares how many frauds are caught (recall) and how many good customers are blocked (precision).

### Common mistakes
- Reporting accuracy on imbalanced data without a baseline.
- Mixing up the order: metrics take `(y_true, y_pred)`, truth first.
- Using `.count()` to count frauds: on a 0/1 column use `.sum()`.
- Mixing up precision and recall. Remember: **re**call = how many frauds did I **re**trieve.

**Now do exercises 14–27.**

---

## Part 3: Trees, forests and overfitting (exercises 28–40)

### Decision trees

A **decision tree** learns a chain of yes/no questions, like a flowchart:

```python
from sklearn.tree import DecisionTreeClassifier, export_text
tree = DecisionTreeClassifier(max_depth=2, random_state=42).fit(iris.data, iris.target)
print(export_text(tree, feature_names=iris.feature_names))
# |--- petal length (cm) <= 2.45
# |   |--- class: 0
# |--- petal length (cm) >  2.45
# |   |--- petal width (cm) <= 1.75
# |   |   |--- class: 1
# ...
```

`max_depth` = how many questions in a row it may ask. There is also `DecisionTreeRegressor` (each leaf predicts an average number).

### Overfitting and underfitting

- **Overfitting**: the model memorises the training data, including its random noise, and does worse on new data. Sign: train score much higher than test score.
- **Underfitting**: the model is too simple to capture the pattern. Sign: both scores low.

```python
for d in [1, 3, None]:
    tree = DecisionTreeClassifier(max_depth=d, random_state=42).fit(X_train, y_train)
    print(d, tree.score(X_train, y_train), tree.score(X_test, y_test))
# 1    0.923  0.923   <- too simple
# 3    0.977  0.944   <- good balance
# None 1.0    0.923   <- memorised the training set
```

Same with KNN: `n_neighbors=1` gets 100% on training data (each row is its own neighbour).

Settings you choose before training, like `max_depth` or `n_neighbors`, are called **hyperparameters**.

### Random forests

A **random forest** trains many trees (say 100), each on a random sample of rows and features, and lets them vote. One tree's mistakes are partly cancelled by the others, so a forest usually overfits less than one tree.

```python
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
forest = RandomForestClassifier(n_estimators=100, random_state=42).fit(X_train, y_train)
```

### Comparing models fairly

Use the **same split** for every model:

```python
models = {"logistic": LogisticRegression(max_iter=5000), "forest": RandomForestClassifier(random_state=42)}
for name, m in models.items():
    print(name, m.fit(X_train, y_train).score(X_test, y_test))
```

A fancier model is not always better (on `load_diabetes` linear regression beats the forest).

### Probabilities: predict_proba

Most classifiers can say **how sure** they are:

```python
proba = model.predict_proba(X_test[:3])
# [[0.019 0.981]     column 0 = P(class 0), column 1 = P(class 1); each row sums to 1
#  [0.998 0.002]
#  [0.176 0.824]]
model.classes_     # [0 1] -> the column order
```

`predict` is simply "is the probability of class 1 at least 0.5?" That 0.5 is called the **threshold**, and you can change it (Part 6).

**Why it matters at work:** random forests (and their cousins, gradient boosting) are the workhorses of fraud and risk models; probabilities let a bank rank payments from most to least suspicious.

### Common mistakes
- Judging a tree by its training score (an unlimited tree always gets 100%).
- Comparing models on different splits.
- Taking the wrong column of `predict_proba`: fraud probability is `[:, 1]`.
- Thinking a forest will fix a rare-class problem by itself (exercise 40 shows it does not).

**Now do exercises 28–40.**

---

## Part 4: Preparing data: preprocessing (exercises 41–52)

Real data is messy: different scales, missing values, text categories. Models need clean numbers. sklearn **transformers** fix this. They all work like this:

- `fit(X_train)`: learn something from the data (a mean, the list of categories...).
- `transform(X)`: apply it.
- `fit_transform(X_train)`: both in one step.

### Scaling with StandardScaler

Turns each column into "how many standard deviations from the mean" (mean 0, spread 1). Needed for models that measure distance or add up weighted features (KNN, logistic regression, KMeans, PCA). Trees and forests do **not** need it.

```python
from sklearn.preprocessing import StandardScaler
X = np.array([[10, 200], [20, 400], [30, 600], [40, 800]])
scaler = StandardScaler()
print(scaler.fit_transform(X))
# [[-1.34 -1.34]
#  [-0.45 -0.45]
#  [ 0.45  0.45]
#  [ 1.34  1.34]]
print(scaler.mean_)    # [ 25. 500.]
```

**Fit on train only.** The test set stands for future data you have not seen. If the scaler learns from it, information "from the future" leaks into training:

```python
scaler = StandardScaler().fit(X_train)       # learn from train
X_train_s = scaler.transform(X_train)
X_test_s = scaler.transform(X_test)          # apply the TRAIN numbers to test
```

On breast cancer, scaling lifts KNN from 0.93 to 0.98 accuracy.

### Filling missing values with SimpleImputer

```python
from sklearn.impute import SimpleImputer
imp = SimpleImputer(strategy="median")          # or "mean", "most_frequent" (works for text), "constant"
filled = imp.fit_transform(df[["sleep_hours"]]) # needs 2-D input
imp.statistics_                                  # [6.9] -> the value it learned
```

### Text categories with OneHotEncoder

Models need numbers. **One-hot encoding** makes one 0/1 column per category:

```python
from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
enc.fit_transform(t[["channel"]])[:2]
# [[0. 1. 0.]      in_store
#  [0. 0. 1.]]     online
enc.get_feature_names_out()   # ['channel_contactless' 'channel_in_store' 'channel_online']
```

- `sparse_output=False` returns a normal array you can print.
- `handle_unknown="ignore"`: a category never seen in training (a new country) becomes all zeros instead of an error.
- Why not `pd.get_dummies`? It only sees the data in front of it, so train and test can get **different columns**. The encoder remembers the categories from `fit`.

### ColumnTransformer: different steps for different columns

```python
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer([
    ("scale",  StandardScaler(),                   ["study_hours_per_week", "attendance_pct", "previous_cgpa"]),
    ("impute", SimpleImputer(strategy="median"),   ["sleep_hours"]),
    ("onehot", OneHotEncoder(handle_unknown="ignore"), ["favourite_subject"]),
])
out = ct.fit_transform(df)
print(out.shape)    # (300, 9): 3 + 1 + 5 subjects
```

Each entry is `(a name you choose, transformer, list of columns)`. Columns you do not list are dropped, unless you add `remainder="passthrough"`. You can also write `"passthrough"` as the transformer for columns that are already fine.

**A note on `student_marks.csv`:** every student passed, so `passed` is useless as a target. In these exercises we make our own target: `distinction = final_marks >= 90`.

**Why it matters at work:** most of a data scientist's time is cleaning and preparing data; doing it inside sklearn makes it repeatable.

### Common mistakes
- Calling `fit` or `fit_transform` on the test set.
- Passing a 1-D column (`df["x"]`) to a transformer: use `df[["x"]]`.
- Forgetting `handle_unknown="ignore"`, then crashing on a new category in production.
- Leaving the target (or something computed from it, like `passed`) inside X.

**Now do exercises 41–52.**

---

## Part 5: Pipelines, cross-validation and tuning (exercises 53–64)

### Pipelines

A **pipeline** chains preprocessing and a model into **one object**. It has `fit`, `predict`, `score` like any model, and it automatically fits each step on the training data only.

```python
from sklearn.pipeline import make_pipeline, Pipeline
pipe = make_pipeline(StandardScaler(), KNeighborsClassifier())
pipe.fit(X_train, y_train)
pipe.score(X_test, y_test)          # 0.979

# same, with your own step names:
pipe = Pipeline([("scaler", StandardScaler()), ("knn", KNeighborsClassifier())])
pipe.set_params(knn__n_neighbors=10)     # step name + two underscores + parameter
```

With `make_pipeline` the step names are the class names in lowercase, e.g. `kneighborsclassifier`. `pipe[-1]` is the last step (the model).

Pipelines can go inside a ColumnTransformer (e.g. impute **then** one-hot a column), and a ColumnTransformer can go inside a pipeline. The full pattern you will use again and again:

```python
pipe = make_pipeline(ct, LogisticRegression())
pipe.fit(X_train, y_train)              # raw DataFrame in...
pipe.predict_proba(new_student_df)      # ...prediction out
```

### Cross-validation

One train/test split depends on luck: the same model scores 0.909 to 0.965 on breast cancer depending on `random_state`. **Cross-validation (CV)** fixes this:

1. Cut the data into 5 parts (**folds**).
2. Train on 4, test on the 5th.
3. Repeat 5 times so each part is the test once.
4. Average the 5 scores.

```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(KNeighborsClassifier(), X, y, cv=5)
print(scores)                       # [0.967 1.    0.933 0.967 1.   ]
print(scores.mean(), scores.std())  # 0.973 0.025
```

Use `scoring="recall"`, `"f1"`, `"average_precision"`, `"neg_mean_absolute_error"` etc. to pick the metric. (sklearn wants "higher is better", so errors come with a minus sign.)

### KFold vs StratifiedKFold

| | What it does | When |
|---|---|---|
| `KFold(n_splits=5, shuffle=True, random_state=42)` | plain cuts | regression |
| `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` | every fold has the same class mix | classification, especially rare classes |

Warning: `KFold` without `shuffle` on sorted data (iris is sorted by species) puts a whole species in one fold, and the score drops to 0. For classifiers, `cv=5` already uses StratifiedKFold.

### GridSearchCV: let CV choose the hyperparameters

```python
from sklearn.model_selection import GridSearchCV
grid = {"kneighborsclassifier__n_neighbors": [1, 3, 5, 7, 9, 15]}
search = GridSearchCV(pipe, grid, cv=5).fit(X_train, y_train)
search.best_params_            # {'kneighborsclassifier__n_neighbors': 9}
search.best_score_             # 0.967 (average CV score)
search.best_estimator_         # already retrained on all of X_train
search.score(X_test, y_test)   # test ONCE at the very end
```

Keep grids small: 4 values x 3 values = 12 combinations x 5 folds = 60 fits.

### Data leakage

**Leakage** = information that would not be available in real use sneaks into training, so the score looks better than reality. Classic case: a step that learns from data (scaler, imputer, feature selector) is fitted on **all** rows before CV.

Exercise 64 shows it dramatically: on pure random noise (nothing to learn, honest accuracy 0.5), choosing the "best" columns on all the data first gives a CV accuracy of 0.82. Doing the same inside a pipeline gives the honest 0.47.

Rule: **every step that learns from data goes inside the pipeline**, and the pipeline goes inside CV.

**Why it matters at work:** "the model was great in the notebook but useless in production" is usually leakage. Interviewers love asking about it.

### Common mistakes
- Tuning on the test set (choosing settings by looking at test scores).
- Wrong parameter name in the grid: it must be `stepname__parameter`.
- Big grids that take forever. Start small.
- Preprocessing outside the pipeline, then cross-validating (leakage).

**Now do exercises 53–64.**

---

## Part 6: Rare classes, thresholds and feature importance (exercises 65–75)

Fraud is **imbalanced**: 98% normal, 2% fraud. A plain model learns that "always normal" is the easiest way to be right, so it catches nothing (recall 0). Three tools fix this.

### 1. class_weight="balanced"

Tells the model that each fraud matters as much as about 50 normal payments, so mistakes on fraud cost more during training.

```python
pipe = make_pipeline(StandardScaler(), LogisticRegression(class_weight="balanced"))
# no weight:  caught 0 of 28 frauds, 1 false alarm
# balanced:   caught 19 of 28 frauds, 434 false alarms
```

Accuracy drops (0.98 -> 0.70) and that is fine: we now catch most fraud. The price is false alarms.

### 2. Choosing your own threshold

`predict` uses 0.5. You can pick any cut-off on the fraud probability:

```python
proba = pipe.predict_proba(X_test)[:, 1]
y_pred = (proba >= 0.3).astype(int)
# threshold 0.3: 1016 alerts, recall 0.96, precision 0.03
# threshold 0.5:  453 alerts, recall 0.68, precision 0.04
# threshold 0.7:  123 alerts, recall 0.29, precision 0.07
```

`precision_recall_curve(y_true, proba)` gives precision and recall for **every** possible threshold, so you can find e.g. the highest threshold that still catches 80% of fraud. Choose the threshold on training or validation data, not on the final test set (Part 8 does this properly).

### 3. Metrics that ignore the threshold

Both use the probabilities and look at all thresholds at once.

| Metric | Plain meaning | Random guessing scores |
|---|---|---|
| **ROC AUC** (`roc_auc_score`) | pick one fraud and one normal payment at random: chance the model gives the fraud a higher score | 0.5 |
| **Average precision** / PR AUC (`average_precision_score`) | average precision of your alerts as you lower the threshold to catch more and more fraud | the fraud rate (about 0.02) |

```python
roc_auc_score(y_test, proba)            # 0.752
average_precision_score(y_test, proba)  # 0.075  (vs 0.019 for random)
```

ROC AUC looks rosy because it also rewards ranking the thousands of easy normal payments. **For rare events, report average precision**, and compare it with the fraud rate, not with 0.5. Draw the curve with `PrecisionRecallDisplay.from_estimator(pipe, X_test, y_test)`.

### Which features matter?

| Method | How | Watch out |
|---|---|---|
| `forest.feature_importances_` | how much each feature was used to split the trees | favours features with many different values (amount, hour) over 0/1 flags |
| `permutation_importance(model, X_test, y_test)` | shuffle one column; how much does the score drop? | slower, but measured on unseen data with your metric. Trust it more |
| logistic `coef_` on **scaled** features | size and sign of each weight | only comparable if features are scaled |

```python
from sklearn.inspection import permutation_importance
r = permutation_importance(forest, X_test, y_test, n_repeats=5, random_state=42, scoring="average_precision")
pd.Series(r.importances_mean, index=X.columns).sort_values(ascending=False)
```

None of these prove **cause**. They say what the model relies on.

**Why it matters at work:** fraud teams set thresholds based on how many alerts their analysts can review per day, and regulators ask which features drive a decision.

### Common mistakes
- Passing 0/1 predictions to `roc_auc_score` or `average_precision_score` instead of probabilities.
- Comparing average precision with 0.5 (the baseline is the fraud rate).
- Tuning the threshold on the test set, then reporting the test score as honest.
- Reading built-in tree importances as the truth.

**Now do exercises 65–75.**

---

## Part 7: Finding groups without labels: clustering and PCA (exercises 76–83)

So far every row had an answer (y). That is **supervised** learning. In **unsupervised** learning there is no y: the model looks for structure in X alone.

### KMeans clustering

**Clustering** = putting similar rows into groups. **KMeans** with `k` clusters:

1. Places k centre points.
2. Assigns each row to its nearest centre.
3. Moves each centre to the middle of its rows.
4. Repeats until nothing changes.

```python
from sklearn.cluster import KMeans
km = KMeans(n_clusters=3, random_state=42)
labels = km.fit_predict(X)        # a cluster number per row; no y!
km.cluster_centers_               # where the centres ended up
```

KMeans uses distances, so **scale first**: `make_pipeline(StandardScaler(), KMeans(...))`. Cluster numbers are just names (0, 1, 2), with no order. The useful output is describing each group in plain words: "older customers with low limits", "young, high-limit customers".

### How many clusters?

- **Inertia** (`km.inertia_`): total distance from rows to their centre. Always falls as k grows, so look for the **elbow** where the drop gets small.
- **Silhouette score** (`silhouette_score(X, labels)`, from -1 to 1): is each row much closer to its own cluster than to the next one? Higher is better.

```python
for k in range(2, 7):
    labels = KMeans(n_clusters=k, random_state=42).fit_predict(Xs)
    print(k, silhouette_score(Xs, labels))
```

Use these as guides; a k that makes business sense matters too. KMeans is also pulled around by outliers (one very slow swimmer can get a cluster to themselves).

### PCA: squeezing many columns into a few

**PCA** (principal component analysis) builds new columns that are mixes of the old ones, ordered by how much of the spread in the data they capture. Keep the first 2 and you can draw any dataset on a flat plot.

```python
from sklearn.decomposition import PCA
pipe = make_pipeline(StandardScaler(), PCA(n_components=2))
X2 = pipe.fit_transform(X)                 # (150, 2)
pipe[-1].explained_variance_ratio_         # [0.73 0.229] -> together 96% of the information
PCA(n_components=0.95)                     # "keep as many components as needed for 95%"
```

Scale before PCA, otherwise the column with the biggest numbers dominates (breast cancer unscaled: 1 component "explains" 95%, because "area" is in the thousands).

**Why it matters at work:** banks segment customers for marketing and to spot unusual behaviour; PCA plots are a quick way to see if classes separate.

### Common mistakes
- Clustering without scaling.
- Treating cluster numbers as meaningful (cluster 2 is not "more" than cluster 1).
- Choosing k only by inertia (it always prefers more clusters).
- Forgetting to remove data errors first (like `age == -1` in customers).

**Now do exercises 76–83.**

---

## Part 8: Project: a real fraud model (exercises 84–91)

This Part puts everything together the way a junior data scientist at a bank would.

### Step 1: feature engineering

**Feature engineering** = creating useful columns from raw data with pandas. Wrap it in a function so training and real use run exactly the same code:

```python
def make_features(t):
    t = t.copy()
    t["hour"] = t["timestamp"].dt.hour
    t["is_night"] = (t["hour"] <= 5).astype(int)
    t["is_foreign"] = (t["country"] != "NL").astype(int)
    t["month"] = t["timestamp"].dt.month
    t["merchant_category"] = t["merchant_category"].fillna("missing")
    return t
# fraud rate: night 3.1% vs day 1.5%; foreign 2.8% vs NL 1.7%
```

### Step 2: split by time

A bank trains on the past and uses the model on the future. So: **train on January–February, test on March.**

A random split mixes future rows into training and hides the fact that fraud patterns change. In exercise 87 the random split gives average precision 0.126 vs 0.089 for the time split: the random split is over-optimistic. Report the time-split number.

To choose a threshold honestly you need a third piece: **train (Jan) -> validation (Feb) to choose the threshold -> test (Mar) to check it once.**

### Step 3: pipeline

```python
ct = ColumnTransformer([
    ("num", StandardScaler(), ["amount_eur", "hour"]),
    ("flags", "passthrough", ["is_night", "is_foreign"]),
    ("cat", OneHotEncoder(handle_unknown="ignore"), ["channel", "merchant_category", "country"]),
])
pipe = make_pipeline(ct, LogisticRegression(class_weight="balanced", max_iter=1000))
```

### Step 4: a threshold for a business goal

"Catch 80% of fraud" is a business goal. Choose the threshold on February, then check March. Expect an uncomfortable answer: with these simple features, catching 80% means flagging more than half of all payments. A good data scientist reports that honestly ("we need better features, like customer history, or a lower target").

You can also turn errors into **money**: each missed fraud costs its amount, each alert costs €5 of analyst time. Then pick the cheapest threshold.

### Step 5: save and load

```python
import joblib, os
os.makedirs("outputs", exist_ok=True)
joblib.dump({"model": pipe, "threshold": 0.6, "columns": cols}, "outputs/fraud_model.joblib")
saved = joblib.load("outputs/fraud_model.joblib")
saved["model"].predict_proba(make_features(new)[saved["columns"]])
```

Save the threshold **with** the model so nobody uses the wrong cut-off later.

**Why it matters at work:** this is a small version of the real job: features -> honest split -> pipeline -> business threshold -> saved model.

### Common mistakes
- Random split on time-ordered data.
- Choosing the threshold on the test set.
- Retraining the model but keeping the old threshold (the probabilities shift).
- Different feature code in training and in use (that is why `make_features` is a function).

**Now do exercises 84–91.**

---

## Part 9: Judging ML code, and a final mini project (exercises 92–100)

With AI tools writing code, the valuable skill is **spotting what is wrong**. Most ML bugs do not crash: they just give a score that is too good.

### The checklist

| Bug | What it looks like | Fix |
|---|---|---|
| Preprocessing before the split | `StandardScaler().fit_transform(X)` then `train_test_split` | split first; scaler inside a pipeline |
| Tuning on the test set | a loop that keeps the best **test** score | GridSearchCV on train; test once |
| Target leakage | a feature only known **after** the event (e.g. `chargeback_filed`) | ask: "would I know this at prediction time?" Drop it |
| No stratify on rare classes | test set with 0–3 frauds; recall jumps around or is undefined | `stratify=y`, more data, StratifiedKFold |
| Unfair comparison | model A and model B tested on different splits | same CV folds for both; show mean and spread |

### Your own step: FunctionTransformer

Turn any pandas function into a pipeline step, so the pipeline accepts raw data:

```python
from sklearn.preprocessing import FunctionTransformer
def add_time_features(df):
    df = df.copy()
    df["hour"] = pd.to_datetime(df["timestamp"]).dt.hour
    df["is_night"] = (df["hour"] <= 5).astype(int)
    return df
pipe = make_pipeline(FunctionTransformer(add_time_features), ct, LogisticRegression())
```

### Learning curves: would more data help?

```python
from sklearn.model_selection import learning_curve
sizes, train_scores, val_scores = learning_curve(pipe, X, y, train_sizes=[0.1, 0.5, 1.0], cv=5)
# rows   train   validation
#  45    1.000   0.793
# 455    0.989   0.981
```

If validation is still rising, more data will probably help. If train and validation have met and flattened, it will not.

### The final mini project

Exercises 99–100 run the full process on student marks: pipeline -> compare two models with CV on the training set -> pick one -> test once -> look at the biggest errors. Looking at errors often reveals data problems: here, about a quarter of all marks are exactly 100 (capped), which hides how good the top students really are.

**Why it matters at work:** reviewing a colleague's notebook and saying "this score is leaky, here is why" is worth more than writing ten models.

### Common mistakes
- Believing a near-perfect score without asking "what could be leaking?"
- Fixing the symptom (e.g. lowering a threshold) instead of the cause (a bad split).
- Never looking at individual errors.

**Now do exercises 92–100.**
