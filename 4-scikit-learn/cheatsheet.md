# scikit-learn cheatsheet

**The pattern:** split -> `fit` on train -> `predict` / `predict_proba` -> metric on test. Preprocessing lives inside a pipeline.

## Data and splitting
| Function | What it does | Tiny example |
|---|---|---|
| `load_iris`, `load_breast_cancer`, `load_diabetes` | built-in offline datasets | `X, y = load_iris(return_X_y=True)` |
| `load_iris(as_frame=True).frame` | dataset as a DataFrame | `df = load_iris(as_frame=True).frame` |
| `train_test_split` | hide a test set | `X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, stratify=y, random_state=42)` |

## Models (all: `.fit(X, y)`, `.predict(X)`, `.score(X, y)`)
| Model | Use | Tiny example |
|---|---|---|
| `LogisticRegression` | classification, gives probabilities | `LogisticRegression(class_weight="balanced", max_iter=1000)` |
| `KNeighborsClassifier` | vote of nearest rows (scale first) | `KNeighborsClassifier(n_neighbors=5)` |
| `DecisionTreeClassifier` / `...Regressor` | yes/no questions | `DecisionTreeClassifier(max_depth=3, random_state=42)` |
| `RandomForestClassifier` / `...Regressor` | many trees voting | `RandomForestClassifier(n_estimators=200, min_samples_leaf=20, random_state=42)` |
| `LinearRegression` | regression, straight-line rule | `m.coef_`, `m.intercept_` |
| `DummyClassifier` / `DummyRegressor` | baseline to beat | `DummyClassifier(strategy="most_frequent")` |
| `predict_proba` | probability per class | `p = m.predict_proba(X_te)[:, 1]` |
| own threshold | turn probability into 0/1 | `(p >= 0.3).astype(int)` |

## Classification metrics (truth first!)
| Function | Meaning | Example |
|---|---|---|
| `accuracy_score` | share correct (useless for rare classes) | `accuracy_score(y_te, y_pred)` |
| `confusion_matrix` | `[[TN FP] [FN TP]]` | `tn, fp, fn, tp = confusion_matrix(y_te, y_pred).ravel()` |
| `precision_score` | of my alerts, share real | `precision_score(y_te, y_pred)` |
| `recall_score` | of real frauds, share caught | `recall_score(y_te, y_pred)` |
| `f1_score` | balance of the two | `f1_score(y_te, y_pred)` |
| `classification_report` | all of the above per class | `print(classification_report(y_te, y_pred))` |
| `roc_auc_score` | ranking quality, random = 0.5 | `roc_auc_score(y_te, p)` |
| `average_precision_score` | PR AUC, random = fraud rate | `average_precision_score(y_te, p)` |
| `precision_recall_curve` | precision/recall at every threshold | `prec, rec, thr = precision_recall_curve(y_te, p)` |
| `PrecisionRecallDisplay` | plot that curve | `PrecisionRecallDisplay.from_estimator(m, X_te, y_te)` |

## Regression metrics
| Function | Meaning | Example |
|---|---|---|
| `mean_absolute_error` | average miss, in real units | `mean_absolute_error(y_te, y_pred)` |
| `root_mean_squared_error` | big misses count extra | `root_mean_squared_error(y_te, y_pred)` |
| `r2_score` | 1 perfect, 0 = guessing the mean | `r2_score(y_te, y_pred)` |

## Preprocessing (fit on train only)
| Function | What it does | Example |
|---|---|---|
| `StandardScaler` | mean 0, spread 1 | `StandardScaler().fit(X_tr)` |
| `SimpleImputer` | fill missing values | `SimpleImputer(strategy="median")` |
| `OneHotEncoder` | category -> 0/1 columns | `OneHotEncoder(handle_unknown="ignore", sparse_output=False)` |
| `ColumnTransformer` | different steps per column | `ColumnTransformer([("num", StandardScaler(), ["amount_eur"]), ("cat", OneHotEncoder(handle_unknown="ignore"), ["country"])], remainder="drop")` |
| `FunctionTransformer` | your own function as a step | `FunctionTransformer(add_time_features)` |
| `get_feature_names_out()` | output column names | `ct.get_feature_names_out()` |

## Pipelines, CV, tuning
| Function | What it does | Example |
|---|---|---|
| `make_pipeline` | chain steps into one model | `pipe = make_pipeline(ct, LogisticRegression())` |
| `Pipeline` | same, with named steps | `Pipeline([("scaler", StandardScaler()), ("knn", KNeighborsClassifier())])` |
| `set_params` | change a step's setting | `pipe.set_params(knn__n_neighbors=10)` |
| `pipe[-1]` | the last step (the model) | `pipe[-1].coef_` |
| `cross_val_score` | k-fold scores | `cross_val_score(pipe, X, y, cv=5, scoring="recall")` |
| `StratifiedKFold` / `KFold` | fold splitters | `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` |
| `GridSearchCV` | try settings with CV | `GridSearchCV(pipe, {"kneighborsclassifier__n_neighbors": [3, 5, 9]}, cv=5)` |
| `.best_params_`, `.best_score_`, `.best_estimator_` | grid search results | `search.best_params_` |
| `learning_curve` | score vs amount of data | `sizes, tr, va = learning_curve(pipe, X, y, cv=5)` |

## Imbalance and importance
| Function | What it does | Example |
|---|---|---|
| `class_weight="balanced"` | rare class counts more | `RandomForestClassifier(class_weight="balanced")` |
| `feature_importances_` | tree split usage (biased) | `pd.Series(f.feature_importances_, index=X.columns)` |
| `permutation_importance` | score drop when a column is shuffled | `permutation_importance(m, X_te, y_te, n_repeats=5, random_state=42)` |

## Unsupervised
| Function | What it does | Example |
|---|---|---|
| `KMeans` | k groups (scale first) | `KMeans(n_clusters=3, random_state=42).fit_predict(Xs)` |
| `.inertia_` | tightness, look for the elbow | `km.inertia_` |
| `silhouette_score` | cluster quality, -1..1 | `silhouette_score(Xs, labels)` |
| `PCA` | squeeze to fewer columns | `PCA(n_components=2)`, `PCA(n_components=0.95)` |
| `.explained_variance_ratio_` | info kept per component | `pca.explained_variance_ratio_` |

## Saving
| Function | What it does | Example |
|---|---|---|
| `joblib.dump` / `joblib.load` | save / load a fitted model | `joblib.dump({"model": pipe, "threshold": 0.6}, "outputs/model.joblib")` |

## Red flags (spot the bug)
- `fit` / `fit_transform` on all data or on test -> leakage. Use a pipeline.
- Picking settings or thresholds by test score -> use CV / a validation set.
- A feature known only after the event -> target leakage.
- Rare class without `stratify=y` -> unstable or undefined metrics.
- Models compared on different splits -> use the same CV folds.
- Accuracy on imbalanced data -> use recall, precision, average precision.
- Random split on time data -> train on past, test on future.
