# two kinds of loops, item loop and an index loop
# item loop: for loopvar in list/string

def contain_bool(p1: list) -> bool:
    # if p1 has a boolean, return True
    # else return False
    for item in p1:
        if type(item) == type(True):
            return True
    return False

# access item/char from a list/string using an index
mylist = [1, 2, 4, 3]
mylist[0]
mystr = "hello"
mystr[3]


mystr = "one and two and three and four"
# searching for a substring in a string
mystr.count("and")
# return = 2
mystr.count("andy")
# return = 0
mystr.count("", 0, 4)
# return = 1

mystr.find(" ")
# return = 3



mylist = [12, 2, 34, 22, 48]
mylist.sort()
mylist
# return = [2, 12, 22, 34, 48]

# ascending sort
mylist = [12, 2, 34, 22, 48]
mylist.sort(reverse=True)
mylist
# return = [48, 34, 22, 12, 2]

# descending sort
"apple" < "banana"
# returns = True

mylist = ["boy", "cow", "doo"]
mylist.sort()
mylist
# return = ['boy', 'cow', 'doo']

