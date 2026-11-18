# Python OOP: 18 exercises (hints and answers)

_Generated from `tools/source/oop.ktx`. Don't edit this file; it gets rebuilt._


## Level 1: Easy

#### 1. **Your first class.** Write a class `Swimmer` whose `__init__` takes `name`, `club` and `best_time`, and stores them on the object. Create two swimmers, then print each one's name and best time like `Diya (Dolphins): 31.47`. (★☆☆)
```python
diya = Swimmer("Diya", "Dolphins", 31.47)
kabir = Swimmer("Kabir", "Sharks", 28.90)
```

`hint:` `class Swimmer:` then `def __init__(self, name, club, best_time):` and inside it `self.name = name` (same for the others). Read them back with `diya.name`.

```python
class Swimmer:
    # __init__ runs automatically every time you write Swimmer(...)
    # self = "the object being built right now"
    def __init__(self, name, club, best_time):
        self.name = name              # store each value ON the object
        self.club = club
        self.best_time = best_time

diya = Swimmer("Diya", "Dolphins", 31.47)
kabir = Swimmer("Kabir", "Sharks", 28.90)

for s in [diya, kabir]:
    print(f"{s.name} ({s.club}): {s.best_time}")
# diya and kabir are two separate OBJECTS (instances) made from ONE class (the blueprint).
# Each has its own name, club and best_time.
```

#### 2. **Methods.** Write a class `Account` with `owner` and a `balance` that **starts at 0** (so you only pass the owner). Add a method `deposit(amount)` that adds to the balance, and a method `show()` that prints `Diya: 150.00 EUR`. Deposit 100, then 50, then call `show()`. (★☆☆)

`hint:` A method is a function written inside the class. Its first parameter is always `self`. Inside it, change `self.balance`, not a plain `balance`. `__init__(self, owner)` can set `self.balance = 0` itself.

```python
class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0          # every new account starts empty: no need to pass it in

    def deposit(self, amount):
        self.balance += amount    # self.balance = THIS account's balance

    def show(self):
        print(f"{self.owner}: {self.balance:.2f} EUR")

acc = Account("Diya")
acc.deposit(100)    # Python turns this into Account.deposit(acc, 100): that's where self comes from
acc.deposit(50)
acc.show()          # Diya: 150.00 EUR
```

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

```python
class Transaction:
    def __init__(self, tx_id, amount, channel):
        self.tx_id = tx_id
        self.amount = amount
        self.channel = channel

    # print(t) and str(t) call this. It must RETURN text.
    def __str__(self):
        return f"{self.tx_id}: {self.amount:.2f} EUR ({self.channel})"

t = Transaction("TX1", 45.2, "online")
print(t)    # TX1: 45.20 EUR (online)
# Without __str__ you get something like <__main__.Transaction object at 0x10a3f...>,
# which is just the class name and a memory address.
```

#### 4. **Class attribute vs instance attribute.** Add to `Transaction`: (★☆☆)
- a **class attribute** `currency = "EUR"` (the same for every transaction), and
- a **class attribute** `count = 0` that goes up by 1 every time a transaction is created.

Create 3 transactions, then print `Transaction.count` (should be `3`) and `t1.currency`.

`hint:` Class attributes are written directly under `class Transaction:`, not inside `__init__`. To change the shared counter inside `__init__`, write `Transaction.count += 1` (not `self.count += 1`).

```python
class Transaction:
    currency = "EUR"   # class attribute: ONE value, shared by all transactions
    count = 0          # class attribute: a shared counter

    def __init__(self, tx_id, amount):
        self.tx_id = tx_id      # instance attributes: different for every transaction
        self.amount = amount
        Transaction.count += 1  # change the SHARED value on the class

t1 = Transaction("TX1", 45.2)
t2 = Transaction("TX2", 899.0)
t3 = Transaction("TX3", 12.5)
print(Transaction.count)   # 3
print(t1.currency)         # EUR: t1 has no own "currency", so Python looks it up on the class
# Why not self.count += 1? That would READ the class value (0), add 1, and then create a NEW
# instance attribute on that one object. The class counter would stay 0.
```

#### 5. **A list of objects.** Using the `Transaction` class from exercise 3 (copy it in), make the transactions below into a **list of objects**. Then, with one loop, print the total amount and the **largest** transaction (use `print(...)` on the object, so your `__str__` is used). (★☆☆)
```python
data = [("TX1", 45.2, "online"), ("TX2", 899.0, "online"),
        ("TX3", 12.5, "contactless"), ("TX4", 120.0, "in_store")]
```

`hint:` `txs = [Transaction(i, a, c) for i, a, c in data]`. Then the accumulator and best-so-far patterns from the logic lesson, but read `t.amount` instead of a number.

```python
class Transaction:
    def __init__(self, tx_id, amount, channel):
        self.tx_id = tx_id
        self.amount = amount
        self.channel = channel

    def __str__(self):
        return f"{self.tx_id}: {self.amount:.2f} EUR ({self.channel})"

data = [("TX1", 45.2, "online"), ("TX2", 899.0, "online"),
        ("TX3", 12.5, "contactless"), ("TX4", 120.0, "in_store")]
txs = [Transaction(i, a, c) for i, a, c in data]   # 4 objects in a list

total = 0
biggest = txs[0]                 # best-so-far: start with the first OBJECT
for t in txs:
    total += t.amount
    if t.amount > biggest.amount:
        biggest = t
print(f"Total: {total:.2f}")      # Total: 1076.70
print("Largest:", biggest)        # Largest: TX2: 899.00 EUR (online)
# Same patterns as before. The only change: each item is an object, so you reach inside with a dot.
```

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

```python
class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

a = Account("Diya")
b = a              # NOT a copy: a and b are two names (labels) for ONE object
b.deposit(50)
c = Account("Diya")  # a brand-new, separate object that just happens to have the same owner
print(a.balance)   # 50     -> the deposit went into the one shared object
print(a is b)      # True   -> same object
print(a is c)      # False  -> same data, different object
# This is why changing an object inside a function also changes it outside:
# the function receives the same object, not a copy. Lists and dicts behave the same way.
```


## Level 2: Medium

#### 7. **Encapsulation: protect the data.** Copy `Account` from exercise 2 and change it so the object **refuses bad changes**: (★★☆)
- `deposit(amount)` raises `ValueError("amount must be positive")` if `amount <= 0`.
- a new `withdraw(amount)` raises `ValueError("amount must be positive")` if `amount <= 0` and `ValueError("insufficient funds")` if `amount` is more than the balance. Otherwise it subtracts.

Test it: deposit 100, withdraw 30, then try to withdraw 500 and deposit -5 inside `try/except ValueError as e`, printing `Refused: ...`. Finally `show()` (should be `70.00`).

`hint:` `raise ValueError("insufficient funds")` stops the method right there, so the balance never changes. Check the bad cases **first**, at the top of the method, and only then change `self.balance`.

```python
class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")   # stop: the balance is not touched
        self.balance += amount

    def withdraw(self, amount):
        # check every bad case FIRST ...
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > self.balance:
            raise ValueError("insufficient funds")
        # ... and only change the data once we know it's safe
        self.balance -= amount

    def show(self):
        print(f"{self.owner}: {self.balance:.2f} EUR")

acc = Account("Diya")
acc.deposit(100)
acc.withdraw(30)
try:
    acc.withdraw(500)
except ValueError as e:
    print("Refused:", e)      # Refused: insufficient funds
try:
    acc.deposit(-5)
except ValueError as e:
    print("Refused:", e)      # Refused: amount must be positive
acc.show()                    # Diya: 70.00 EUR
# This is encapsulation: the RULES about the balance live inside the class,
# so no code anywhere can put the account into an impossible state through these methods.
```

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

```python
class Account:
    def __init__(self, owner):
        self.owner = owner
        self._balance = 0        # leading underscore = "internal". Python doesn't block it,
                                 # but every Python programmer reads it as "hands off"

    @property
    def balance(self):           # acc.balance (no brackets!) calls this method
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount  # inside the class we change the internal value

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount

acc = Account("Diya")
acc.deposit(100)
print(acc.balance)               # 100: reads like a normal attribute
try:
    acc.balance = 1_000_000      # no setter -> Python refuses
except AttributeError as e:
    print("Blocked:", e)
print(acc.balance)               # still 100
# The only way to change the balance is now through deposit/withdraw, which check the rules.
```

#### 9. **A property with a setter (validation).** Write a class `Swimmer` with `name` and `best_time`. Make `best_time` a property with a **setter** that raises `ValueError` if the new time is not a positive number (it must be an `int` or `float` and greater than 0). The check must also run when the object is first **created**. (★★☆)
Test: create `Swimmer("Diya", 31.47)`, set `best_time = 30.9` (works), then try `-3` and `"fast"` and print the refusals.

`hint:` Store the real value in `self._best_time`. Use `@property` for the getter and `@best_time.setter` for the setter. In `__init__`, write `self.best_time = best_time` (no underscore) so the setter runs there too. `isinstance(x, (int, float))` checks the type.

```python
class Swimmer:
    def __init__(self, name, best_time):
        self.name = name
        self.best_time = best_time       # NO underscore: this goes through the setter below,
                                         # so even a brand-new swimmer gets checked

    @property
    def best_time(self):                 # getter: runs on  s.best_time
        return self._best_time

    @best_time.setter
    def best_time(self, value):          # setter: runs on  s.best_time = value
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"best_time must be a positive number, got {value!r}")
        self._best_time = value          # the real data lives in _best_time

s = Swimmer("Diya", 31.47)
s.best_time = 30.9
print(s.name, s.best_time)               # Diya 30.9
for bad in [-3, "fast"]:
    try:
        s.best_time = bad
    except ValueError as e:
        print("Refused:", e)
try:
    Swimmer("Kabir", 0)                  # the check also protects creation
except ValueError as e:
    print("Refused:", e)
print(s.best_time)                       # still 30.9
```

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

```python
class Transaction:
    def __init__(self, tx_id, amount, channel):
        self.tx_id = tx_id
        self.amount = amount
        self.channel = channel

    def __str__(self):
        return f"{self.tx_id}: {self.amount:.2f} EUR ({self.channel})"

class OnlineTransaction(Transaction):          # "an OnlineTransaction IS A Transaction"
    def __init__(self, tx_id, amount, ip_country):
        # let the parent set up the shared parts (we don't copy-paste its code)
        super().__init__(tx_id, amount, "online")
        self.ip_country = ip_country           # the extra part only the child has

    def __str__(self):                          # override: replace the parent's version
        return f"{self.tx_id}: {self.amount:.2f} EUR ({self.channel}, IP: {self.ip_country})"

t1 = Transaction("TX1", 45.2, "in_store")
t2 = OnlineTransaction("TX2", 899.0, "NG")
print(t1)                                       # TX1: 45.20 EUR (in_store)
print(t2)                                       # TX2: 899.00 EUR (online, IP: NG)
print(isinstance(t2, Transaction))              # True:  every online tx is a transaction
print(isinstance(t1, OnlineTransaction))        # False: not every transaction is online
print(issubclass(OnlineTransaction, Transaction))  # True
```

#### 11. **Override and extend with `super()`.** Give the base `Transaction` a method `risk_score()`: 1 point if `amount > 500`, else 0. In `OnlineTransaction`, override `risk_score()` so it **starts from the parent's score** (call `super().risk_score()`) and adds 2 points if `ip_country` is not `"NL"`. (★★☆)
Print the risk score of each:
```python
txs = [Transaction("TX1", 45.2, "in_store"), Transaction("TX2", 1200.0, "in_store"),
       OnlineTransaction("TX3", 30.0, "NL"), OnlineTransaction("TX4", 899.0, "NG")]
```
Expected scores: 0, 1, 0, 3.

`hint:` In the child: `score = super().risk_score()` then `if self.ip_country != "NL": score += 2`, then `return score`. Don't copy the "amount > 500" rule into the child.

```python
class Transaction:
    def __init__(self, tx_id, amount, channel):
        self.tx_id = tx_id
        self.amount = amount
        self.channel = channel

    def risk_score(self):
        return 1 if self.amount > 500 else 0

class OnlineTransaction(Transaction):
    def __init__(self, tx_id, amount, ip_country):
        super().__init__(tx_id, amount, "online")
        self.ip_country = ip_country

    def risk_score(self):
        score = super().risk_score()      # reuse the parent's rule ...
        if self.ip_country != "NL":
            score += 2                    # ... and add the online-only rule on top
        return score

txs = [Transaction("TX1", 45.2, "in_store"), Transaction("TX2", 1200.0, "in_store"),
       OnlineTransaction("TX3", 30.0, "NL"), OnlineTransaction("TX4", 899.0, "NG")]
for t in txs:
    print(t.tx_id, t.risk_score())        # 0, 1, 0, 3
# If the bank later changes the amount rule to "> 400", you change ONE line in the parent,
# and every child gets it automatically. That's the point of super().
```

#### 12. **Polymorphism.** Copy your classes from exercise 11 and add a third: `ContactlessTransaction(Transaction)`, whose `risk_score()` is the parent's score **plus 1 if `amount > 50`** (contactless payments above 50 EUR are unusual). Put one of each type in a list and print every risk score in **one loop with no `if` about the type**. (★★☆)
Then add a class `GiftCardPurchase` that does **not** inherit from anything but has its own `tx_id` and a `risk_score()` that always returns 2. Add it to the list. Does the loop still work? Explain why in a comment.

`hint:` The loop just calls `t.risk_score()`. Each object runs **its own** version. Python only cares that the object *has* a `risk_score` method, not what its parent class is ("duck typing").

```python
class Transaction:
    def __init__(self, tx_id, amount, channel):
        self.tx_id = tx_id
        self.amount = amount
        self.channel = channel

    def risk_score(self):
        return 1 if self.amount > 500 else 0

class OnlineTransaction(Transaction):
    def __init__(self, tx_id, amount, ip_country):
        super().__init__(tx_id, amount, "online")
        self.ip_country = ip_country

    def risk_score(self):
        score = super().risk_score()
        if self.ip_country != "NL":
            score += 2
        return score

class ContactlessTransaction(Transaction):
    def __init__(self, tx_id, amount):
        super().__init__(tx_id, amount, "contactless")

    def risk_score(self):
        return super().risk_score() + (1 if self.amount > 50 else 0)

class GiftCardPurchase:                 # NOT a Transaction child at all
    def __init__(self, tx_id):
        self.tx_id = tx_id

    def risk_score(self):
        return 2

txs = [Transaction("TX1", 700.0, "in_store"),
       OnlineTransaction("TX2", 899.0, "NG"),
       ContactlessTransaction("TX3", 60.0),
       GiftCardPurchase("TX4")]
for t in txs:
    print(t.tx_id, type(t).__name__, t.risk_score())   # one line, no type checks
# TX1 Transaction 1 | TX2 OnlineTransaction 3 | TX3 ContactlessTransaction 1 | TX4 GiftCardPurchase 2
# Polymorphism = "same method call, different behaviour depending on the object".
# GiftCardPurchase works too: Python doesn't check the family tree, only whether the object
# HAS a risk_score() method. This is called duck typing ("if it quacks like a duck...").
# scikit-learn uses exactly this: every model has .fit() and .predict(), so you can swap models freely.
```

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

```python
class SwimResult:
    def __init__(self, swimmer, time_sec):
        self.swimmer = swimmer
        self.time_sec = time_sec

    def __repr__(self):                   # used when the object is shown inside a list
        return f"SwimResult({self.swimmer!r}, {self.time_sec})"

    def __eq__(self, other):              # runs on  a == b
        return self.time_sec == other.time_sec

    def __lt__(self, other):              # runs on  a < b ; sorted() and min() use it
        return self.time_sec < other.time_sec

results = [SwimResult("Diya", 31.47), SwimResult("Kabir", 28.90),
           SwimResult("Rohan", 29.60), SwimResult("Meera", 31.47)]
print(sorted(results))           # fastest first, no key= needed
print(min(results))              # SwimResult('Kabir', 28.9)
print(results[0] == results[3])  # True: same time (a dead heat)
print(results[0] is results[3])  # False: still two different objects
# "Dunder" = double underscore. These methods let your objects work with Python's own
# operators and functions: ==, <, len(), print(), sorted() ...
# pandas does this too: df["a"] + df["b"] works because Series defines __add__.
```


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

```python
from abc import ABC, abstractmethod

class FraudRule(ABC):
    """The CONTRACT: every rule must be able to check(tx)."""

    @abstractmethod
    def check(self, tx):
        ...                             # no body: each child must write its own

    def describe(self):                 # a normal method all children get for free
        return type(self).__name__

class AmountRule(FraudRule):
    def __init__(self, limit):
        self.limit = limit

    def check(self, tx):
        return tx["amount"] > self.limit

class CountryRule(FraudRule):
    def __init__(self, blocked):
        self.blocked = blocked

    def check(self, tx):
        return tx["country"] in self.blocked

try:
    FraudRule()                         # an abstract class is only a template
except TypeError as e:
    print("Can't create it:", e)

transactions = [{"id": "T1", "amount": 40.0, "country": "NL"},
                {"id": "T2", "amount": 2500.0, "country": "NG"},
                {"id": "T3", "amount": 15.0, "country": "RU"}]
rules = [AmountRule(1000), CountryRule({"NG", "RU"})]

for tx in transactions:
    fired = [r.describe() for r in rules if r.check(tx)]   # polymorphism: each rule checks its own way
    if fired:
        print(f"{tx['id']} flagged by: {', '.join(fired)}")
    else:
        print(f"{tx['id']} OK")
# Abstraction = the code that USES rules only knows "a rule has check()". It doesn't know or care
# how each rule works inside. Adding a NightRule tomorrow needs zero changes to this loop.
```

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

```python
class Transaction:
    def __init__(self, amount, country):
        self.amount = amount
        self.country = country

class Customer:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.transactions = []          # a Customer HAS transactions (composition)

    def add(self, tx):
        self.transactions.append(tx)

    def total_spent(self):
        return sum(t.amount for t in self.transactions)

    def foreign_total(self):
        return sum(t.amount for t in self.transactions if t.country != "NL")

    def is_flagged(self):
        return self.foreign_total() > 500 or any(t.amount > 1000 for t in self.transactions)

rows = [("C1", "NL", 40.0), ("C2", "US", 300.0), ("C1", "DE", 120.0),
        ("C3", "NL", 1500.0), ("C2", "NG", 250.0), ("C4", "NL", 999.0),
        ("C1", "NL", 800.0), ("C4", "FR", 20.0)]

customers = {}                           # customer_id -> Customer object
for cid, country, amount in rows:
    if cid not in customers:
        customers[cid] = Customer(cid)
    customers[cid].add(Transaction(amount, country))

for c in customers.values():
    print(c.customer_id, f"total {c.total_spent():.0f}, foreign {c.foreign_total():.0f}")
print(sorted(c.customer_id for c in customers.values() if c.is_flagged()))   # ['C2', 'C3']
# Is-a  -> inheritance  (OnlineTransaction IS A Transaction)
# Has-a -> composition  (Customer HAS transactions)
# Compare with logic #8: the rules now live INSIDE Customer, with a clear name (is_flagged),
# instead of being spread across loose dicts and sets.
```

#### 16. **`@classmethod` and `@staticmethod`.** Write a `Transaction` class with `tx_id`, `amount`, `country` and `hour` (an `int`). Add: (★★★)
- a `@staticmethod` `is_night(hour)` that returns `True` for hours 0–5 (it doesn't need any object),
- a `@classmethod` `from_row(cls, row)` that builds a `Transaction` from **one row of `transactions.csv`** (a dict from `csv.DictReader`). It must turn the text into the right types (the hour is in the `timestamp` text `"2025-01-03 02:15:00"`),
- a normal method `is_suspicious()`: night **and** amount over 300.

Read `../data/transactions.csv`, build all transactions with `Transaction.from_row(row)`, and print how many there are and how many are suspicious. Also print `Transaction.is_night(3)`.

`hint:` `timestamp[11:13]` is the hour text, `int(...)` makes it a number. `from_row` ends with `return cls(row["transaction_id"], float(row["amount_eur"]), row["country"], hour)`. `cls` is the class itself, so `cls(...)` is the same as `Transaction(...)`.

```python
import csv

class Transaction:
    def __init__(self, tx_id, amount, country, hour):
        self.tx_id = tx_id
        self.amount = amount
        self.country = country
        self.hour = hour

    @staticmethod
    def is_night(hour):                 # no self, no cls: just a helper that belongs with the class
        return 0 <= hour <= 5

    @classmethod
    def from_row(cls, row):             # an ALTERNATIVE way to build a Transaction
        hour = int(row["timestamp"][11:13])   # "2025-01-03 02:15:00"[11:13] -> "02" -> 2
        return cls(row["transaction_id"], float(row["amount_eur"]), row["country"], hour)

    def is_suspicious(self):            # normal method: needs THIS object's data
        return Transaction.is_night(self.hour) and self.amount > 300

with open("../data/transactions.csv", newline="") as f:
    txs = [Transaction.from_row(row) for row in csv.DictReader(f)]

print("transactions:", len(txs))
print("suspicious:", sum(t.is_suspicious() for t in txs))   # True counts as 1
print(Transaction.is_night(3))                               # True
# normal method -> works on one object (self)
# classmethod   -> works on the class (cls): usually "another way to create an object".
#                  pandas has these: pd.DataFrame.from_dict(...)
# staticmethod  -> a plain function stored in the class because it belongs there
```

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

```python
# Bug 1 (the crash): RelaySquad.__init__ never calls super().__init__(coach),
#        so self.coach is never set -> AttributeError: 'RelaySquad' object has no attribute 'coach'.
# Bug 2 (silent, the dangerous one): members = [] is a CLASS attribute, so there is ONE list
#        shared by EVERY squad. a.add("Diya") and b.add("Kabir") both append to that same list,
#        so a.members shows ['Diya', 'Kabir'].
#        Fix: create the list inside __init__ so each object gets its own.
class Squad:
    def __init__(self, coach):
        self.coach = coach
        self.members = []                 # fix 2: one NEW list per squad

    def add(self, name):
        self.members.append(name)

class RelaySquad(Squad):
    def __init__(self, coach, stroke):
        super().__init__(coach)           # fix 1: let the parent set coach and members
        self.stroke = stroke

    def describe(self):
        return f"{self.stroke} relay, coach {self.coach}: {self.members}"

a = Squad("Mr. Rao")
b = Squad("Ms. Iyer")
a.add("Diya")
b.add("Kabir")
print(a.members)        # ['Diya']   (with the bug: ['Diya', 'Kabir'])
r = RelaySquad("Mr. Rao", "Medley")
print(r.describe())     # Medley relay, coach Mr. Rao: []
# Rule: anything that changes per object (lists, dicts, counts per object) goes in __init__.
# Class attributes are only for values that really are shared, like currency = "EUR".
```

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

```python
from sklearn.dummy import DummyClassifier

class ThresholdClassifier:
    def __init__(self):
        self.threshold_ = None            # nothing learned yet

    def fit(self, X, y):
        best_t, best_correct = None, -1
        for row in X:                     # every amount is a candidate threshold
            t = row[0]
            correct = sum((r[0] >= t) == bool(label) for r, label in zip(X, y))
            if correct > best_correct:    # best-so-far pattern
                best_t, best_correct = t, correct
        self.threshold_ = best_t          # learned value -> trailing underscore
        return self                       # so you can chain: model.fit(X, y).predict(X_test)

    def predict(self, X):
        if self.threshold_ is None:       # encapsulation: refuse to give nonsense
            raise RuntimeError("call fit() first")
        return [1 if r[0] >= self.threshold_ else 0 for r in X]

X = [[12.0], [45.0], [80.0], [150.0], [300.0], [650.0], [900.0], [1500.0], [2200.0], [95.0]]
y = [0, 0, 0, 0, 0, 1, 0, 1, 1, 0]
X_test = [[30.0], [700.0], [5000.0]]

try:
    ThresholdClassifier().predict(X_test)
except RuntimeError as e:
    print("Refused:", e)

model = ThresholdClassifier().fit(X, y)
print("learned threshold:", model.threshold_)   # 650.0 (9 out of 10 right; only the 900 is wrong)
print("predictions:", model.predict(X_test))    # [0, 1, 1]

# Polymorphism / duck typing: your class and a real scikit-learn model in ONE loop
for m in [ThresholdClassifier(), DummyClassifier(strategy="most_frequent")]:
    preds = m.fit(X, y).predict(X_test)
    print(type(m).__name__, [int(p) for p in preds])   # int(): sklearn returns numpy numbers
# DummyClassifier always predicts the most common label (0), so it gets [0, 0, 0].
# Every scikit-learn model is a class with this same shape: settings in __init__,
# learning in fit() (stored as name_), using it in predict(). Now you know why.
```
