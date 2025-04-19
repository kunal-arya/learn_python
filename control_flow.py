###############################################################
###############################################################
####
#### More Control Flow Tools
####
###############################################################
###############################################################

########################
## IF Statements
########################

# x = int(input("Please enter an integer: "))
# if x < 0:
#     x = 0
#     print("Negative Values changes to Zero")
# elif x == 0:
#     print("Zero")
# elif x == 1:
#     print("Single")
# else:
#     print("More")

########################
## FOR Statements
########################

# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# Interate over collections
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user,status in users.copy().items():
    if status == "inactive":
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user,status in users.items():
    if status == "active":
        active_users[user] = status

print(active_users, users)



########################
## The range() Function
########################

# generates arithmetic progressions
for i in range(5):
    print(i)

# 🧠 Key Points:
# range(end) generates numbers from 0 up to (but not including) end.

# The end point is never part of the sequence.

# You can also use range(start, end) to start from a different number.

# range(start, end, step) allows customizing the step (can be negative too!).


print(list(range(0, 10, 3)))
# ➞ [0, 3, 6, 9]

print(list(range(-10, -100, -30)))
# ➞ [-10, -40, -70]


# Iterate over the indices of a sequence, you can combine range() and len() as follows:
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print(range(10))
# returns a range object, not a list.

# The range object behaves like a list but doesn't store the sequence, saving memory.

# It's an iterable, meaning it can be used in constructs like for loops or functions expecting successive items.

# Example: computes the sum of 0 + 1 + 2 + 3, which is 6.
print(sum(range(4)))

########################
# 📌 Python Loop `else` Clause – Key Notes
########################

# - The `else` block after a `for` or `while` loop runs **only if the loop finishes normally (no `break`)**.
# - In a `for` loop: `else` runs after the last iteration, **if no `break`** was encountered.
# - In a `while` loop: `else` runs when the loop condition becomes false **without `break`**.
# - If the loop exits due to `break`, `return`, or an exception → `else` is **skipped**.

# ✅ Use case: Searching for something (like a factor or item)
#    - If found → `break` the loop
#    - If not found → `else` runs (e.g., "not found" message)

# 🔍 Example: Prime number check
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # runs only if inner loop didn’t `break` (i.e., no divisor found)
        print(n, 'is a prime number')

# 💡 Think of loop + else like:
#     - if/if/if/.../else
#     - If no `if` condition triggers `break`, then `else` runs

# 🧠 Analogy: Like `try/except/else`
#     - `try` has `else` for "no error"
#     - `loop` has `else` for "no break"

########################
# 📌 Python `pass` Statement – Key Notes
########################

# - `pass` is a **no-op** (does nothing). It's used when a statement is syntactically required but no action is needed.

# ✅ Common use cases:

# 1. Infinite loops with intentional pause (e.g., waiting for an interrupt)
# while True:
    # pass  # keeps the loop running (can use Ctrl+C to stop)

# 2. Creating minimal classes or function placeholders
class MyEmptyClass:
    pass  # class definition placeholder

def initlog(*args):
    pass  # TODO: implement later

# 3. Used in `if`, `for`, `while`, etc. when planning or stubbing code:
# if debug:
    # pass  # stub for future logging

# 💡 Helpful during development to maintain structure while skipping logic

########################
# 📌 Python `match` Statement – Pattern Matching (Python 3.10+)
########################

# ➤ `match <value>` compares against multiple `case` patterns, like a `switch`, but more powerful.
# ➤ Only the **first matching case** runs.
# ➤ `_` is a wildcard pattern (matches anything).

# 🔹 Basic Example:
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401 | 403 | 404:
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"
        

# ✅ Matching and binding values from tuples
point = (0, 5)
match point:
    case (0, 0):
        print("Origin")  # x = 0, y = 0
    case (0, y):
        print(f"Y={y}")  # x = 0, y = any → y is bound
    case (x, 0):
        print(f"X={x}")  # y = 0, x = any → x is bound
    case (x, y):
        print(f"X={x}, Y={y}")  # any (x, y) → both are bound, bound means assigning value that will be given by the user
    case _:
        raise ValueError("Not a point")

# ✅ Matching with custom classes
class Point:
    __match_args__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

# ✅ Matching lists or sequences with destructuring
points = [Point(0, 0), Point(0, 1)]
match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")

# ✅ Using guards (if conditions inside a match)
point = Point(3, 3)
match point:
    case Point(x, y) if x == y:
        print(f"Y = X at {x}")
    case Point(x, y):
        print("Not on the diagonal")

# ✅ Extended unpacking with * (like in function arguments)
sequence = [1, 2, 3, 4]
match sequence:
    case [x, y, *rest]:
        print(f"x={x}, y={y}, rest={rest}")

# ✅ Matching dictionaries (mapping patterns)
net = {"bandwidth": 100, "latency": 30}
match net:
    case {"bandwidth": b, "latency": l}:
        print(f"bw={b}, lat={l}")

# ✅ Matching with enums / constants using dotted names
from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color.RED
match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("Feeling blue")


########################
# 🔸 Python Functions - Differences from JavaScript
########################

# ✅ Docstrings: Optional string just after `def` — used for documentation
def greet():
    """This is a docstring — visible via help(greet) or __doc__"""
    print("Hello")

# ✅ Tuple unpacking in assignments (used a lot in Python)
a, b = 0, 1       # assigns 0 to a, 1 to b
a, b = b, a + b   # updates both a and b in one line (used in Fibonacci)

# ✅ No block braces: indentation defines function body (no `{}` like in JS)
#     → make sure spacing is consistent (PEP8 recommends 4 spaces)

# ✅ All variables inside a function are local by default
#     → can't reassign outer/global vars unless using `global` or `nonlocal`
# global x / nonlocal y (used in closures)

# ✅ Functions return `None` by default (like `undefined` in JS, but explicit)
def do_nothing():
    pass

print(do_nothing())  # → None

# ✅ Functions are objects (same as JS)
# You can assign, pass, or return them
f = greet
f()  # → "Hello"

# ✅ `append()` method (used for lists) is efficient
# result.append(a) instead of result = result + [a]

# ✅ No function overloading — last defined wins
# Can use default arguments or *args to handle multiple cases

# ✅ Python uses "call by object reference"
# Mutable args (like lists) can be changed inside the function


# ✅ Keyword Args (Python has native support)
def func(a, b=2): pass
func(b=3, a=1)  # Allowed
# JS: simulate with obj → func({ a: 1, b: 3 })


# ✅ Argument unpacking
args = [1, 2]
func(*args)
kwargs = {"a": 1}
func(**kwargs)
# JS: spread → func(...args)

# ✅ Lambda = JS arrow func, but 1-line only
add = lambda x, y: x + y
# JS: (x, y) => x + y

# ✅ Docstrings = Triple quotes
def foo():
    # \"\"\"This explains the function\"\"\"
    pass
# JS: /** doc comment */

# ✅ Type Hints (Like TS, not enforced)
def f(x: int) -> str: pass
# JS: Use TypeScript: (x: number): string => {}

# ✅ Style: PEP8
# snake_case, 4 spaces, True/False, None
# JS: camelCase, 2 spaces, true/false, null

# ========================================
# 🔁 Default Arguments in Python
# ========================================

# ✅ Default Args (Same in JS)
def greet(name="World"):
    pass
# JS: function greet(name = "World") {}

# ⚠️ Default args evaluated ONLY ONCE — can cause bugs with mutables!
def bad_func(x, arr=[]):  # BAD: arr is shared across calls
    arr.append(x)
    return arr

# ✅ Safe version — use None and assign inside
def good_func(x, arr=None):
    if arr is None:
        arr = []
    arr.append(x)
    return arr

# ========================================
# ✨ *args and **kwargs
# ========================================

# ✅ *args → collects extra positional arguments as a tuple
# ✅ **kwargs → collects extra keyword arguments as a dict

def demo(kind, *args, **kwargs):
    print("Kind:", kind)
    print("Positional:", args)   # tuple of extra positional args
    print("Keyword:", kwargs)    # dict of keyword args

# ➕ Usage:
demo("apple", 1, 2, 3, color="red", size="L")

# JS Equivalent:
# ...args is like *args
# JS has NO equivalent of **kwargs (needs manual object param)

# ========================================
# 🚦 Positional-only (/) and Keyword-only (*) args
# ========================================

def func(a, /, b, *, c):
    print(a, b, c)

# Meaning:
# a → positional-only (must pass by position)
# b → either positional or keyword
# c → keyword-only (must use c=...)

# ✅ func(1, 2, c=3)
# ❌ func(a=1, b=2, c=3) → a must be positional
# ❌ func(1, 2, 3) → c must be keyword

# JS: No equivalent — JS doesn't enforce how args are passed
