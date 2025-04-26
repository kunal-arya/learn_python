# Basics: Syntax, variables, operators
## url - https://docs.python.org/3/tutorial/introduction.html

###############################################################
#### Numbers
###############################################################


## The integer numbers (e.g. 2, 4, 20) have type int, 
print(2 * 4)

# the ones with a fractional part (e.g. 5.0, 1.6) have type float.
print(5.0 * 1.6)

# Division (/) always returns a float. 
print(17 / 3)

# To do floor division and get an integer result you can use the // operator
print(17 // 3)

# to calculate the remainder you can use %
print(17 % 3)

# use the ** operator to calculate powers
print(2 ** 3)

# operators with mixed type operands convert the integer operand to floating point
print(4 * 3.75 - 1)

###############################################################
#### Text
###############################################################

# If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

# String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''.
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# Strings can be concatenated (glued together) with the + operator, and repeated with *:
## 3 times 'un', followed by 'ium'
print(3 * 'un' + 'ium')

# Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
## This feature is particularly useful when you want to break long strings
print("py" "thon")
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

# If you want to concatenate variables or a variable and a literal, use +:
prefix = "py"
print(prefix + 'thon')

# While indexing is used to obtain individual characters, slicing allows you to obtain a substring:
word = "Python"
print(word[0:2])  # characters from position 0 (included) to 2 (excluded)
print(word[2:5])  # characters from position 2 (included) to 5 (excluded)
print(word[-1]) # last character

# Slice indices have useful defaults; an omitted first index defaults to zero, 
# an omitted second index defaults to the size of the string being sliced.
print(word[:2])   # character from the beginning to position 2 (excluded)
print(word[4:])  # characters from position 4 (included) to the end
print(word[-2:])  # characters from the second-last (included) to the end

# Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s:
print(word[:2] + word[2:])
# 'Python'
print(word[:4] + word[4:])
# 'Python'

# Attempting to use an index that is too large will result in an error:
# print(word[42])  # the word only has 6 characters

# However, out of range slice indexes are handled gracefully when used for slicing:
print(word[4:42])
print(word[42:])

# Python strings cannot be changed
## they are immutable. Therefore, assigning to an indexed position in the string results in an error:
## word[0] = 'J'
## word[2:] = 'py'

# If you need a different string, you should create a new one:
print('J' + word[1:])
# 'Jython'
print(word[:2] + 'py')
# 'Pypy'

# The built-in function len() returns the length of a string:
s = 'supercalifragilisticexpialidocious'
len_s = len(s)
print(len_s)

###############################################################
#### Lists
###############################################################

#  Lists might contain items of different types, but usually the items all have the same type.
squares = [1, 4, 9, 16, 25]
print(squares)

# Like strings (and all other built-in sequence types), lists can be indexed and sliced:
print(squares[0])  # indexing returns the item
# 1
print(squares[-1])
# 25
print(squares[-3:])  # slicing returns a new list
# [9, 16, 25]

# Lists also support operations like concatenation:
squares = squares + [36, 49, 64, 81, 100]
print(squares)

# Unlike strings, which are immutable, 
# lists are a mutable type, i.e. it is possible to change their content:
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64  # replace the wrong value
print(cubes)

# add new items at the end of the list, by using the list.append() method
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
print(cubes)

# Simple assignment in Python never copies data. 
# When you assign a list to a variable, 
# the variable refers to the existing list.
# Any changes you make to the list through one variable 
# will be seen through all other variables that refer to it.
rgb = ["Red", "Green", "Blue"]
rgba = rgb
print(id(rgb), id(rgba),id(rgb) == id(rgba))  # they reference the same object
# True
rgba.append("Alph")
print(rgb)
# ["Red", "Green", "Blue", "Alph"]

############################
########### Copy       Type	  Outer Object	 Inner Objects (Nested)	   Shared?
########### Shallow    Copy	  New	         Same references	   Yes
########### Deep       Copy	  New	         New recursive copies	   No
############################

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)
# ['a', 'b', 'C', 'D', 'E', 'f', 'g']

# now remove them
letters[2:5] = []
print(letters)
# ['a', 'b', 'f', 'g']

# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)

# nest lists (create lists containing other lists)
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

print(x)
# [['a', 'b', 'c'], [1, 2, 3]]

print(x[0])
# ['a', 'b', 'c']

print(x[0][1])
# 'b'

# reverse your list using slice method
alphabets = ["A","E","I","O","U"]
print(alphabets[::-1])