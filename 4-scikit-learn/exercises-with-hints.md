# scikit-learn: 100 exercises (hints)

_Generated from `tools/source/sklearn.ktx`. Don't edit this file; it gets rebuilt._


## Level 1: Easy

#### 1. Import scikit-learn and print its version. (The package is installed as `scikit-learn` but you import it as `sklearn`.) (★☆☆)

`hint:` `import sklearn` then `sklearn.__version__`

#### 2. Load the built-in **iris** flower dataset with `load_iris()`. Print the shape of `iris.data` (the features X) and of `iris.target` (the labels y). (★☆☆)

`hint:` `from sklearn.datasets import load_iris`; then `.shape`

#### 3. Print the feature names and the target names (species) of the iris dataset. Then print the first flower's 4 measurements and its species *name*. (★☆☆)

`hint:` `iris.feature_names`, `iris.target_names`; use the number in `iris.target[0]` as an index into `target_names`

#### 4. Load iris as a pandas DataFrame with `load_iris(as_frame=True)`. Print the first 5 rows of `.frame` and count how many flowers there are of each class. (★☆☆)

`hint:` `.frame.head()` and `value_counts()` on the `"target"` column

#### 5. Load the **breast cancer** dataset as `X, y` in one line with `return_X_y=True`. Print the shapes and how many samples there are of each class. (In this dataset 0 = malignant, 1 = benign.) (★☆☆)

`hint:` `load_breast_cancer(return_X_y=True)`; count classes with `np.bincount(y)`

#### 6. Load the **diabetes** dataset with `return_X_y=True`. Print the first 5 values of `y` and the min and max of `y`. In a comment, say whether this is a classification or a regression problem, and why. (★☆☆)

`hint:` `load_diabetes`. Is `y` a small set of categories or any number on a scale?

#### 7. Load `../data/student_marks.csv`. Build `X` from the columns `study_hours_per_week`, `attendance_pct`, `previous_cgpa`, and `y` from `final_marks`. Print the shapes of `X` and `y`. (★☆☆)

`hint:` Double brackets `df[[...]]` give a 2-D DataFrame (X), single brackets give a 1-D Series (y)

#### 8. Split iris into a training set and a test set with `train_test_split`, keeping 25% for testing and `random_state=42`. Print the shapes of all four pieces. (★☆☆)

`hint:` `from sklearn.model_selection import train_test_split`; it returns `X_train, X_test, y_train, y_test` in that order

#### 9. Split iris twice with `test_size=0.2, random_state=0`: once normally and once with `stratify=y`. For each, print how many test flowers are in each class. What does `stratify` do? (★☆☆)

`hint:` `np.bincount(y_test)` counts each class

#### 10. Train your first model: a `KNeighborsClassifier` on the iris training set (`test_size=0.25, random_state=42`). Predict the species of the first 5 test flowers and print them next to the true answers. (★☆☆)

`hint:` `model = KNeighborsClassifier()`, then `model.fit(X_train, y_train)` and `model.predict(X_test[:5])`

#### 11. On the same iris split, train a `KNeighborsClassifier` and a `LogisticRegression(max_iter=1000)`. Print the test score of each with `.score(X_test, y_test)`. What does `.score` measure for a classifier? (★☆☆)

`hint:` `from sklearn.linear_model import LogisticRegression`; `.score` on a classifier returns accuracy

#### 12. Using student marks (X = study hours, attendance, previous CGPA; y = final marks), split 80/20 with `random_state=42` and train a `LinearRegression`. Print the test score, and print each coefficient next to its feature name, plus the intercept. (★☆☆)

`hint:` `model.coef_`, `model.intercept_`; `zip(X.columns, model.coef_)`. For regression `.score` is R² (1 = perfect, 0 = no better than guessing the average)

#### 13. Use the model from exercise 12 (retrain it on the full data this time) to predict the final marks of a new student who studies 15 hours a week, has 90% attendance and a previous CGPA of 8.0. (★☆☆)

`hint:` Put the new student in a one-row DataFrame with the **same column names** as X

#### 14. Train a `KNeighborsClassifier` on breast cancer (`test_size=0.25, random_state=42, stratify=y`). Compute the accuracy twice: with `accuracy_score`, and by hand as the share of predictions equal to the truth. They should match. (★☆☆)

`hint:` `from sklearn.metrics import accuracy_score`; by hand: `(y_pred == y_test).mean()`

#### 15. For the same model as exercise 14, print the `confusion_matrix`. In comments, explain what each of the four numbers means here (0 = malignant, 1 = benign). (★☆☆)

`hint:` `from sklearn.metrics import confusion_matrix`; rows = true class, columns = predicted class

#### 16. Here are 10 true labels and 10 predictions for "is this fraud?" (1 = fraud). Print the confusion matrix, then unpack it into `tn, fp, fn, tp` and print each. (★☆☆)
```python
y_true = [0, 0, 0, 1, 0, 1, 0, 0, 1, 0]
y_pred = [0, 1, 0, 1, 0, 0, 0, 0, 1, 1]
```

`hint:` `tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()`

#### 17. Load `../data/transactions.csv`. Print the number of transactions, the number of frauds, and the fraud rate in percent. (★☆☆)

`hint:` `is_fraud` is 0/1, so `.sum()` counts frauds and `.mean()` gives the rate

#### 18. A lazy "model" says *no transaction is ever fraud*. Make `y_pred` all zeros and print its accuracy on the whole transactions file. Then print how many frauds it caught. Why is accuracy misleading here? (★☆☆)

`hint:` `np.zeros(len(t), dtype=int)`; caught frauds = rows where both truth and prediction are 1

#### 19. Do exercise 18 the proper way: split transactions (X = `amount_eur` only, y = `is_fraud`, `test_size=0.25`, `stratify=y`, `random_state=42`) and fit a `DummyClassifier(strategy="most_frequent")`. Print its test accuracy. This is your **baseline**: any real model must beat it. (★☆☆)

`hint:` `from sklearn.dummy import DummyClassifier`

#### 20. Using the labels from exercise 16, compute precision and recall with `precision_score` and `recall_score`. Then compute both by hand from `tp`, `fp` and `fn` and check they match. (★☆☆)

`hint:` precision = tp / (tp + fp): of the alerts, how many were fraud? recall = tp / (tp + fn): of the frauds, how many did we catch?

#### 21. Still with the labels from exercise 16, compute the F1 score with `f1_score`. Check it against the formula `2 * p * r / (p + r)`. In a comment, say when F1 is useful. (★☆☆)

`hint:` `from sklearn.metrics import f1_score`

#### 22. Print a `classification_report` for the breast cancer KNN model from exercise 14, using `target_names=["malignant", "benign"]`. (★☆☆)

`hint:` `from sklearn.metrics import classification_report`; wrap it in `print()`

#### 23. Train a `LogisticRegression` on the transactions split from exercise 19 (X = `amount_eur` only). Print its test accuracy and its recall for fraud. Compare with the dummy baseline (~0.981). (★☆☆)

`hint:` `recall_score(y_test, y_pred)` measures recall for class 1 (fraud) by default

#### 24. Retrain the student marks `LinearRegression` from exercise 12. Compute the **mean absolute error (MAE)** on the test set. What does the number mean in plain words? (★☆☆)

`hint:` `from sklearn.metrics import mean_absolute_error`

#### 25. For the same model, compute the **root mean squared error (RMSE)** with `root_mean_squared_error`. Why is RMSE usually bigger than MAE? (★☆☆)

`hint:` `from sklearn.metrics import root_mean_squared_error`

#### 26. For the same model, compute R² with `r2_score` and check it equals `model.score(X_test, y_test)`. (★☆☆)

`hint:` `from sklearn.metrics import r2_score`

#### 27. Make a regression baseline: `DummyRegressor(strategy="mean")` always predicts the average training mark. Compare its test MAE with the `LinearRegression` MAE on the same split. (★☆☆)

`hint:` `from sklearn.dummy import DummyRegressor`

#### 28. Train a `DecisionTreeClassifier(random_state=42)` on iris (`test_size=0.25, random_state=42`) and print its test accuracy. (★☆☆)

`hint:` `from sklearn.tree import DecisionTreeClassifier`

#### 29. Train a `DecisionTreeClassifier(random_state=42)` with no depth limit on breast cancer (`test_size=0.25, stratify=y, random_state=42`). Print the **training** accuracy and the **test** accuracy. What does the gap tell you? (★☆☆)

`hint:` Call `.score` on both `X_train, y_train` and `X_test, y_test`

#### 30. On the same breast cancer split, loop over `max_depth` in `[1, 2, 3, 5, None]`. For each, print the train and test accuracy. Which depth looks best? (★☆☆)

`hint:` `DecisionTreeClassifier(max_depth=d, random_state=42)`

#### 31. Train a tree with `max_depth=2` on the full iris data and print its rules with `export_text`, using the real feature names. (★☆☆)

`hint:` `from sklearn.tree import export_text`; `export_text(tree, feature_names=iris.feature_names)`

#### 32. Train a `RandomForestClassifier(n_estimators=100, random_state=42)` on the breast cancer split and print train and test accuracy. Compare with the single tree from exercise 29. (★☆☆)

`hint:` `from sklearn.ensemble import RandomForestClassifier`

#### 33. Compare four models on the same breast cancer split: `LogisticRegression(max_iter=5000)`, `KNeighborsClassifier()`, `DecisionTreeClassifier(random_state=42)`, `RandomForestClassifier(random_state=42)`. Store them in a dict `{name: model}` and print each test accuracy. (★☆☆)

`hint:` Loop over `models.items()`; fit and score each on the **same** split so the comparison is fair

#### 34. Train a `LogisticRegression(max_iter=5000)` on the breast cancer split. Print `predict_proba` for the first 5 test rows, rounded to 3 decimals, and print `model.classes_`. What do the two columns mean? (★☆☆)

`hint:` `model.predict_proba(X_test[:5]).round(3)`

#### 35. Show that `predict` is just "probability of class 1 is at least 0.5". Take column 1 of `predict_proba`, make your own predictions with `>= 0.5`, and check they equal `model.predict(X_test)` for every row. (★☆☆)

`hint:` `proba = model.predict_proba(X_test)[:, 1]`; `(proba >= 0.5).astype(int)`

#### 36. On the iris split (`test_size=0.25, random_state=42`), train `KNeighborsClassifier` with `n_neighbors` = 1, 5 and 25. Print train and test accuracy for each. Which one memorises the training data? (★☆☆)

`hint:` `KNeighborsClassifier(n_neighbors=k)`

#### 37. On student marks (3 features as before, 80/20, `random_state=42`), compare the test MAE of `LinearRegression` and `DecisionTreeRegressor(max_depth=3, random_state=42)`. (★☆☆)

`hint:` `from sklearn.tree import DecisionTreeRegressor`: same idea as the classifier, but each leaf predicts an average number

#### 38. On the diabetes dataset (`test_size=0.25, random_state=42`), compare the test R² of `LinearRegression` and `RandomForestRegressor(n_estimators=100, random_state=42)`. (★☆☆)

`hint:` `from sklearn.ensemble import RandomForestRegressor`

#### 39. Predict swim times. Load `../data/swim_results.csv`, keep only rows with `status == "OK"`, and use `distance_m` and `pool_length_m` as X and `time_sec` as y. Train a `LinearRegression` (80/20, `random_state=42`) and print the test MAE in seconds and the two coefficients. (★☆☆)

`hint:` Filter with a boolean mask first: DQ rows have no time

#### 40. Build two simple fraud features with pandas: `amount_eur` and `online` (1 if `channel == "online"`, else 0). Train a `RandomForestClassifier(random_state=42)` (`test_size=0.25, stratify=y, random_state=42`) and print accuracy and fraud recall. (★☆☆)

`hint:` `(t["channel"] == "online").astype(int)`


## Level 2: Medium

#### 41. Scale a small array with `StandardScaler`. Print the scaled array, and the scaler's learned `mean_` and `scale_`. Check that each scaled column now has mean 0 and standard deviation 1. (★★☆)
```python
X = np.array([[10, 200], [20, 400], [30, 600], [40, 800]])
```

`hint:` `from sklearn.preprocessing import StandardScaler`; `fit_transform`, then `.mean(axis=0)` and `.std(axis=0)`

#### 42. Split breast cancer (`test_size=0.25, stratify=y, random_state=42`). Fit a `StandardScaler` on `X_train` only, then transform both sets. Print the mean of the first column in scaled train and scaled test. Why is the test mean not exactly 0, and why is that correct? (★★☆)

`hint:` `scaler.fit(X_train)` then `scaler.transform(X_test)`: never `fit` on test

#### 43. KNN measures distance between rows, so big-number features dominate. On the breast cancer split, compare KNN test accuracy **without** scaling and **with** a `StandardScaler` fitted on train. (★★☆)

`hint:` Fit the scaler on train, transform both, then train KNN on the scaled data

#### 44. In student marks, `sleep_hours` has missing values. Use `SimpleImputer(strategy="median")` to fill them. Print the number of missing values before and after, and the value the imputer learned. (★★☆)

`hint:` `from sklearn.impute import SimpleImputer`; it needs 2-D input, so use `df[["sleep_hours"]]`; learned value is in `.statistics_`

#### 45. In transactions, `merchant_category` has 30 missing values. Fill them with the most common category using `SimpleImputer(strategy="most_frequent")`. Print which value it used. (★★☆)

`hint:` `most_frequent` also works on text columns

#### 46. One-hot encode the `channel` column of transactions with `OneHotEncoder(sparse_output=False)`. Print the column names it creates (`get_feature_names_out()`) and the first 5 encoded rows. (★★☆)

`hint:` `from sklearn.preprocessing import OneHotEncoder`; input must be 2-D: `t[["channel"]]`

#### 47. Fit a `OneHotEncoder` on countries `["NL", "DE", "NL", "BE"]`, then transform `["NL", "US"]`. First try it with default settings (it raises an error, catch it with `try/except` and print the message), then with `handle_unknown="ignore"`. (★★☆)

`hint:` Put each list in a DataFrame with one column `"country"`; `handle_unknown="ignore"` turns an unseen category into all zeros

#### 48. Why use `OneHotEncoder` instead of `pd.get_dummies`? Run `pd.get_dummies` separately on a train and a test DataFrame of channels, and print both column lists. Then show that `OneHotEncoder` fitted on train gives the same columns for test. (★★☆)
```python
train = pd.DataFrame({"channel": ["online", "in_store", "contactless", "online"]})
test = pd.DataFrame({"channel": ["online", "online"]})
```

`hint:` The encoder *remembers* the categories it saw during `fit`; `get_dummies` only sees what is in front of it

#### 49. Use a `ColumnTransformer` on student marks to: scale `study_hours_per_week`, `attendance_pct`, `previous_cgpa`; median-impute `sleep_hours`; and one-hot encode `favourite_subject`. Fit it on the whole DataFrame and print the output shape and the output column names. (★★☆)

`hint:` `from sklearn.compose import ColumnTransformer`; give a list of `(name, transformer, columns)` tuples

#### 50. Build a `ColumnTransformer` for transactions: scale `amount_eur` and one-hot encode `merchant_category`, `channel`, `country`. First replace missing `merchant_category` with the text `"missing"` using pandas. Print the output shape. (★★☆)

`hint:` `t["merchant_category"].fillna("missing")`

#### 51. Repeat the student marks `ColumnTransformer` with only the scaling step for `study_hours_per_week` and `attendance_pct`, but set `remainder="passthrough"` for `part_time_job` (pass in only these three columns). Print the output names. What does `remainder` control? (★★☆)

`hint:` `ColumnTransformer([...], remainder="passthrough")`

#### 52. Everyone in this file passed, so make a new target: `distinction = (final_marks >= 90)`. Split student marks 80/20 (`stratify=y, random_state=42`). Fit the `ColumnTransformer` from exercise 49 on the training set only, transform both sets, train a `LogisticRegression`, and print the test accuracy. (★★☆)

`hint:` `ct.fit_transform(X_train)`, then `ct.transform(X_test)`

#### 53. Build a pipeline with `make_pipeline(StandardScaler(), KNeighborsClassifier())`. Fit it on the breast cancer training set (`test_size=0.25, stratify=y, random_state=42`) and print the test accuracy. Compare with exercise 43. (★★☆)

`hint:` `from sklearn.pipeline import make_pipeline`; a pipeline has `.fit`, `.predict`, `.score` like any model

#### 54. Build the same thing with `Pipeline([("scaler", ...), ("knn", ...)])` so the steps have your own names. Print `pipe.named_steps`, then change the number of neighbours to 10 with `set_params(knn__n_neighbors=10)`, refit and print the test accuracy. (★★☆)

`hint:` `from sklearn.pipeline import Pipeline`; step name + two underscores + parameter name

#### 55. Redo exercise 52 as **one** pipeline: `ColumnTransformer` + `LogisticRegression`. Fit on train, print test accuracy, then predict the distinction probability for this new student: (★★☆)
```python
new = pd.DataFrame([{"study_hours_per_week": 18, "attendance_pct": 92, "sleep_hours": 7.5,
                     "previous_cgpa": 8.4, "part_time_job": 0, "favourite_subject": "Python"}])
```

`hint:` `make_pipeline(ct, LogisticRegression())`; raw DataFrame in, prediction out

#### 56. A column can need two steps (first impute, then encode). Make a small pipeline `make_pipeline(SimpleImputer(strategy="most_frequent"), OneHotEncoder(handle_unknown="ignore"))` and use it as the transformer for `merchant_category` inside a `ColumnTransformer` (scale `amount_eur` too). Fit on transactions and print the output shape. (★★☆)

`hint:` A pipeline can be used anywhere a transformer is expected, including inside a `ColumnTransformer`

#### 57. Use `cross_val_score` with `cv=5` on iris with a `KNeighborsClassifier`. Print the 5 scores, their mean and their standard deviation. (★★☆)

`hint:` `from sklearn.model_selection import cross_val_score`; it returns an array of scores

#### 58. Why cross-validate? Split breast cancer 5 times with `random_state` 0 to 4 (`test_size=0.25`), train a `DecisionTreeClassifier(random_state=42)` each time, and print the 5 test accuracies. (★★☆)

`hint:` Loop over `range(5)` and pass the loop variable as `random_state` to `train_test_split`

#### 59. Iris rows are sorted by species (all 0s, then 1s, then 2s). Run `cross_val_score` on a `LogisticRegression(max_iter=1000)` with `cv=KFold(n_splits=3)` (no shuffle), then with `KFold(n_splits=3, shuffle=True, random_state=42)`. Explain the first result. (★★☆)

`hint:` `from sklearn.model_selection import KFold`

#### 60. For transactions, count the frauds in each test fold of `KFold(n_splits=5, shuffle=True, random_state=1)` and of `StratifiedKFold(n_splits=5, shuffle=True, random_state=1)`. Which gives more even folds? (★★☆)

`hint:` `for train_idx, test_idx in cv.split(X, y):` then `y.iloc[test_idx].sum()`

#### 61. Score a fraud model with cross-validation using **recall**, not accuracy. Features: `amount_eur` and `online` (as in exercise 40). Model: `make_pipeline(StandardScaler(), LogisticRegression(class_weight="balanced"))`. Use `StratifiedKFold(5, shuffle=True, random_state=42)` and print the recall per fold and the mean. (`class_weight` is explained in Part 6: for now, it makes the model take fraud seriously.) (★★☆)

`hint:` `cross_val_score(pipe, X, y, cv=cv, scoring="recall")`

#### 62. Use `GridSearchCV` to choose `n_neighbors` from `[1, 3, 5, 7, 9, 15]` for a `make_pipeline(StandardScaler(), KNeighborsClassifier())` on the breast cancer **training** set (`cv=5`). Print `best_params_` and `best_score_`. (★★☆)

`hint:` `from sklearn.model_selection import GridSearchCV`; with `make_pipeline` the step name is the class name in lowercase: `kneighborsclassifier__n_neighbors`

#### 63. Grid-search a `DecisionTreeClassifier(random_state=42)` on the breast cancer training set over `max_depth` in `[2, 3, 4, 6]` and `min_samples_leaf` in `[1, 5, 10]` (`cv=5`). Print the best parameters, then score `best_estimator_` **once** on the test set. (★★☆)

`hint:` The grid has 4 x 3 = 12 combinations; `search.best_estimator_` is already refitted on all training data

#### 64. **Leakage demo.** Make pure noise: `X = rng.normal(size=(100, 2000))` and random labels `y = rng.integers(0, 2, 100)` with `rng = np.random.default_rng(42)`. There is nothing to learn, so honest accuracy should be about 0.5. (★★☆)
(a) Pick the 20 "best" columns with `SelectKBest(k=20)` on **all** the data, then cross-validate a `LogisticRegression` on those columns.
(b) Put `SelectKBest` **inside** a pipeline and cross-validate that. Compare.

`hint:` `from sklearn.feature_selection import SelectKBest`: it keeps the k columns most related to y

#### 65. From now on, use these fraud features (copy this block): (★★☆)
```python
t = pd.read_csv("../data/transactions.csv", parse_dates=["timestamp"])
t["hour"] = t["timestamp"].dt.hour
t["is_night"] = (t["hour"] <= 5).astype(int)
t["is_foreign"] = (t["country"] != "NL").astype(int)
t["is_online"] = (t["channel"] == "online").astype(int)
X = t[["amount_eur", "hour", "is_night", "is_foreign", "is_online"]]
y = t["is_fraud"]
```
Split (`test_size=0.25, stratify=y, random_state=42`). Train `make_pipeline(StandardScaler(), LogisticRegression())` with and without `class_weight="balanced"`. Print accuracy and fraud recall for both.

`hint:` `LogisticRegression(class_weight="balanced")` makes each fraud count about 50x more during training

#### 66. For the two models in exercise 65, print the confusion matrix of each. How many extra false alarms did the balanced model raise to catch its frauds? (★★☆)

`hint:` `confusion_matrix(y_test, y_pred)`; false alarms are top-right, caught frauds bottom-right

#### 67. Same features and split as exercise 65. Train `RandomForestClassifier(n_estimators=200, min_samples_leaf=30, class_weight="balanced", random_state=42)` and print precision and recall for fraud. Compare with the balanced logistic regression. (★★☆)

`hint:` `min_samples_leaf=30` stops trees from making tiny leaves that memorise single frauds

#### 68. Use the balanced logistic regression from exercise 65. Instead of `predict`, take the fraud probability and try thresholds `0.3, 0.5, 0.7`. For each, print the number of alerts, precision and recall. (★★☆)

`hint:` `proba = pipe.predict_proba(X_test)[:, 1]`; `y_pred = (proba >= thr).astype(int)`

#### 69. Find the highest threshold that still catches at least 80% of fraud on the test set of exercise 68, using `precision_recall_curve`. Print the threshold, its precision and its recall. (In Part 8 you will do this properly on a separate validation set.) (★★☆)

`hint:` `precision, recall, thresholds = precision_recall_curve(y_test, proba)`; `precision` and `recall` have one more element than `thresholds`, so drop the last one

#### 70. Compute the **ROC AUC** of the balanced logistic regression (exercise 65) with `roc_auc_score` on the fraud probabilities. Also compute it for random scores `rng.random(len(y_test))` (`rng = np.random.default_rng(42)`). What does each number mean? (★★☆)

`hint:` `from sklearn.metrics import roc_auc_score`; pass probabilities, not 0/1 predictions

#### 71. For the same model, compute **average precision** (PR AUC) with `average_precision_score`. Compare it with the fraud rate in `y_test`, which is what random scores would get. Why does it look much worse than the ROC AUC? (★★☆)

`hint:` `from sklearn.metrics import average_precision_score`

#### 72. Plot the precision-recall curve of the balanced logistic regression with `PrecisionRecallDisplay.from_estimator(pipe, X_test, y_test)`. Save it to `outputs/pr_curve.png`. (★★☆)

`hint:` `from sklearn.metrics import PrecisionRecallDisplay`; `plt.savefig(...)` after `os.makedirs("outputs", exist_ok=True)`

#### 73. Train the random forest from exercise 67 and print its `feature_importances_` as a pandas Series with feature names, sorted from most to least important. (★★☆)

`hint:` `pd.Series(forest.feature_importances_, index=X.columns).sort_values(ascending=False)`

#### 74. Now measure importance the more trustworthy way: `permutation_importance` on the **test** set (`n_repeats=5, random_state=42, scoring="average_precision"`) for the same forest. Print the mean importances sorted. Do they agree with exercise 73? (★★☆)

`hint:` `from sklearn.inspection import permutation_importance`; results are in `.importances_mean`

#### 75. Another view of importance: in a logistic regression on **scaled** features, the size of each coefficient shows how strongly a feature pushes towards fraud. Fit the balanced logistic pipeline from exercise 65 and print its coefficients with names, sorted. Why must the features be scaled for this comparison to be fair? (★★☆)

`hint:` `pipe[-1].coef_[0]` gets the coefficients of the last step


## Level 3: Hard

#### 76. Make 300 points in 3 groups with `make_blobs(n_samples=300, centers=3, random_state=42)`. Cluster them with `KMeans(n_clusters=3, random_state=42)`. Print the cluster centres and how many points ended up in each cluster. (★★★)

`hint:` `from sklearn.cluster import KMeans`; `fit_predict(X)` returns a cluster number per row; no `y` is used

#### 77. Group bank customers. Load `../data/customers.csv`, drop rows with `age == -1` (data-entry errors), and cluster on `age` and `credit_limit_eur` with a pipeline `make_pipeline(StandardScaler(), KMeans(n_clusters=3, random_state=42))`. Add the cluster as a column and print the mean age, mean credit limit and size of each cluster. (★★★)

`hint:` `pipe.fit_predict(X)`; then `groupby("cluster").agg(...)`

#### 78. How many clusters? For the scaled customer data of exercise 77, fit KMeans for k = 1 to 8 and print the `inertia_` for each. Where does the drop flatten out (the "elbow")? (★★★)

`hint:` Scale once with `StandardScaler().fit_transform(X)`, then loop over k

#### 79. Use the **silhouette score** to choose k for the same scaled customer data. Try k = 2 to 6, print each score, and print the best k. (★★★)

`hint:` `from sklearn.metrics import silhouette_score`; `silhouette_score(Xs, labels)`; higher is better

#### 80. Group swimmers by performance. From `../data/swim_results.csv`: keep `status == "OK"`, clean the event names with `.str.strip().str.title()`, and keep `"50 Free"` only. Per swimmer, compute the best time and the number of races. Cluster swimmers into 3 groups (scale first, `random_state=42`) and print each group's mean best time, mean races and size. (★★★)

`hint:` `groupby("swimmer_id")["time_sec"].agg(best="min", races="count")`; then the same scale + KMeans pipeline as exercise 77

#### 81. Reduce iris from 4 features to 2 with `PCA(n_components=2)`. Print the new shape and `explained_variance_ratio_`. How much of the information do the 2 new columns keep? (★★★)

`hint:` `from sklearn.decomposition import PCA`; scale first with a pipeline

#### 82. Make a 2-D scatter plot of iris after PCA (exercise 81), coloured by species. Add axis labels and save it to `outputs/iris_pca.png`. (★★★)

`hint:` `plt.scatter(X2[:, 0], X2[:, 1], c=y)`

#### 83. Breast cancer has 30 features. How many PCA components do you need to keep 95% of the variance? Use `PCA(n_components=0.95)` after scaling and print the number of components. Then try without scaling and explain the difference. (★★★)

`hint:` A number between 0 and 1 for `n_components` means "keep this share of variance"; the result is in `.n_components_`

#### 84. **Fraud project, step 1: features.** Write a function `make_features(t)` that takes the raw transactions DataFrame and returns a copy with: `hour`, `is_night` (hour 0–5), `is_foreign` (country not NL), `month`, and `merchant_category` with missing values filled as `"missing"`. Apply it, then print the fraud rate grouped by `is_night` and by `is_foreign`. (★★★)

`hint:` Parse dates with `parse_dates=["timestamp"]`; use `.dt.hour` and `.dt.month`; return `t.assign(...)` or work on `t.copy()`

#### 85. **Step 2: time-based split.** Using `make_features` from exercise 84, put January and February in `train` and March in `test`. Print the number of rows and frauds in each. In a comment, explain why this is more honest than a random split for fraud. (★★★)

`hint:` `train = t[t["month"] <= 2]`, `test = t[t["month"] == 3]`

#### 86. **Step 3: pipeline.** Build a `ColumnTransformer` that scales `amount_eur` and `hour`, passes through `is_night` and `is_foreign`, and one-hot encodes `channel`, `merchant_category` and `country`. Put it in a pipeline with `LogisticRegression(class_weight="balanced", max_iter=1000)`. Train on Jan–Feb, and on March print the average precision, the ROC AUC and the fraud rate. (★★★)

`hint:` Use `"passthrough"` as the transformer for columns that are already ready

#### 87. Compare the time split with a random split of the **same size** (`test_size=len(test)`, `stratify`, `random_state=42`) for the pipeline from exercise 86. Print the average precision for both. Which is more optimistic, and why should you report the time-split number? (★★★)

`hint:` `train_test_split(t, test_size=len(test), stratify=t["is_fraud"], random_state=42)` splits whole rows of the DataFrame

#### 88. Swap the logistic regression in the exercise 86 pipeline for `RandomForestClassifier(n_estimators=200, min_samples_leaf=20, class_weight="balanced", random_state=42)`. On the time split, print average precision for both models. Which would you pick? (★★★)

`hint:` Keep the same `ColumnTransformer`; scaling does not hurt the forest. Loop over a dict of models

#### 89. **Step 4: threshold for a business goal.** The bank wants to catch at least 80% of fraud. Choosing the threshold on the March test set would be cheating, so: train on **January**, choose the threshold on **February** (the validation set), then use that same model and threshold on **March** (the test set). Print the threshold, and March's recall, precision, number of alerts and share of transactions flagged. (★★★)

`hint:` Three time periods: train (Jan), validation (Feb), test (Mar). Use `precision_recall_curve` on February like exercise 69

#### 90. Make the threshold choice about money. Assume each missed fraud costs the bank its `amount_eur`, and each alert costs €5 for an analyst to check. On February (model trained on January, as in exercise 89), compute the total cost for thresholds `0.3, 0.4, ..., 0.9` and print the cheapest. (★★★)

`hint:` cost = (amounts of frauds with prediction 0).sum() + 5 * number of alerts. `np.arange(0.3, 0.91, 0.1)`

#### 91. **Step 5: save and reuse.** Train the exercise 86 pipeline on Jan–Feb and save it together with a threshold of 0.6 to `outputs/fraud_model.joblib` as a dict. Then load it back and score these two new transactions, printing the probability and an alert flag: (★★★)
```python
new = pd.DataFrame({
    "timestamp": pd.to_datetime(["2025-04-01 03:12:00", "2025-04-01 12:30:00"]),
    "merchant_category": ["electronics", "groceries"], "channel": ["online", "in_store"],
    "country": ["RU", "NL"], "amount_eur": [899.0, 23.5]})
```

`hint:` `import joblib`; `joblib.dump(obj, path)` and `joblib.load(path)`; run `make_features` on the new rows too

#### 92. **Spot the bug.** A colleague wrote this. What is wrong, why does it matter, and how do you fix it? Write the fixed version. (★★★)
```python
X, y = load_breast_cancer(return_X_y=True)
X = StandardScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, stratify=y, random_state=42)
model = LogisticRegression().fit(X_train, y_train)
print(model.score(X_test, y_test))
```

`hint:` Which rows did the scaler learn its mean and standard deviation from?

#### 93. **Spot the bug.** What is wrong with this way of choosing `k`, and what does the final printed number really mean? Write a fixed version. (★★★)
```python
best_k, best = None, 0
for k in range(1, 31):
    pipe = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=k)).fit(X_train, y_train)
    s = pipe.score(X_test, y_test)
    if s > best:
        best_k, best = k, s
print("k =", best_k, "test accuracy =", best)
```
(Data: breast cancer, `test_size=0.25, stratify=y, random_state=42`.)

`hint:` If you pick the best of 30 scores on the test set, is that score still a fair guess for new data?

#### 94. **Why is this result too good to be true?** The bank's data team added a column `chargeback_filed` (did the customer later dispute the payment?). A model using it scores almost perfectly. Run it, explain the problem, and show the honest score without it. (★★★)
```python
rng = np.random.default_rng(42)
t = pd.read_csv("../data/transactions.csv")
t["is_online"] = (t["channel"] == "online").astype(int)
# a dispute is filed weeks AFTER the payment, for almost every fraud
t["chargeback_filed"] = np.where(t["is_fraud"] == 1, rng.random(len(t)) < 0.95, rng.random(len(t)) < 0.003).astype(int)
X = t[["amount_eur", "is_online", "chargeback_filed"]]
```

`hint:` Would you know this column's value at the moment the card is swiped?

#### 95. **Why is this misleading?** A colleague evaluates on a small sample: the first 500 transactions, split 80/20 **without** `stratify`. Show how many frauds land in the test set for `random_state` 0 to 4, and what fraud recall is when the test set has no frauds at all. Then fix it. (★★★)

`hint:` `y_test.sum()` for each seed; `recall_score(..., zero_division=0)` when there are no frauds

#### 96. **Unfair comparison.** A colleague says "the forest beats logistic regression": they trained logistic regression (with scaling) on a split with `random_state=0` and the forest on a split with `random_state=10` (breast cancer, `test_size=0.25`). Show the two numbers, explain the problem, then compare both models fairly with `cross_val_score` on the **same** `StratifiedKFold(5, shuffle=True, random_state=42)`. (★★★)

`hint:` Create one `cv` object and pass it to both `cross_val_score` calls

#### 97. Turn your feature code into a pipeline step with `FunctionTransformer`, so the pipeline accepts the **raw** transactions (timestamp as text). Write `add_time_features(df)` that parses `timestamp` and adds `hour` and `is_night`, then use `make_pipeline(FunctionTransformer(add_time_features), ColumnTransformer(...), LogisticRegression(...))`. Train on a stratified 75/25 split of the raw file and print the average precision. (★★★)

`hint:` `from sklearn.preprocessing import FunctionTransformer`; the function receives a DataFrame and must return one

#### 98. Draw a **learning curve**: does more data help? Use `learning_curve` on breast cancer with `make_pipeline(StandardScaler(), LogisticRegression())`, `train_sizes=[0.1, 0.25, 0.5, 0.75, 1.0]`, `cv=5`. Print the number of training rows and the mean train and validation score for each size. (★★★)

`hint:` `from sklearn.model_selection import learning_curve`; it returns `sizes, train_scores, val_scores`; average each row with `.mean(axis=1)`

#### 99. **Mini project, part 1.** Predict `final_marks` from all useful columns of student marks (`study_hours_per_week`, `attendance_pct`, `sleep_hours`, `previous_cgpa`, `part_time_job`, `favourite_subject`). Hold out 20% as a test set (`random_state=42`). On the training set only, compare `LinearRegression` and `RandomForestRegressor(n_estimators=200, min_samples_leaf=5, random_state=42)` with 5-fold cross-validated MAE, using the same preprocessing pipeline for both. Print the mean CV MAE of each. (★★★)

`hint:` `scoring="neg_mean_absolute_error"` (sklearn wants "higher is better", so it gives MAE with a minus sign; flip it back)

#### 100. **Mini project, part 2.** Take the model with the lower CV MAE from exercise 99, fit it on the full training set, and report its test MAE **once**. Then print the 5 test students with the biggest errors (true mark, predicted mark, error). Look at their true marks: what pattern do you notice, and what does it say about the data? (★★★)

`hint:` Put `y_test`, the predictions and `abs(error)` in a DataFrame and use `.nlargest(5, "abs_error")`. How many students have exactly 100?
