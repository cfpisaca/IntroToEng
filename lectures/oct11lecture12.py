# midterm - next week wednesday 20th

list.insert([1, 2, 3], 0, 999)
l1 = [1, 2, 3]
list.insert(l1, 0, 999)

# * terrible idea to name variables after types

l1[2] = 97
# returns l1
#         [999, 1, 97, 3]

result = 12
result = result + 1
# l1[[1]
# returns 1
# l1[1] = 13
# l1[1] = l1[1] + 123
# returns l1
#        [999, 136, 97, 3]

l1[1] = result == 54
# returns l1
#         [999, False, 97, 3]

mystr = "hello"
mystr[3]
# returns 'l'

mystr[3] = "e"
# cant set this to be something else
# * strings are immutable objects, can't change chars in strings using []

mystr.replace("l", "L")
'heLLothere'
# return mystr
'hellothere'
# still the same
mystr = mystr.replace("l", "L")
# set it equal in order to actually change variable

# * dont use += with lists
l1 = [1, 2, 3]
l2 = [10, 23, 44]
l1 + l2
# returns [1, 2, 3, 10, 23, 44]

# ** "use full to remember" - prof
mychar = "q"
mychar in "aeiou"
# returns False

mychar = "a"
mychar in "aeiou"
# returns True

mychar = "aa"
mychar in "aeiou"
# returns False

mystr = "hello"
for char in mystr:
    if char in "aeiou":
        print("vowel")
# returns vowel
#         vowel

# while loop
# while [test condition]:

# control + c, to end an infinite loop

i = 0
while i < len(mystr):
    if mystr[i] in "aeiou":
        print(mystr[i])
    i += 1

mylist = [1, 23, 4]
mylist.reserve()
mylist
# returns [4, 23, 1]

# lists are mutable

mystr = "hello"
reverse = ""
for char in mystr:
    revere = char + reverse
reverse
# returns 'olleh'
for char in mystr:
    reverse = reverse + char
reverse
# returns 'ollehhello'

mystr[::-1]
# return 'olleh'

mylist = [4, 23, 1]
# need to remove even numbers
for i in range(len(mylist)):
    print(mylist[i])
    if mylist[i] % 2 == 0:
        mylist.remove(mylist[i])
# * never change the length of list in a for loop
# for this statement in index two, the loop has an error


# ******** for lab

mylist = [12, 3, True, 4, False]
garbage = []
# take out booleans
for item in mylist:
    if type(item) == type(True):
        garbage.append(item)

mylist
# returns [12, 3, True, 4, False]
garbage
# returns [True, False]

for item in garbage:
    mylist.remove(item)

garbage
# returns [True, False]
mylist
# returns [12, 3, 4]

mylist = [12, 3, True, 4, False]
intlist = []
boollist = []

while mylist:
    if type(mylist[0]) == type(True):
        boollist.append(mylist[0])
    else:
        intlist.append(mylist[0])
    mylist.remove(mylist[0])

mylist
# returns []
intlist
# returns [12, 3, 4]
boollist
# returns [True, False]
