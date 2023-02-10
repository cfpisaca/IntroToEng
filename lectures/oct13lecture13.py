# worked on next_vowel from lab12

def increment(p1: int) -> int:
    return p1 + 1


def decrement(p1: int) -> int:
    return p1 - 1


def addition(p1: int, p2: int) -> int:
    while p2 > 0:
        p2 = decrement(p2)
        p1 = increment(p1)
    return p1


# p1 // 2 keep doing that while the result > 0
def floor_log_base_2(p1: int) -> int:
    result = 0
    while p1 // 2 > 0:
        p1 = p1 // 2
        result = result + 1
    return result


# don't call any variable by list, str, etc.
mylist = [1, 2, 3]
mylist.reverse()
mylist
# returns [3, 2, 1]
list.reverse(mylist)
mylist
# returns [1, 2, 3]
list = 12
list.reverse(mylist)
# returns ERROR

# string manipulation
# split()
# slice()
# replace()
# count()
# find() - finds index where ("") starts. you can also use an index to choose the start ("", 2)

# modify lists
# insert()
# append()
# remove()
# direct access []


def mt_practice(p1: list) -> list:
    result = []
    for i in p1:
        if i[0].islower():
            result.append(i)
    for i in result:
        p1.remove(i)
    return result


input = ["Asdf", "One", "one", "asdf"]
print("before func call", input)
r = mt_practice(input)
print("input is now: ", input)
print("result: ", r)


# isupper()
# islower()




