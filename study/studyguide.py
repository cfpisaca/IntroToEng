# ★★★ defining functions
def function(parameter1: type, parameter2: int):
    # contents go here
    print(parameter1)
    # parameters used inside contents

# ------------------------------------------------------

# ★★★ types of data in Python
# type() -> used to find type of data
# int - any integer & negative numbers
# float - any decimal value
# string - any text/chars in ""
# boolean - True or False statements (uppercase required)
# list - list of numbers in []

# ------------------------------------------------------

# ★★★ concatenation
# use plus to add or "concatenate" strings
print("Hello" + "World")
# returns 'HelloWorld'

# can also add int values to string
print("Hello" + str("2003"))
# returns 'Hello2003'
# will discuss conversions in later section

# ------------------------------------------------------

# ★★★ variables
vNum = 1
vFloat = 1.0
vStr = "string"
vBool = True
vList = []
# use <var> += 1 or <var> = <var> + 1 to add
# variables can have data types listed above

# ------------------------------------------------------

# ★★★ importing files
# lab5.function()
# from lab5 import *
# use these to import and test functions

# ------------------------------------------------------

# ★★★ conversions
# int() -> used to convert input to int
# > base output is 0
# > convert int to int
# > convert float to int
# > convert string containing num to int
# > Ex:
int("231")
#   returns 231
# > NO list

# float() -> used to convert input to float
# > base output is 0.0
# > convert float to float
# > convert int to float
# > convert string containing float to int
# > Ex:
float("1.2")
#   returns 1.2
# > NO list

# str() -> used to convert input to string
# > base output is ''
# > convert string to string
# > convert int to string
# > convert float to string
# > convert boolean to string
# > convert list to string

# bool() -> used to convert input to boolean
# > base output is False
# > True/False is True/False
# > 0/>1 is True/False
# > 0.0/>0.{infinite 0s}1 is True/False
# > ""/"..." is True/False
# > []/[...] is True/False

# list() -> used to convert input to list
# > base output is []
# > converts strings to list with index being each char
# > Ex:
list("Hello")
#   returns ['H', 'e', 'l', 'l', 'o']
# > NO int
# > NO float
# > NO boolean

# ------------------------------------------------------

# ★★★ boolean logic +
# boolean statements - True or False
# > capitalization matters

# defining variables - {=}

# testing for equality - {==}

# not equal to - {!=}

# less/greater than - {</>}
# less/greater than or equal to - {<=/>=}

# mod - {%}
# > divides and output is remainder
# > if no remainder - even
# > if remainder - odd

# addition - {+}
# subtraction - {-}
# multiplication - {*}
# float division - {/}
# integer division - {//}

# ------------------------------------------------------

# ★★★ predicates
# logic gates
# and - if both are True
# or - if one are True
# not - invert gate, gives opposite
# Ex: not (-/+)1
#     returns False
# Ex: not 0
#     returns True

# ------------------------------------------------------

# ★★★ conditionals
# if:
# elif:
# else:

# use predicates and boolean within conditionals

# ------------------------------------------------------

# ★★★ for in loops
# uses functions:
# > len() -> input of string, list, or range
# > Ex:
len("string")
#     returns 6
# > Ex:
len([1, "string", True])
#     returns 3
# > Ex:
len(range(0, 9))
#     return 9
# > range() -> start and end of a function starting at index 0
#   > range(stop)
#   > range(start, stop,[, step])
#   > only takes ints
#   > for range(0,9) it only prints numbers 0-8

# ★★ for i in loop
# > goes through ith items in strings/lists and returns
# > Ex:
p1 = [1, "string", True]
for i in p1:
    print(i)
# returns 1
#         2
#         string
#         True

# > Ex:
p1 = "look"
for i in p1:
    print(i)
# returns l
#         o
#         o
#         k

# ★★ for i in range loops
# goes through ith items in range of int and returns
# > Ex:
p1 = 3
for i in range(p1):
    print(i)
# returns 0
#         1
#         2
# > Ex:
p1 = 1
p2 = 4
p3 = 2
for i in range(p1, p2, p3):
    print(i)
# returns 1
#         3

# ------------------------------------------------------

# ★★★ indexing
# index loops to iterate for specific numeric value
# > Ex:
p1 = [1, "hello", 23, 4]
for i in range(len(p1)):
    print(p1[i])

# returns 1
#         hello
#         23
#         4
# > Ex:


def find_vowels(p1: str):
    vowels = ""
    for i in range(len(p1)):
        if p1[i] in "aeiou":
            vowels = vowels + p1[i]
    return vowels
# returns eo

# ★★ direct indexing
# mylist = [23, 7, 3, 789, 12, 43, 90, 8, 1098]
# mylist = [beg, end, step] - end will return index before end index

# > Ex: mylist[3:7] - *start at index 3, *end at index 7-1, step of 1
# returns [789, 12, 43, 90]

# > Ex: mylist[3:7:2] - *start at index 3, *end at index 7-1, *step of 2
# returns [789, 43]

# > Ex: mylist[3:] - *start at index 3, end at last index, step of 1
# returns [789, 12, 43, 90, 8, 1098]

# > Ex: mylist[:8] - start at first index, *end at index 8-1, step of 1
# returns [23, 7, 3, 789, 12, 43, 90, 8]

# > Ex: mylist[::2] - start at first index, end at last index, *step of 2
# returns [23, 3, 12, 90, 1098]

# > Ex: mylist[:5:2] - start at first index, *end at index 5, *step of 2
# returns [23, 3, 12]

# > Ex: mylist[2::3] - *start at first index, end at last index, *step of 3
# returns [3, 43, 1098]

# ------------------------------------------------------

# ★★★ functions and methods
# a function can take any data type
# a method can only take a certain data type

# ★ .split("<char>") -> NO ALTER, specific to str
# doesn't change str
# splits a string at a character
# > returns list
# Ex:
p1 = "Hello, world"
p1.split(", ")
# returns ['Hello', 'world']
# have to set:
p1 = p1.split(", ")
# to actually change the value of the list

# ★ .find("<char>", start, end) -> specific to str
# finds the index of a char/str in a string
# when applying an index, the end is index-1
# returns int
# returns -1 if char/str is not found
# Ex:
p1 = "syracuse orange"
p1.find("o", 0, 9)
# returns -1

# Ex:
p1.find("o", 0, 10)
# returns 9

# ★ .count("<char>", start, end) -> specific to str/list
# returns number of occurrences in list/str
# returns int
# Ex:
p1 = ["hello", "world", "carlo", "hello"]
p1.count("hello")
# returns 2

# Ex:
p1 = "orange nation yo"
p1.count("o", 0, 1)
# returns 1

# ★ .sort(<none>) -> ALTER, specific to list
# changes list
# sorts list by lowest number
# Ex:
p1 = [1, 3, 9, 1, 2, 99, 34, 14]
p1.sort()
# returns [1, 1, 2, 3, 9, 14, 34, 99]

# ★ .reverse(<none>) -> ALTER, specific to list
# changes list
# reverses the order of the list
# Ex:
p1 = [1, 3, 9, 1, 2, 99, 34, 14]
p1.reverse()
# returns [14, 34, 99, 2, 1, 9, 3, 1]

# Ex:
# can also be used with sort
p1 = [1, 3, 9, 1, 2, 99, 34, 14]
p1.sort(reverse=True)
# returns [99, 34, 14, 9, 3, 2, 1, 1]

# ★ .startswith("<char>", start, end) -> specific to str
# takes in a string and tests if starts with string
# returns boolean statement
# Ex:
p1 = "god"
p1.startswith("g")
# returns True

# Ex:
p1 = "god is life"
p1.startswith("l", 7)
# returns True

# Ex:
p1 = "god is life"
p1.startswith("l", 8)
# returns False

# ★ .join("<char/separator>") -> NO ALTER, specific to str
# joins at a separator
# Ex:
mylist = ["a", "bc"]
sep = "-"
mylist = sep.join(mylist)
# returns 'a-bc'

# Ex:
mylist = "hello"
sep = "~~"
mylist = mylist.join(sep)
# returns "~hello~"

# Ex:
mylist = "hello"
sep = "~"
mylist = mylist.join(sep)
# returns "~"

# ★ .replace(<old>, <new>, <count>) -> NO ALTER, specific to str
# replaces a char in a str with a new one
# Ex:
p1 = "['Carlo', 'how', 'are', 'you']"
p1 = p1.replace("[", "")
p1 = p1.replace("]", "")
p1 = p1.replace("'", "")
p1 = p1.replace(",", "")
# returns 'Carlo how are you'

# Ex:
p1 = "['Carlo', 'how', 'are', 'you']"
p1 = p1.replace("[", "")
p1 = p1.replace("]", "")
p1 = p1.replace("'", "")
p1 = p1.replace(",", "", 2)
# returns 'Carlo how are, you'

# ★ .strip("<char>") -> NO ALTER, specific to str
# strips chars from a str
# Ex:
p1 = "www.google.com"
p1 = p1.strip("wcom.")
# returns 'google'

# ★ .insert(<index>, <item>) -> ALTER, specific to list
# inserts an item into a list at a certain index
# Ex:
mylist = ["hello", "iello", "jello", "kello"]
mylist.insert(2, "ijello")
# returns ['hello', 'iello', 'ijello', 'jello', 'kello']

# ★ .remove(<item>) -> ALTER, specific to list
# removes an item from a list
# Ex:
mylist = [1, True, 34, "str"]
mylist.remove(1)
mylist
# returns [True, 34, 'str']

# ★ .append(<item>) -> ALTER, specific to list
# adds an item to a list
# Ex:
mylist = [1, True, 34, "str"]
mylist.append("new")
mylist
# returns [1, True, 34, 'str', 'new']

# ★ .clear() -> ALTER, specific to list
# clears a list
# Ex:
mylist = ["so", "many", "items", "in", "this", "list"]
mylist.clear()
# returns []

# ★ .format(<item>) -> NO ALTER, specific to str
# used to concatenate strings
# Ex:
str.format("{0} some message {1}", "hi", "there")
# return 'hi some message there'

