# Python OOP cheatsheet

## Basics
| Thing | What it does | Tiny example |
|---|---|---|
| `class Name:` | define a blueprint | `class Swimmer:` |
| `__init__(self, ...)` | set up a new object's attributes | `self.name = name` |
| `self` | the current object (Python passes it for you) | `self.balance += x` |
| `obj = Name(...)` | create an object (instance) | `acc = Account("Diya")` |
| `obj.attr` / `obj.method()` | read data / call behaviour | `acc.deposit(50)` |
| class attribute | one value shared by all objects | `currency = "EUR"` under `class` |
| `a is b` | same object? (`==` = same value?) | `b = a` → `a is b` is `True` |

## Encapsulation
| Thing | What it does | Tiny example |
|---|---|---|
| `raise ValueError("...")` | refuse bad input | `if amount <= 0: raise ValueError("...")` |
| `_name` | "internal, don't touch" (convention) | `self._balance = 0` |
| `@property` | method read like an attribute | `acc.balance` → returns `self._balance` |
| `@x.setter` | runs on `obj.x = value`, can validate | `@best_time.setter` |

## Inheritance
| Thing | What it does | Tiny example |
|---|---|---|
| `class Child(Parent):` | child gets everything from parent | `class OnlineTransaction(Transaction):` |
| `super().__init__(...)` | run the parent's setup | first line of child `__init__` |
| override | same method name in child replaces parent's | `def risk_score(self):` |
| `super().method()` | call the parent's version inside an override | `score = super().risk_score()` |
| `isinstance(obj, Cls)` | is obj a Cls (or a child of it)? | `isinstance(t, Transaction)` |
| `issubclass(A, B)` | is class A a child of B? | `issubclass(OnlineTransaction, Transaction)` |

## Polymorphism and dunder methods
| You write | Python calls | Return |
|---|---|---|
| `print(x)` | `__str__` | a string |
| shown in a list | `__repr__` | a string |
| `a == b` | `__eq__` | `True`/`False` |
| `a < b`, `sorted`, `min`, `max` | `__lt__` | `True`/`False` |
| `len(x)` | `__len__` | an int |
| `a + b` | `__add__` | a new object |

Duck typing: any object with the right method works. No shared parent needed.

## Abstraction
```python
from abc import ABC, abstractmethod
class FraudRule(ABC):
    @abstractmethod
    def check(self, tx): ...      # children MUST implement; FraudRule() -> TypeError
```

## Design
| Thing | When | Tiny example |
|---|---|---|
| inheritance | "is a" | `OnlineTransaction` is a `Transaction` |
| composition | "has a" | `self.transactions = []` in `Customer` |
| `@classmethod` (gets `cls`) | another way to create objects | `Transaction.from_row(row)` |
| `@staticmethod` (gets nothing) | helper that belongs with the class | `Transaction.is_night(3)` |
| `@dataclass` | data-holding class, auto `__init__`/`__repr__`/`__eq__` | `swimmer: str` |
| sklearn shape | `__init__` settings, `fit` learns (`name_`), `predict` uses | `model.fit(X, y).predict(X2)` |

## Traps
- Missing `self` in `def method(self)` → "takes 1 positional argument but 2 were given"
- Child `__init__` without `super().__init__()` → parent attributes missing
- `members = []` as a class attribute → shared by every object. Put it in `__init__`
- Setter that assigns `self.x` instead of `self._x` → infinite recursion
