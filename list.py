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