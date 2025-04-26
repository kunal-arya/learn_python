# PYTHON LIST OPERATIONS WITH JAVASCRIPT COMPARISONS
# -------------------------------------------------

# CREATION
fruits = ['apple', 'banana', 'orange']  # Similar to JS: const fruits = ['apple', 'banana', 'orange']
numbers = list(range(10))  # Creates [0,1,2,3,4,5,6,7,8,9] - JS: Array.from({length: 10}, (_, i) => i)

# LENGTH
len(fruits)  # Returns the length - JS: fruits.length

# MEMBERSHIP TESTING
'apple' in fruits  # Returns True/False - JS: fruits.includes('apple') or fruits.indexOf('apple') !== -1

# ACCESS BY INDEX
fruits[0]   # First element - Same in JS
fruits[-1]  # Last element - JS: fruits[fruits.length - 1] (JS has no negative indexing)

# SLICING
fruits[1:3]  # From index 1 up to but not including 3 - JS: fruits.slice(1, 3)

# ADDING ELEMENTS
fruits.append('grape')  # Add to end - JS: fruits.push('grape')
fruits.extend(['kiwi', 'mango'])  # Add multiple items - JS: fruits.push(...['kiwi', 'mango'])
fruits.insert(1, 'pear')  # Insert at position - JS: fruits.splice(1, 0, 'pear')

# REMOVING ELEMENTS
fruits.remove('apple')  # Remove by value - JS: const index = fruits.indexOf('apple'); if (index > -1) fruits.splice(index, 1)
last_item = fruits.pop()  # Remove & return last - JS: const lastItem = fruits.pop()
first_item = fruits.pop(0)  # Remove & return first - JS: const firstItem = fruits.shift()
fruits.clear()  # Remove all items - JS: fruits.length = 0
del fruits[0]  # Delete by index - JS: fruits.splice(0, 1)
del fruits[1:3]  # Delete slice - JS: fruits.splice(1, 2)

# FINDING ELEMENTS
fruits.index('banana')  # Index of first occurrence - JS: fruits.indexOf('banana')
fruits.index('banana', 4)  # Search starting from index 4 - JS: fruits.indexOf('banana', 4)
fruits.count('apple')  # Count occurrences - JS: fruits.filter(item => item === 'apple').length

# SORTING
fruits.sort()  # Sort in-place - JS: fruits.sort() (both modify original)
fruits.sort(key=len)  # Sort by function - JS: fruits.sort((a, b) => a.length - b.length)
fruits.sort(reverse=True)  # Reverse sort - JS: fruits.sort().reverse()
fruits.reverse()  # Reverse list - JS: fruits.reverse()
sorted_fruits = sorted(fruits)  # Return new sorted list - JS: const sortedFruits = [...fruits].sort()

# COPYING
new_fruits = fruits.copy()  # Shallow copy - JS: const newFruits = [...fruits] or fruits.slice()

# LIST AS STACK (LIFO)
stack = []
stack.append('item')  # Push - JS: stack.push('item')
item = stack.pop()  # Pop - JS: const item = stack.pop()

# LIST AS QUEUE (FIFO) - inefficient, better use collections.deque
queue = []
queue.append('item')  # Enqueue - JS: queue.push('item')
item = queue.pop(0)  # Dequeue - JS: const item = queue.shift()

# Better queue in Python
from collections import deque
queue = deque()
queue.append('item')  # Enqueue
item = queue.popleft()  # Dequeue - Much more efficient than list.pop(0)

# LIST COMPREHENSIONS
squares = [x**2 for x in range(10)]  # JS: const squares = Array.from({length: 10}, (_, x) => x**2)
evens = [x for x in range(10) if x % 2 == 0]  # JS: Array.from({length: 10}, (_, x) => x).filter(x => x % 2 === 0)

# NESTED LIST COMPREHENSIONS
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(3)]  # JS: matrix[0].map((_, colIndex) => matrix.map(row => row[colIndex]))

# Alternative to nested comprehension 
transposed_alt = list(zip(*matrix))  # Transpose using zip and unpacking - Elegant Python solution

# KEY DIFFERENCES FROM JAVASCRIPT:
# 1. Python lists return None for modifying operations, JS often returns useful values
# 2. Python has powerful list comprehensions built into the language
# 3. Python has negative indexing (fruits[-1]), JS doesn't
# 4. Python has the 'del' statement for deletion
# 5. Python has more specialized data structures in standard library (like deque)
# 6. Python slicing is more powerful with step parameter: fruits[0:5:2]

# Python Tuples
# ------------

# ✅ Tuple = Immutable, ordered collection
# - Similar to JS arrays but **cannot be modified**
# - Items can be of different types (int, str, etc.)
# - Defined using parentheses () or just commas

# Examples:
t1 = (1, 2, 3)           # Normal tuple
t2 = 1, 2, 3             # Also a tuple — commas define it!
t3 = ("a", 3.14, True)   # Mixed types
t4 = (42,)               # ✅ Single-element tuple — must use comma

# ❌ Immutable:
# t1[0] = 100   → TypeError: 'tuple' object does not support item assignment

# ✅ You can:
# - Access by index → t1[1] → 2
# - Iterate → for x in t1
# - Nest tuples → ((1, 2), (3, 4))

# 🧠 Use when:
# - You want a fixed collection of items
# - You want to use it as a dict key or set element (requires immutability)

# 🔁 JS comparison:
# - Closest match is an array, but with `Object.freeze()` (kinda)
# - Tuples = lightweight, immutable data containers

# Creating tuples - comma-separated values with optional parentheses
t = 12345, 54321, 'hello!'  # Tuple packing
# Same as: t = (12345, 54321, 'hello!')
# JS equivalent: const t = [12345, 54321, 'hello!']; // JS uses arrays, no direct tuple equivalent

# Accessing tuple elements works like lists
first_element = t[0]  # Returns 12345
# JS equivalent: const firstElement = t[0]; // Same syntax in JS

# Tuples can be nested
nested_tuple = t, (1, 2, 3, 4, 5)  # Creates ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
# JS equivalent: const nestedArray = [t, [1, 2, 3, 4, 5]]; // Nested arrays in JS

# Tuples are immutable - this would cause an error:
# t[0] = 88888  # TypeError: 'tuple' object does not support item assignment
# JS difference: JS arrays are mutable, so this would work: t[0] = 88888;
# JS immutable alternative: const t = Object.freeze([12345, 54321, 'hello!']);

# Tuples can contain mutable objects
tuple_with_lists = ([1, 2, 3], [3, 2, 1])  # The lists inside can be modified
# JS equivalent: const arrayWithArrays = [[1, 2, 3], [3, 2, 1]];

# Special cases for tuples
empty_tuple = ()  # Empty tuple
# JS equivalent: const emptyArray = [];

singleton_tuple = 'hello',  # Single element tuple MUST have trailing comma
# JS equivalent: const singletonArray = ['hello']; // No special syntax needed in JS

# Tuple unpacking - assigning tuple values to variables
x, y, z = t  # x gets 12345, y gets 54321, z gets 'hello!'
# JS equivalent: const [x, y, z] = t; // Destructuring assignment in JS

# Python Sets
# ----------

# Creating sets - uses curly braces
fruits = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}  # Duplicates are removed
# JS equivalent: const fruits = new Set(['apple', 'orange', 'apple', 'pear', 'orange', 'banana']);

# Empty set must use set() constructor, not {}
empty_set = set()  # {} would create an empty dictionary
# JS equivalent: const emptySet = new Set();

# Fast membership testing
'orange' in fruits  # Returns True
# JS equivalent: fruits.has('orange'); // Returns true

'kiwi' in fruits    # Returns False
# JS equivalent: fruits.has('kiwi'); // Returns false

# Set operations
a = set('abracadabra')  # Creates {'a', 'r', 'b', 'c', 'd'}
# JS equivalent: const a = new Set('abracadabra'.split(''));

b = set('alacazam')     # Creates {'a', 'l', 'c', 'z', 'm'}
# JS equivalent: const b = new Set('alacazam'.split(''));

# Python set operations have no direct equivalents in JS Set
# You need custom functions or use library like lodash

# Difference (elements in a but not in b)
difference = a - b      # Elements in a but not in b: {'r', 'd', 'b'}
# JS equivalent:
# const difference = new Set([...a].filter(x => !b.has(x)));

# Union (elements in either a or b)
union = a | b           # Elements in either a or b: {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
# JS equivalent:
# const union = new Set([...a, ...b]);

# Intersection (elements in both a and b)
intersection = a & b    # Elements in both a and b: {'a', 'c'}
# JS equivalent:
# const intersection = new Set([...a].filter(x => b.has(x)));

# Symmetric difference (in a or b but not both)
sym_diff = a ^ b        # In a or b but not both: {'r', 'd', 'b', 'm', 'z', 'l'}
# JS equivalent:
# const symDiff = new Set([...a].filter(x => !b.has(x)).concat([...b].filter(x => !a.has(x))));

# Set comprehension
filtered_set = {x for x in 'abracadabra' if x not in 'abc'}  # Creates {'r', 'd'}
# JS equivalent:
# const filteredSet = new Set('abracadabra'.split('').filter(x => !['a','b','c'].includes(x)));

# Python Dictionaries
# ------------------

# Creating a dictionary with initial key-value pairs
tel = {'jack': 4098, 'sape': 4139}
# JS equivalent: const tel = {'jack': 4098, 'sape': 4139}; // JS objects are similar to Python dictionaries

# Adding a new key-value pair
tel['guido'] = 4127  # Adds 'guido': 4127 to the dictionary
# JS equivalent: tel['guido'] = 4127; // Same syntax in JS

# Accessing values by key
jack_number = tel['jack']  # Returns 4098
# JS equivalent: const jackNumber = tel['jack']; // Same syntax in JS

# Deleting a key-value pair
del tel['sape']  # Removes the 'sape' entry
# JS equivalent: delete tel['sape']; // Similar but uses delete operator in JS

# Getting all keys as a list (in insertion order)
keys_list = list(tel)  # Returns ['jack', 'guido', 'irv']
# JS equivalent: const keysList = Object.keys(tel); // Similar function in JS

# Getting sorted keys
sorted_keys = sorted(tel)  # Returns keys in alphabetical order
# JS equivalent: const sortedKeys = Object.keys(tel).sort();

# Checking if a key exists
'guido' in tel  # Returns True
# JS equivalent: 'guido' in tel; // Same syntax in JS
# Or more commonly: tel.hasOwnProperty('guido');

'jack' not in tel  # Returns False
# JS equivalent: !('jack' in tel); // Need to negate in JS

# Creating dictionaries using dict() constructor
contact_dict = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# JS equivalent: const contactDict = Object.fromEntries([['sape', 4139], ['guido', 4127], ['jack', 4098]]);

# Dictionary comprehension
square_dict = {x: x**2 for x in (2, 4, 6)}  # Creates {2: 4, 4: 16, 6: 36}
# JS equivalent: const squareDict = Object.fromEntries([2, 4, 6].map(x => [x, x**2]));

# Creating dictionaries with keyword arguments (only for string keys)
contact_dict = dict(sape=4139, guido=4127, jack=4098)
# JS equivalent: const contactDict = {sape: 4139, guido: 4127, jack: 4098};


# Python Looping Techniques
# ------------------------

# Looping through dictionary keys and values with items()
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
# JS equivalent:
# Object.entries(knights).forEach(([k, v]) => {
#     console.log(k, v);
# });

# Loop with index position using enumerate()
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)  # 0 tic, 1 tac, 2 toe
# JS equivalent:
# ['tic', 'tac', 'toe'].forEach((v, i) => {
#     console.log(i, v);
# });

# Looping over multiple sequences with zip()
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print(f'What is your {q}? It is {a}.')
# JS equivalent:
# questions.forEach((q, i) => {
#     const a = answers[i];
#     console.log(`What is your ${q}? It is ${a}.`);
# });

# Looping in reverse order
for i in reversed(range(1, 10, 2)):
    print(i)  # Prints 9, 7, 5, 3, 1
# JS equivalent:
# [...Array(5)].map((_, i) => 1 + i*2).reverse().forEach(i => {
#     console.log(i);
# });

# Looping over sorted sequence
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)  # Prints items in alphabetical order
# JS equivalent:
# [...basket].sort().forEach(i => {
#     console.log(i);
# });

# Looping over unique items in sorted order
for f in sorted(set(basket)):
    print(f)  # Prints unique items in alphabetical order
# JS equivalent:
# [...new Set(basket)].sort().forEach(f => {
#     console.log(f);
# });

# Creating a new list while filtering items (safer than modifying while iterating)
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
# JS equivalent:
# const filteredData = rawData.filter(value => !Number.isNaN(value));

# Python Conditions
# ----------------

# Comparison operators in conditions
x = 5
y = 10
if x < y:  # Less than
    print("x is less than y")
# JS equivalent: if (x < y) { console.log("x is less than y"); }

# Membership operators
fruits = ['apple', 'banana', 'orange']
if 'apple' in fruits:  # Checks if 'apple' is in the list
    print("Found apple")
# JS equivalent: if (fruits.includes('apple')) { console.log("Found apple"); }

if 'grape' not in fruits:  # Checks if 'grape' is not in the list
    print("No grapes")
# JS equivalent: if (!fruits.includes('grape')) { console.log("No grapes"); }

# Identity operators
a = [1, 2, 3]
b = [1, 2, 3]
c = a

if a is c:  # Checks if a and c are the same object (they are)
    print("a and c are the same object")
# JS equivalent: if (a === c) { console.log("a and c are the same object"); }

if a is not b:  # Checks if a and b are different objects (they are)
    print("a and b are different objects")
# JS equivalent: if (a !== b) { console.log("a and b are different objects"); }

# Chained comparisons
n = 5
if 1 < n < 10:  # Checks if n is between 1 and 10
    print("n is between 1 and 10")
# JS equivalent: if (1 < n && n < 10) { console.log("n is between 1 and 10"); }

# Boolean operators with short-circuit evaluation
x = 5
y = 0
if x > 0 and y > 0:  # y > 0 is evaluated only if x > 0 is True
    print("Both x and y are positive")
# JS equivalent: if (x > 0 && y > 0) { console.log("Both x and y are positive"); }

if x > 0 or y > 0:  # y > 0 is not evaluated if x > 0 is True
    print("At least one of x or y is positive")
# JS equivalent: if (x > 0 || y > 0) { console.log("At least one of x or y is positive"); }

# Assigning Boolean results to variables
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3  # Returns first non-empty string
# JS equivalent: const nonNull = string1 || string2 || string3;

# The walrus operator := (Python 3.8+) for assignment in expressions
# No direct JS equivalent, but similar to combining assignment with evaluation
numbers = [1, 2, 3, 4, 5]
if (n := len(numbers)) > 3:  # Assigns n = 5, then checks if n > 3
    print(f"List has {n} items")
# JS equivalent: const n = numbers.length; if (n > 3) { console.log(`List has ${n} items`); }


# Comparing Sequences and Other Types
# ----------------------------------

# Lexicographical comparison of sequences
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
if tuple1 < tuple2:  # Compares items one by one until a difference is found
    print("tuple1 is less than tuple2")
# JS equivalent: 
# // No direct equivalent, would need custom comparison function
# if (JSON.stringify(tuple1) < JSON.stringify(tuple2)) { console.log("tuple1 is less than tuple2"); }


# ✅ String comparison in Python (lexicographic, Unicode-based)
if 'ABC' < 'Python':
    print("ABC comes before Python")  # ✅ Printed

# 📌 Why?
# - Python compares strings using Unicode code points
# - Comparison is done character by character
# - 'A' = 65, 'P' = 80 → so 'A' < 'P' → 'ABC' < 'Python' is True
# 🧠 Mnemonic: Like dictionary order — stops at first difference

# 🔁 JS equivalent:
# if ('ABC' < 'Python') {
#     console.log("ABC comes before Python");
# }

# ✅ Tuple (and sequence) comparison in Python

# 🧠 Rule 1: Python compares sequences **element by element**, from left to right
# - Like dictionary order
# - Comparison stops at the first difference


# 🔸 Comparing sequences of different lengths

if (1, 2) < (1, 2, -1):
    print("(1, 2) is less than (1, 2, -1)")  # ✅ True

# 📌 Explanation:
# - Python sees: 1 == 1 → continue
# - Then: 2 == 2 → continue
# - Now: first tuple ends, second tuple still has more → first is smaller
# - Just like in a dictionary, "cat" < "cater"

# 🧠 Think of it like this:
# - A shorter tuple that’s a **prefix** of a longer one is considered smaller

# 🔁 JS equivalent:
# // JS doesn’t compare arrays like this — you'd need to write a custom function:
# function compareTuples(a, b) { ... }

# 🔸 Comparing sequences with nested structures

if (1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4):
    print("First tuple is less than second tuple")  # ✅ True

# 📌 Explanation:
# - 1 == 1 → continue
# - 2 == 2 → continue
# - ('aa', 'ab') < ('abc', 'a') → this is true
#   → because 'aa' < 'abc' (string comparison)
# - Since this part differs, Python doesn’t even check the trailing 4

# 🧠 Tuples are compared **recursively**, element-by-element, including inner tuples

# 🔁 JS equivalent:
# // No built-in way to compare nested arrays/tuples — must write custom logic

# 🔸 Mixed numeric type comparison

if 1 == 1.0:
    print("1 equals 1.0")  # ✅ True

# 📌 Explanation:
# - Python considers int and float as numeric types → compares by value
# - 1 == 1.0 → True

# 🔁 JS equivalent:
# if (1 === 1.0) { console.log("1 equals 1.0"); }  // ✅ Also true in JS
# JS auto-converts between number types during comparison

# 🔸 Comparing completely different types

# list1 = [1, 2]
# dict1 = {'a': 1}
# if list1 < dict1:  # ❌ Raises TypeError in Python
#     print("This will cause an error")

# 📌 Explanation:
# - Python doesn’t allow comparison between incompatible types like list vs dict
# - Raises a TypeError: '<' not supported between instances of 'list' and 'dict'

# 🔁 JS equivalent:
# // JS converts both to strings → doesn't raise error, but gives nonsense
# console.log([1, 2] < { a: 1 });  // → true or false depending on weird coercion

# 🧠 Summary:
# Python = strict → TypeError on bad comparisons
# JS = loose → weird coercions, may lead to bugs
