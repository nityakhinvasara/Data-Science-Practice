# Python OOP guide: classes, objects and the 4 pillars

## How to use this guide
- This is a **longer day** (about 2 hours): ~25 min reading, ~90 min for the 18 exercises. Read one Part, then do its exercises, then read the next Part. Don't read everything first.
- Run every example in a scratch cell. Change a value and see what happens.
- Keep the logic habit: write your steps as `#` comments before you code.
- If you run out of time, finish 14–18 on Friday (review day).

**Why OOP matters for data science:** every scikit-learn model is a class (`LogisticRegression()` makes an object, `.fit()` and `.predict()` are methods). A pandas DataFrame is an object too. Interviews for junior roles often ask *"explain the 4 pillars of OOP"*. After today you can answer that and show code.

---

## Part 1: Classes and objects (exercises 1–6)

### The words
| Word | Plain meaning | Swim example |
|---|---|---|
| **class** | a blueprint: describes what something *has* and what it can *do* | the idea "Swimmer" |
| **object** (= **instance**) | one real thing built from the blueprint | Diya, Kabir |
| **attribute** | a value stored on an object (what it *has*) | `diya.best_time` |
| **method** | a function that belongs to the class (what it can *do*) | `acc.deposit(50)` |
| **`__init__`** | runs automatically when you create an object. Sets up its attributes | |
| **`self`** | inside the class, "the object we're working on right now" | |

You've already used objects all day: `"abc".upper()` calls the `upper` method of a string object; `[1, 2].append(3)` calls `append` on a list object. Today you write your own.

### Your first class
```python
class Account:
    def __init__(self, owner):       # runs on Account("Diya")
        self.owner = owner           # store the value ON the object
        self.balance = 0             # start value, not passed in

    def deposit(self, amount):       # a method: first parameter is always self
        self.balance += amount

    def show(self):
        print(f"{self.owner}: {self.balance:.2f} EUR")

acc = Account("Diya")    # create an object. You don't pass self: Python does that
acc.deposit(100)         # Python runs Account.deposit(acc, 100), so self = acc
acc.show()               # Diya: 100.00 EUR
```
**Where `self` comes from:** `acc.deposit(100)` is turned into `Account.deposit(acc, 100)`. The object before the dot becomes `self`. That's how one method can work for thousands of different accounts.

### `__str__`: how your object prints
Without it, `print(acc)` shows `<__main__.Account object at 0x10a3f...>`. Add:
```python
    def __str__(self):
        return f"Account of {self.owner}"    # must RETURN a string
```

### Class attributes vs instance attributes
```python
class Transaction:
    currency = "EUR"        # CLASS attribute: one value, shared by every transaction
    count = 0

    def __init__(self, amount):
        self.amount = amount          # INSTANCE attribute: each object has its own
        Transaction.count += 1        # change the shared one through the class name
```
`t.currency` works: Python looks on the object first, doesn't find it, then looks on the class.

### Two names, one object
```python
a = Account("Diya")
b = a              # NOT a copy, just a second name for the same object
b.deposit(50)
print(a.balance)   # 50
print(a is b)      # True  (is = "the very same object?")
```
`==` asks "same value?", `is` asks "same object?".

### Common mistakes
- Forgetting `self` in the method definition: `def deposit(amount):` → `TypeError: takes 1 positional argument but 2 were given`.
- Writing `balance += amount` instead of `self.balance += amount` inside a method. Without `self.` it's just a local variable that disappears.
- `__init__` written as `_init_` (one underscore) or `__int__`. It must be **two underscores, init, two underscores**.
- `__str__` that *prints* instead of *returns*.

**Now do exercises 1–6.**

---

## Part 2: The 4 pillars of OOP

The 4 pillars are the 4 big ideas OOP is built on. Learn this table by heart. It's the interview answer.

| Pillar | One-line meaning | Python tools | Exercises |
|---|---|---|---|
| **Encapsulation** | keep the data and the rules about it together, and stop outsiders from breaking them | methods that check input, `_private` names, `@property` | 7–9 |
| **Inheritance** | a new class gets everything from an existing class, then adds or changes parts | `class Child(Parent)`, `super()` | 10–11 |
| **Polymorphism** | the same method call does different things depending on the object | overriding, duck typing, dunder methods | 12–13 |
| **Abstraction** | show only *what* something does, hide *how*. Force a common shape | `ABC`, `@abstractmethod` | 14 |

### Pillar 1: Encapsulation (exercises 7–9)

**The idea:** the account balance should never go below 0. If any code anywhere can write `acc.balance = -500`, that rule is just a hope. With encapsulation, the class itself guards its data.

**Step 1: check inside methods, and `raise` an error when the input is bad.**
```python
def withdraw(self, amount):
    if amount > self.balance:
        raise ValueError("insufficient funds")   # stops the method here: nothing changes
    self.balance -= amount
```
`raise` is the opposite of `try/except`: it **creates** an error on purpose. The caller catches it:
```python
try:
    acc.withdraw(500)
except ValueError as e:
    print("Refused:", e)        # Refused: insufficient funds
```

**Step 2: mark internal data with `_`.** `self._balance` means "internal, don't touch from outside". Python doesn't actually block it. It's a strong agreement between programmers. (Two underscores, `self.__balance`, makes Python rename it to `_Account__balance`, so it's harder to touch by accident. You'll rarely need that.)

**Step 3: `@property`, a method that looks like an attribute.**
```python
class Account:
    def __init__(self, owner):
        self.owner = owner
        self._balance = 0

    @property
    def balance(self):              # acc.balance  (no brackets) runs this
        return self._balance
```
Now `print(acc.balance)` works, but `acc.balance = 1_000_000` raises `AttributeError`, because there's no setter. The only way in is through `deposit`/`withdraw`, which check the rules.

**Step 4: a setter that validates.**
```python
class Swimmer:
    def __init__(self, name, best_time):
        self.name = name
        self.best_time = best_time         # no underscore: goes through the setter!

    @property
    def best_time(self):
        return self._best_time

    @best_time.setter
    def best_time(self, value):            # runs on  s.best_time = value
        if value <= 0:
            raise ValueError("time must be positive")
        self._best_time = value
```
Same name three times: the property (`best_time`), the setter decorator (`@best_time.setter`), the setter function (`best_time`). The real data hides in `_best_time`.

**Why at work:** a fraud system that lets an amount be negative or a probability be 1.7 produces wrong alerts quietly. Checks inside the class catch it at the moment it happens.

### Pillar 2: Inheritance (exercises 10–11)

**The idea:** an online transaction *is a* transaction with one extra thing (the IP country). Don't copy-paste the whole class. Inherit from it.
```python
class Transaction:                          # parent (also called base class / superclass)
    def __init__(self, tx_id, amount, channel):
        self.tx_id = tx_id
        self.amount = amount
        self.channel = channel

    def risk_score(self):
        return 1 if self.amount > 500 else 0

class OnlineTransaction(Transaction):       # child (subclass): gets EVERYTHING from Transaction
    def __init__(self, tx_id, amount, ip_country):
        super().__init__(tx_id, amount, "online")   # let the parent do its part
        self.ip_country = ip_country                # then add the new part

    def risk_score(self):                   # OVERRIDE: replace the parent's version ...
        score = super().risk_score()        # ... but reuse it inside
        if self.ip_country != "NL":
            score += 2
        return score

t = OnlineTransaction("TX9", 899.0, "NG")
print(t.amount)          # 899.0  (set by the parent's __init__)
print(t.risk_score())    # 3      (1 from the parent + 2 from the child)
```
- **`super()`** = "the parent class". `super().__init__(...)` runs the parent's setup. `super().risk_score()` runs the parent's version of the method.
- **Override** = the child defines a method with the same name. Python uses the child's version.
- When you call a method, Python looks in the object's class first, then the parent, then the grandparent... (this search order is called the **MRO**, method resolution order. See it with `OnlineTransaction.__mro__`).
- **`isinstance(t, Transaction)`** → `True` (a child object counts as its parent type). **`issubclass(OnlineTransaction, Transaction)`** → `True`.

### Pillar 3: Polymorphism (exercises 12–13)

"Poly" = many, "morph" = form. **The same call, different behaviour per object.**
```python
for t in [Transaction("A", 700, "in_store"), OnlineTransaction("B", 899, "NG")]:
    print(t.risk_score())     # 1, then 3. No "if type == ..." anywhere
```
Each object runs **its own** `risk_score`. Add a new transaction type tomorrow and this loop doesn't change.

**Duck typing:** Python doesn't check the family tree. It only checks *"does this object have a `risk_score` method?"* A class that inherits from nothing but has `risk_score()` works in the same loop. ("If it walks like a duck and quacks like a duck, it's a duck.") This is exactly why you can swap `LogisticRegression` for `RandomForestClassifier` in scikit-learn: both have `.fit()` and `.predict()`.

**Dunder methods** ("double underscore") are polymorphism with Python's own operators. You define them, and Python calls them for you:

| You write | Python calls |
|---|---|
| `print(x)`, `str(x)` | `x.__str__()` |
| `x` shown inside a list, or in the notebook | `x.__repr__()` |
| `a == b` | `a.__eq__(b)` |
| `a < b`, and `sorted()`, `min()`, `max()` | `a.__lt__(b)` |
| `len(x)` | `x.__len__()` |
| `a + b` | `a.__add__(b)` |

```python
class SwimResult:
    def __init__(self, swimmer, time_sec):
        self.swimmer, self.time_sec = swimmer, time_sec
    def __lt__(self, other):
        return self.time_sec < other.time_sec   # "smaller time" = "less than"

results = [SwimResult("Diya", 31.5), SwimResult("Kabir", 28.9)]
print(min(results).swimmer)     # Kabir: min() used our __lt__
```
`df["a"] + df["b"]` works in pandas because the Series class defines `__add__`.

### Pillar 4: Abstraction (exercise 14)

**The idea:** hide the *how*, show only the *what*. You drive a car with a steering wheel and pedals. You don't need to know how the engine works. In code: the fraud engine only needs to know *"every rule has a `check(tx)` method"*.

An **abstract base class** is a template that **can't be used directly**. It only says "every child must have these methods":
```python
from abc import ABC, abstractmethod

class FraudRule(ABC):
    @abstractmethod
    def check(self, tx):      # no real body: it's a promise, not code
        ...

class AmountRule(FraudRule):
    def __init__(self, limit):
        self.limit = limit
    def check(self, tx):      # the child MUST write this
        return tx["amount"] > self.limit

FraudRule()                   # TypeError: Can't instantiate abstract class ...
AmountRule(1000)              # fine
```
If a child forgets to write `check`, it can't be created either. You find out at once, not deep inside a production run.

**Abstraction vs encapsulation** (a favourite interview question): encapsulation *protects* the data inside one object (rules + hiding). Abstraction *simplifies the outside view*: users only see the important methods, and many classes can share one shape.

### Common mistakes (Part 2)
- Forgetting `super().__init__(...)` in the child: the parent's attributes are never created → `AttributeError`.
- A `@property` and an attribute with the **same name** inside the setter: `self.best_time = value` inside the setter calls the setter again, forever (`RecursionError`). Store in `self._best_time`.
- Writing `if isinstance(t, OnlineTransaction): ... elif ...` everywhere. That's the thing polymorphism replaces: put the different behaviour in each class's method.
- Using inheritance for "has-a". See Part 3.

**Now do exercises 7–14.**

---

## Part 3: Designing with classes (exercises 15–18)

### Composition: "has-a" vs "is-a"
| Relationship | Use | Example |
|---|---|---|
| **is a** | inheritance | `OnlineTransaction` **is a** `Transaction` |
| **has a** | composition: store objects inside another object | a `Customer` **has** transactions |

```python
class Customer:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.transactions = []           # a list of Transaction objects

    def add(self, tx):
        self.transactions.append(tx)

    def total_spent(self):
        return sum(t.amount for t in self.transactions)
```
A customer is not a kind of transaction, so `class Customer(Transaction)` would be wrong. Rule of thumb: **if "is a" sounds silly out loud, use composition.**

### Three kinds of methods
```python
class Transaction:
    def __init__(self, amount, hour):
        self.amount, self.hour = amount, hour

    def is_big(self):                 # normal method: uses THIS object (self)
        return self.amount > 1000

    @classmethod
    def from_text(cls, text):         # class method: gets the CLASS (cls). Usually a
        amount, hour = text.split(",")   # different way to CREATE an object
        return cls(float(amount), int(hour))

    @staticmethod
    def is_night(hour):               # static method: gets nothing. A plain helper function
        return 0 <= hour <= 5         #   that belongs with this class

t = Transaction.from_text("1500.0,3")
print(t.is_big(), Transaction.is_night(t.hour))   # True True
```
You'll see class methods in pandas: `pd.DataFrame.from_dict(...)`, `pd.Timestamp.now()`.

### The shared-list trap
```python
class Squad:
    members = []            # CLASS attribute: ONE list for ALL squads!
```
Every squad appends to the same list. Anything that should be separate per object (lists, dicts) must be created **inside `__init__`**: `self.members = []`.

### scikit-learn models are classes
```python
model = LogisticRegression(C=1.0)   # __init__: store the settings
model.fit(X_train, y_train)          # method: learn. Learned values get a trailing _: model.coef_
model.predict(X_test)                # method: use what was learned
```
In exercise 18 you build your own class with this exact shape, and run it in the same loop as a real scikit-learn model.

### Bonus (not in the exercises): `@dataclass`
For classes that mostly hold data, Python can write `__init__`, `__repr__` and `__eq__` for you:
```python
from dataclasses import dataclass

@dataclass
class SwimResult:
    swimmer: str
    time_sec: float

r = SwimResult("Kabir", 28.9)
print(r)             # SwimResult(swimmer='Kabir', time_sec=28.9)
```

### Common mistakes
- Making everything a class. A 5-line calculation is fine as a function. Use a class when you have **data + behaviour that belong together**, or many objects of the same kind.
- Mutable class attributes (the shared-list trap above).
- Calling `predict` before `fit`, or forgetting `return self` in `fit` (then `model.fit(X, y).predict(...)` fails on `None`).

**Now do exercises 15–18.** Then write 1–3 lines in `my-mistakes.md`.

---

## The interview answer, in 4 lines
> **Encapsulation**: bundle data with the methods that use it, and protect it (validation, `_private`, properties).
> **Inheritance**: a child class reuses and extends a parent class (`super()`), an "is-a" relationship.
> **Polymorphism**: one interface, many behaviours: the same method call works differently per class (overriding, duck typing).
> **Abstraction**: expose *what* an object does and hide *how*; abstract base classes force a common shape.
