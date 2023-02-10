# break/continue
# try/except
# julia programming language


lines = ["jen:88\n," "joe:99\n", "\n", "jill:9i9"]

for l in lines:
    name, score = l.strip().split(":")
    print(name, "->", score)
# returns jen -> 88
#         joe -> 99
#         Error

# better way

for l in lines:
    l = l.strip()
    if l == "":
        continue
    name, score = l.strip().split(":")
    print(name, "->", score)

# returns jen -> 88
#         joe -> 99
#         jill -> 9i9
lines
# returns ['jen:88\n', 'joe:99\n', '\n', 'jill:9i9\n']

for l in lines:
    for c in l:
        if c == "o":
            continue
        print(c)

# ---------------------------------------------------------

mylist = [12, 1, 33, 4]
# magic index
mylist = [1, 4, 12, 33]

for i in range(len(mylist)):
    if i == mylist[i]:
        print("aha!")
# returns nothing, runs four times

for i in range(len(mylist)):
    if i == mylist[i]:
        print("aha!")
    if i > mylist[i]:
        break

# ---------------------------------------------------------

mydict = {"key1:": 12}
mydict["asdf"]
# returns key error

mydict.get("asdf", 0)
# returns 0
mydict.get("key1", 0)
# returns 12

# ---------------------------------------------------------

import collections
# from collections import defaultdict
mydict = collections.defaultdict(int)

int()
# returns 0
str()
# returns "
list()
# returns []
dict()
# returns {}

mydict
# returns defaultdict(<class 'int'>, {})
mydict["key"]
# returns 0
mydict
# returns defaultdict(<class 'int'>, {'key': 0}) <- inserted {'key': 0}
mydict["key23"] += 1
mydict
# returns defaultdict(<class 'int'>, {'key': 0, 'key23': 1})
mydict = collections.defaultdict(list)
mydict
# returns defaultdict(<class 'list'>, {})
mydict["key23"]
# returns []
mydict
# returns defaultdict(<class 'list'>, {'key23': []})
mydict["key888"].append("9asdf")
mydict
# returns defaultdict(<class 'list'>, {'key23': [], 'key888': ['9asdf']})