# Python OOP: 18 exercises (hints)

_Generated from `tools/source/oop.ktx`. Don't edit this file; it gets rebuilt._


## Level 1: Easy

#### 1. **Your first class.** Write a class `Swimmer` whose `__init__` takes `name`, `club` and `best_time`, and stores them on the object. Create two swimmers, then print each one's name and best time like `Diya (Dolphins): 31.47`. (★☆☆)
```python
diya = Swimmer("Diya", "Dolphins", 31.47)
kabir = Swimmer("Kabir", "Sharks", 28.90)
```

`hint:` `class Swimmer:` then `def __init__(self, name, club, best_time):` and inside it `self.name = name` (same for the others). Read them back with `diya.name`.

#### 2. **Methods.** Write a class `Account` with `owner` and a `balance` that **starts at 0** (so you only pass the owner). Add a method `deposit(amount)` that adds to the balance, and a method `show()` that prints `Diya: 150.00 EUR`. Deposit 100, then 50, then call `show()`. (★☆☆)

`hint:` A method is a function written inside the class. Its first parameter is always `self`. Inside it, change `self.balance`, not a plain `balance`. `__init__(self, owner)` can set `self.balance = 0` itself.

#### 3. **`__str__`.** Here is a `Transaction` class. First run `print(t)` and look at the ugly output. Then add a `__str__` method so `print(t)` shows `TX1: 45.20 EUR (online)`. (★☆☆)
```python
class Transaction:
    def __init__(self, tx_id, amount, channel):
        self.tx_id = tx_id
        self.amount = amount
        self.channel = channel

t = Transaction("TX1", 45.2, "online")
print(t)
```

`hint:` `def __str__(self):` must **return** a string (not print it). `print()` calls `__str__` for you.

#### 4. **Class attribute vs instance attribute.** Add to `Transaction`: (★☆☆)
- a **class attribute** `currency = "EUR"` (the same for every transaction), and
- a **class attribute** `count = 0` that goes up by 1 every time a transaction is created.

Create 3 transactions, then print `Transaction.count` (should be `3`) and `t1.currency`.

`hint:` Class attributes are written directly under `class Transaction:`, not inside `__init__`. To change the shared counter inside `__init__`, write `Transaction.count += 1` (not `self.count += 1`).

#### 5. **A list of objects.** Using the `Transaction` class from exercise 3 (copy it in), make the transactions below into a **list of objects**. Then, with one loop, print the total amount and the **largest** transaction (use `print(...)` on the object, so your `__str__` is used). (★☆☆)
```python
data = [("TX1", 45.2, "online"), ("TX2", 899.0, "online"),
        ("TX3", 12.5, "contactless"), ("TX4", 120.0, "in_store")]
```

`hint:` `txs = [Transaction(i, a, c) for i, a, c in data]`. Then the accumulator and best-so-far patterns from the logic lesson, but read `t.amount` instead of a number.

#### 6. **Predict, then run.** Write down what you think each `print` shows, **then** run it. Explain in a `#` comment why `a.balance` changed even though we only touched `b`. (★☆☆)
```python
class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

a = Account("Diya")
b = a
b.deposit(50)
c = Account("Diya")
print(a.balance)
print(a is b)
print(a is c)
```

`hint:` `b = a` does **not** copy the account. It puts a second name on the **same** object. `is` checks "is this the very same object?". `c` was made with a new `Account(...)` call.


## Level 2: Medium

#### 7. **Encapsulation: protect the data.** Copy `Account` from exercise 2 and change it so the object **refuses bad changes**: (★★☆)
- `deposit(amount)` raises `ValueError("amount must be positive")` if `amount <= 0`.
- a new `withdraw(amount)` raises `ValueError("amount must be positive")` if `amount <= 0` and `ValueError("insufficient funds")` if `amount` is more than the balance. Otherwise it subtracts.

Test it: deposit 100, withdraw 30, then try to withdraw 500 and deposit -5 inside `try/except ValueError as e`, printing `Refused: ...`. Finally `show()` (should be `70.00`).

`hint:` `raise ValueError("insufficient funds")` stops the method right there, so the balance never changes. Check the bad cases **first**, at the top of the method, and only then change `self.balance`.

#### 8. **`_private` and a read-only `@property`.** The account from exercise 7 has a weakness: anyone can still write `acc.balance = 1_000_000` and skip all your checks. Fix it: (★★☆)
- store the balance as `self._balance` (the underscore means "internal, don't touch from outside"),
- add a `@property` called `balance` that **returns** `self._balance`, with **no setter**.

Show that `acc.balance` still reads fine, and that `acc.balance = 1_000_000` now raises an `AttributeError` (catch it and print `Blocked: ...`).

`hint:` ```python
@property
def balance(self):
    return self._balance
```
Inside the class, `deposit` and `withdraw` must now change `self._balance`. A property with no setter can be read but not assigned.

#### 9. **A property with a setter (validation).** Write a class `Swimmer` with `name` and `best_time`. Make `best_time` a property with a **setter** that raises `ValueError` if the new time is not a positive number (it must be an `int` or `float` and greater than 0). The check must also run when the object is first **created**. (★★☆)
Test: create `Swimmer("Diya", 31.47)`, set `best_time = 30.9` (works), then try `-3` and `"fast"` and print the refusals.

`hint:` Store the real value in `self._best_time`. Use `@property` for the getter and `@best_time.setter` for the setter. In `__init__`, write `self.best_time = best_time` (no underscore) so the setter runs there too. `isinstance(x, (int, float))` checks the type.

#### 10. **Inheritance.** Start from this base class. Write a **child class** `OnlineTransaction(Transaction)` that also has an `ip_country`. Its `__init__` must call `super().__init__(...)` for the shared parts, then store `ip_country`. **Override** `__str__` so it shows `TX2: 899.00 EUR (online, IP: NG)`. (★★☆)
Then print both objects, and print `isinstance(t2, Transaction)`, `isinstance(t1, OnlineTransaction)` and `issubclass(OnlineTransaction, Transaction)`.
```python
class Transaction:
    def __init__(self, tx_id, amount, channel):
        self.tx_id = tx_id
        self.amount = amount
        self.channel = channel

    def __str__(self):
        return f"{self.tx_id}: {self.amount:.2f} EUR ({self.channel})"

t1 = Transaction("TX1", 45.2, "in_store")
t2 = OnlineTransaction("TX2", 899.0, "NG")
```

`hint:` `class OnlineTransaction(Transaction):` then in its `__init__(self, tx_id, amount, ip_country)`: `super().__init__(tx_id, amount, "online")` and then `self.ip_country = ip_country`.

#### 11. **Override and extend with `super()`.** Give the base `Transaction` a method `risk_score()`: 1 point if `amount > 500`, else 0. In `OnlineTransaction`, override `risk_score()` so it **starts from the parent's score** (call `super().risk_score()`) and adds 2 points if `ip_country` is not `"NL"`. (★★☆)
Print the risk score of each:
```python
txs = [Transaction("TX1", 45.2, "in_store"), Transaction("TX2", 1200.0, "in_store"),
       OnlineTransaction("TX3", 30.0, "NL"), OnlineTransaction("TX4", 899.0, "NG")]
```
Expected scores: 0, 1, 0, 3.

`hint:` In the child: `score = super().risk_score()` then `if self.ip_country != "NL": score += 2`, then `return score`. Don't copy the "amount > 500" rule into the child.

#### 12. **Polymorphism.** Copy your classes from exercise 11 and add a third: `ContactlessTransaction(Transaction)`, whose `risk_score()` is the parent's score **plus 1 if `amount > 50`** (contactless payments above 50 EUR are unusual). Put one of each type in a list and print every risk score in **one loop with no `if` about the type**. (★★☆)
Then add a class `GiftCardPurchase` that does **not** inherit from anything but has its own `tx_id` and a `risk_score()` that always returns 2. Add it to the list. Does the loop still work? Explain why in a comment.

`hint:` The loop just calls `t.risk_score()`. Each object runs **its own** version. Python only cares that the object *has* a `risk_score` method, not what its parent class is ("duck typing").

#### 13. **Dunder methods: compare and sort your own objects.** Write a class `SwimResult` with `swimmer` and `time_sec`. Add: (★★☆)
- `__repr__` returning `SwimResult('Kabir', 28.9)` (this is what you see inside a printed list),
- `__eq__`: two results are equal if their **times** are equal,
- `__lt__`: one result is "less than" another if its time is **smaller** (faster).

Then `sorted(results)` must work with **no** `key=`, `min(results)` must give the fastest, and `results[0] == results[3]` must be `True`.
```python
results = [SwimResult("Diya", 31.47), SwimResult("Kabir", 28.90),
           SwimResult("Rohan", 29.60), SwimResult("Meera", 31.47)]
```

`hint:` `def __lt__(self, other): return self.time_sec < other.time_sec`. `sorted()` and `min()` use `<` behind the scenes, so `__lt__` is all they need. `__repr__` is like `__str__` but for developers (lists use it).


## Level 3: Hard

#### 14. **Abstraction with `ABC`.** Build a tiny fraud-rule system: (★★★)
- an **abstract** base class `FraudRule(ABC)` with an abstract method `check(tx)` (returns `True` if the transaction looks suspicious) and a normal method `describe()` that returns the class name,
- `AmountRule(limit)`: suspicious if `tx["amount"] > limit`,
- `CountryRule(blocked)`: suspicious if `tx["country"]` is in the `blocked` set.

First show that `FraudRule()` **cannot** be created (catch the `TypeError`). Then run every rule on every transaction and print which rules fired, like `T2 flagged by: AmountRule, CountryRule`.
```python
transactions = [{"id": "T1", "amount": 40.0, "country": "NL"},
                {"id": "T2", "amount": 2500.0, "country": "NG"},
                {"id": "T3", "amount": 15.0, "country": "RU"}]
rules = [AmountRule(1000), CountryRule({"NG", "RU"})]
```

`hint:` `from abc import ABC, abstractmethod`. Put `@abstractmethod` above `def check(self, tx):` and give it no real body (`...` or `pass`). Children **must** write their own `check`, or they can't be created either. `type(self).__name__` gives the class name.

#### 15. **Composition ("has-a").** A customer is **not** a kind of transaction, but a customer **has** transactions. Write: (★★★)
- `Transaction(amount, country)` (just stores the two values),
- `Customer(customer_id)` that starts with an **empty list** `self.transactions`, plus methods `add(tx)`, `total_spent()` and `foreign_total()` (everything with `country != "NL"`), and `is_flagged()`: `True` if the foreign total is more than 500 **or** any single transaction is over 1000.

Load the data below into customers (one `Customer` object per ID, kept in a dict), then print the flagged IDs in order. Answer: `['C2', 'C3']` (it's logic exercise 8 again, now with objects).
```python
rows = [("C1", "NL", 40.0), ("C2", "US", 300.0), ("C1", "DE", 120.0),
        ("C3", "NL", 1500.0), ("C2", "NG", 250.0), ("C4", "NL", 999.0),
        ("C1", "NL", 800.0), ("C4", "FR", 20.0)]
```

`hint:` Keep `customers = {}`. For each row: if the ID isn't in the dict yet, put a new `Customer(cid)` there, then `customers[cid].add(Transaction(amount, country))`. `any(t.amount > 1000 for t in self.transactions)` checks "any single one".

#### 16. **`@classmethod` and `@staticmethod`.** Write a `Transaction` class with `tx_id`, `amount`, `country` and `hour` (an `int`). Add: (★★★)
- a `@staticmethod` `is_night(hour)` that returns `True` for hours 0–5 (it doesn't need any object),
- a `@classmethod` `from_row(cls, row)` that builds a `Transaction` from **one row of `transactions.csv`** (a dict from `csv.DictReader`). It must turn the text into the right types (the hour is in the `timestamp` text `"2025-01-03 02:15:00"`),
- a normal method `is_suspicious()`: night **and** amount over 300.

Read `../data/transactions.csv`, build all transactions with `Transaction.from_row(row)`, and print how many there are and how many are suspicious. Also print `Transaction.is_night(3)`.

`hint:` `timestamp[11:13]` is the hour text, `int(...)` makes it a number. `from_row` ends with `return cls(row["transaction_id"], float(row["amount_eur"]), row["country"], hour)`. `cls` is the class itself, so `cls(...)` is the same as `Transaction(...)`.

#### 17. **Spot the bugs.** This code has **two** bugs. Run it, read the error, fix it, run again, and then look closely at the output: something is still wrong. Explain both bugs in comments and fix them. (★★★)
```python
class Squad:
    members = []

    def __init__(self, coach):
        self.coach = coach

    def add(self, name):
        self.members.append(name)

class RelaySquad(Squad):
    def __init__(self, coach, stroke):
        self.stroke = stroke

    def describe(self):
        return f"{self.stroke} relay, coach {self.coach}: {self.members}"

a = Squad("Mr. Rao")
b = Squad("Ms. Iyer")
a.add("Diya")
b.add("Kabir")
print(a.members)
r = RelaySquad("Mr. Rao", "Medley")
print(r.describe())
```

`hint:` Bug 1: what does `RelaySquad.__init__` forget to do, so `self.coach` never exists? Bug 2: `members = []` is written under `class Squad:`, not inside `__init__`. How many lists exist in total, for all squads?

#### 18. **Mini task: build your own scikit-learn-style model.** Write a class `ThresholdClassifier` that works like a scikit-learn model: (★★★)
- `fit(X, y)`: `X` is a list of rows like `[[45.0], [1200.0], ...]` (one feature: the amount), `y` is a list of 0/1 labels. Try **every amount in X** as a threshold ("predict 1 if amount >= threshold"), and keep the one that gets the most rows right. Store it as `self.threshold_` (scikit-learn puts a `_` at the end of anything learned during `fit`). `fit` must `return self`.
- `predict(X)`: returns a list of 0/1 predictions.
- If `predict` is called **before** `fit`, raise `RuntimeError("call fit() first")`.

Fit it on the training data, print the learned threshold and the predictions for `X_test`. Then loop over `[ThresholdClassifier(), DummyClassifier(strategy="most_frequent")]` (from `sklearn.dummy`) and call `.fit(X, y).predict(X_test)` on **both** in the same loop.
```python
X = [[12.0], [45.0], [80.0], [150.0], [300.0], [650.0], [900.0], [1500.0], [2200.0], [95.0]]
y = [0, 0, 0, 0, 0, 1, 0, 1, 1, 0]
X_test = [[30.0], [700.0], [5000.0]]
```

`hint:` In `__init__`, set `self.threshold_ = None`. In `fit`: loop `for row in X: t = row[0]`, count `correct = sum((r[0] >= t) == bool(label) for r, label in zip(X, y))`, and keep the best `t` (best-so-far). In `predict`: `[1 if r[0] >= self.threshold_ else 0 for r in X]`.
