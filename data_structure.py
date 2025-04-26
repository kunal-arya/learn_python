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