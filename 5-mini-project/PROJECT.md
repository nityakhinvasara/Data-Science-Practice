# Mini project: catch card fraud

**What you'll build:** a model that looks at a card transaction and estimates how likely it is to be
fraud. Dutch banks like ING, Rabobank and ABN AMRO hire junior data scientists for exactly this.
At the end you'll have a clean notebook and a README you can put on GitHub and talk about in
interviews and in your Utrecht application.

**Data:** `../data/transactions.csv` (6,000 payments, ~1.9% fraud) and `../data/customers.csv` (800 customers).
**Where to work:** `fraud_project.ipynb` in this folder. It already has the sections laid out.
**Rules:** no `answer()` here. You may look back at your own exercise notebooks and the guides,
which is exactly what real data scientists do. Use AI only to explain error messages.

5 days, 1 hour each. Each step ends with **checkpoint questions**: write the answers in the notebook
as text (a markdown cell). Writing down your reasoning is half the value.

---

## Step 1 (Day 34): Explore the data
1. Load both CSVs. Print shape, `info()`, and the first rows.
2. What % of transactions are fraud? Make a bar chart of fraud vs not fraud.
3. Fraud rate by `merchant_category`, `channel` and `country` (groupby + mean of `is_fraud`).
4. Compare `amount_eur` for fraud vs not fraud (median and a histogram).
5. Convert `timestamp` to datetime. Fraud rate by hour of day: does night look different?

**Checkpoint:** Write 3 findings in plain English, like you'd tell a manager.
("Gift card purchases are X times more likely to be fraud than groceries.")

## Step 2 (Day 36): Clean and build features
1. Find the problems: missing `merchant_category`, customers with `age = -1`. Decide what to do
   with each and **write why**.
2. Merge customers into transactions (check the row count didn't change!).
3. Build features (new columns that help the model):
   - `hour`, `is_night` (0–5h), `is_foreign` (country not NL), `is_online`
   - `customer_avg_amount` (that customer's average) and `amount_vs_avg` (amount ÷ that average)
   - `n_tx_last_24h` per customer (harder: try it, it's OK if you skip it)
   - account age in days on the day of the transaction
4. Make the final table: features + `is_fraud`. No ID columns, no raw timestamp.

**Checkpoint:** Which feature do you think will matter most, and why? Is any feature "cheating",
meaning it uses information you wouldn't have at the moment of the payment?

## Step 3 (Day 37): First models
1. **Time-based split:** train on January–February, test on March. (Why not a random split?
   Write your answer.)
2. Baseline: a "model" that always says "not fraud". What's its accuracy? What's its recall?
3. Pipeline: preprocessing (OneHotEncoder for categories, scaler for numbers) + `LogisticRegression`.
4. Same pipeline with `RandomForestClassifier`.
5. For both: precision, recall, F1, ROC AUC and average precision (PR AUC) on the **test** set.

**Checkpoint:** Why is accuracy useless here? Which metric would a bank care about, and why?

## Step 4 (Day 38): Improve and choose a threshold
1. Try `class_weight="balanced"`. Did recall go up? What happened to precision?
2. Small `GridSearchCV` on the training data only (e.g. `max_depth`, `n_estimators`).
3. **Business decision:** the fraud team can check ~50 payments a week by hand. Using
   `predict_proba`, pick a threshold that fits that limit. How much fraud do you catch?
4. Which features matter most? (`permutation_importance`)
5. Save the final pipeline with `joblib` to `outputs/`.

**Checkpoint:** Explain your threshold choice to a non-technical manager in 3 sentences.

## Step 5 (Day 39): Write it up and put it on GitHub
1. Clean the notebook: delete dead cells, add a short markdown heading and one sentence of
   explanation before each section. **Restart and Run All** to be sure it works top to bottom.
2. Write `README.md` in this folder:
   - **Problem** (2 lines), **Data** (2 lines, and say it's synthetic practice data)
   - **Approach** (5 bullets), **Results** (a small table of metrics + the threshold story)
   - **What I'd do next** (3 bullets: more data, real-time features, monitoring)
   - **What I learned** (3 bullets, honest)
3. Put the project on GitHub (we'll do this together).

**You're done.** This is project #1 of the four you need before applying.
