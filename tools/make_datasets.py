"""Creates the practice datasets in ../data/.

You never need to run this: the CSV files are already there.
Run it only if you delete or break a CSV:  python tools/make_datasets.py
Everything is random but with a fixed seed, so the files come out identical every time.
"""
from pathlib import Path

import numpy as np
import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "data"
DATA.mkdir(exist_ok=True)
rng = np.random.default_rng(2024)

# ---------------------------------------------------------------- swimmers
first = ["Aarav", "Diya", "Kabir", "Ananya", "Vihaan", "Isha", "Arjun", "Meera", "Rohan", "Sara",
         "Aditya", "Tara", "Kiran", "Nisha", "Dev", "Riya", "Omkar", "Pooja", "Yash", "Sneha",
         "Neil", "Aisha", "Varun", "Kavya", "Siddharth", "Zoya", "Aryan", "Mira", "Ishaan", "Anika"]
last = ["Patil", "Sharma", "Kulkarni", "Deshmukh", "Iyer", "Mehta", "Joshi", "Rao", "Nair", "Gupta"]
clubs = ["Pune Sharks", "Deccan Dolphins", "Baner Barracudas", "Kothrud Orcas"]
coaches = ["Coach Arjun", "Coach Neha", "Coach Ravi", "Coach Sana"]
cities = ["Pune", "Mumbai", "Nashik", "Satara"]

n_sw = 60
sw = pd.DataFrame({
    "swimmer_id": [f"S{i:03d}" for i in range(1, n_sw + 1)],
    "name": [f"{first[i % 30]} {last[(i * 7) % 10]}" for i in range(n_sw)],
    "gender": ["M" if (i % 30) % 2 == 0 else "F" for i in range(n_sw)],
    "birth_year": rng.integers(2008, 2016, n_sw),
    "city": rng.choice(cities, n_sw, p=[0.6, 0.2, 0.1, 0.1]),
    "club": rng.choice(clubs, n_sw),
    "coach": rng.choice(coaches, n_sw),
    "joined_date": pd.to_datetime("2019-01-01")
    + pd.to_timedelta(rng.integers(0, 365 * 5, n_sw), unit="D"),
})
sw["joined_date"] = sw["joined_date"].dt.strftime("%Y-%m-%d")
sw.loc[[5, 17, 42], "city"] = np.nan
sw.to_csv(DATA / "swimmers.csv", index=False)

# ---------------------------------------------------------------- swim results
events = {  # event: (stroke, distance, base seconds for a 12-year-old)
    "50 Free": ("Freestyle", 50, 34), "100 Free": ("Freestyle", 100, 75),
    "200 Free": ("Freestyle", 200, 165), "50 Back": ("Backstroke", 50, 40),
    "100 Back": ("Backstroke", 100, 86), "50 Breast": ("Breaststroke", 50, 45),
    "100 Breast": ("Breaststroke", 100, 96), "50 Fly": ("Butterfly", 50, 39),
    "200 IM": ("Individual Medley", 200, 185),
}
meets = [("District Winter Meet", "2024-01-20", 25), ("Pune Open", "2024-03-16", 50),
         ("Summer Splash", "2024-05-11", 25), ("State Qualifier", "2024-08-24", 50),
         ("Diwali Cup", "2024-10-26", 25), ("District Winter Meet", "2025-01-18", 25),
         ("Pune Open", "2025-03-15", 50), ("Summer Splash", "2025-05-10", 25)]
rows = []
skill = rng.normal(0, 0.06, n_sw)  # each swimmer's talent
for m_i, (meet, date, pool) in enumerate(meets):
    for s_i, s in sw.iterrows():
        n_ev = rng.integers(1, 4)
        for ev in rng.choice(list(events), n_ev, replace=False):
            stroke, dist, base = events[ev]
            age = int(date[:4]) - s.birth_year
            factor = (1 - 0.035 * (age - 12)) * (1 + skill[s_i]) * (1 - 0.01 * m_i)
            factor *= 1.03 if s.gender == "F" else 1.0
            factor *= 0.98 if pool == 50 else 1.0
            t = base * factor * rng.normal(1, 0.025)
            rows.append([meet, date, pool, s.swimmer_id, ev, stroke, dist, round(t, 2)])
res = pd.DataFrame(rows, columns=["meet", "date", "pool_length_m", "swimmer_id",
                                  "event", "stroke", "distance_m", "time_sec"])
res.insert(0, "result_id", range(1, len(res) + 1))
# disqualifications and messy bits, for cleaning practice
dq = rng.choice(res.index, 25, replace=False)
res["status"] = "OK"
res.loc[dq, "status"] = "DQ"
res.loc[dq, "time_sec"] = np.nan
res.loc[rng.choice(res.index, 12, replace=False), "stroke"] = " freestyle "
res.loc[rng.choice(res.index, 8, replace=False), "event"] = "50 free"
res = pd.concat([res, res.sample(6, random_state=1)]).reset_index(drop=True)  # duplicate rows
res.to_csv(DATA / "swim_results.csv", index=False)

# ---------------------------------------------------------------- customers + transactions
n_c = 800
cust = pd.DataFrame({
    "customer_id": [f"C{i:04d}" for i in range(1, n_c + 1)],
    "age": rng.integers(18, 76, n_c),
    "city": rng.choice(["Amsterdam", "Rotterdam", "Utrecht", "The Hague", "Eindhoven", "Groningen"],
                       n_c, p=[0.3, 0.2, 0.15, 0.15, 0.1, 0.1]),
    "account_open_date": (pd.to_datetime("2012-01-01")
                          + pd.to_timedelta(rng.integers(0, 365 * 12, n_c), unit="D")).strftime("%Y-%m-%d"),
    "credit_limit_eur": rng.choice([1000, 2500, 5000, 7500, 10000], n_c, p=[0.2, 0.35, 0.25, 0.12, 0.08]),
    "segment": rng.choice(["student", "standard", "premium"], n_c, p=[0.2, 0.65, 0.15]),
})
cust.loc[rng.choice(cust.index, 20, replace=False), "age"] = -1  # data-entry errors
cust.to_csv(DATA / "customers.csv", index=False)

n_t = 6000
cats = ["groceries", "restaurants", "transport", "online_shopping", "electronics",
        "travel", "entertainment", "fuel", "gift_cards"]
cat_p = [0.25, 0.15, 0.14, 0.15, 0.06, 0.05, 0.1, 0.07, 0.03]
cat_mu = dict(zip(cats, [3.3, 3.2, 2.6, 3.8, 5.2, 5.5, 3.3, 3.9, 4.0]))
t = pd.DataFrame({
    "transaction_id": [f"T{i:05d}" for i in range(1, n_t + 1)],
    "customer_id": rng.choice(cust["customer_id"], n_t),
    "timestamp": pd.to_datetime("2025-01-01")
    + pd.to_timedelta(rng.integers(0, 90 * 24 * 3600, n_t), unit="s"),
    "merchant_category": rng.choice(cats, n_t, p=cat_p),
    "channel": rng.choice(["in_store", "online", "contactless"], n_t, p=[0.4, 0.35, 0.25]),
    "country": rng.choice(["NL", "DE", "BE", "FR", "US", "NG", "RU"], n_t,
                          p=[0.82, 0.06, 0.04, 0.04, 0.02, 0.01, 0.01]),
})
t["amount_eur"] = np.round(np.exp(rng.normal(t["merchant_category"].map(cat_mu), 0.7)), 2)
hour = t["timestamp"].dt.hour
risk = (-5.2 + 1.6 * t["country"].isin(["NG", "RU", "US"]) + 0.9 * (t["channel"] == "online")
        + 1.4 * (t["merchant_category"].isin(["gift_cards", "electronics"]))
        + 1.1 * ((hour >= 0) & (hour < 5)) + 0.0025 * t["amount_eur"].clip(upper=1000))
t["is_fraud"] = (rng.random(n_t) < 1 / (1 + np.exp(-risk))).astype(int)
t = t.sort_values("timestamp").reset_index(drop=True)
t["timestamp"] = t["timestamp"].dt.strftime("%Y-%m-%d %H:%M:%S")
t.loc[rng.choice(t.index, 30, replace=False), "merchant_category"] = np.nan
t.to_csv(DATA / "transactions.csv", index=False)

# ---------------------------------------------------------------- student marks (regression practice)
n_s = 300
hours = np.round(rng.uniform(0, 25, n_s), 1)
attend = np.round(np.clip(rng.normal(80, 12, n_s), 35, 100), 0)
sleep = np.round(np.clip(rng.normal(7, 1.1, n_s), 4, 10), 1)
prev = np.round(np.clip(rng.normal(7.3, 1.0, n_s), 4, 10), 2)
part_time = rng.choice([0, 1], n_s, p=[0.75, 0.25])
final = (18 + 1.3 * hours + 0.25 * attend + 2.0 * sleep + 3.5 * prev - 4 * part_time
         + rng.normal(0, 5, n_s))
st = pd.DataFrame({
    "student_id": [f"P{i:03d}" for i in range(1, n_s + 1)],
    "study_hours_per_week": hours, "attendance_pct": attend, "sleep_hours": sleep,
    "previous_cgpa": prev, "part_time_job": part_time,
    "favourite_subject": rng.choice(["Python", "Statistics", "Databases", "Web", "Networks"], n_s),
    "final_marks": np.round(np.clip(final, 0, 100), 1),
})
st["passed"] = (st["final_marks"] >= 40).astype(int)
st.loc[rng.choice(st.index, 10, replace=False), "sleep_hours"] = np.nan
st.to_csv(DATA / "student_marks.csv", index=False)

for f in sorted(DATA.glob("*.csv")):
    d = pd.read_csv(f)
    print(f"{f.name:20s} {d.shape}")
print("fraud rate:", round(pd.read_csv(DATA / "transactions.csv")["is_fraud"].mean(), 4))
