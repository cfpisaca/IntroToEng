def f1(p1: int) -> bool:
    if p1 % 2 == 0:
        return True
    # implicit return - returns type 'None'
    # return
    return False


mylist = [1, 2, 3, 4]


def f2(p1: list) -> None:
    p1.remove(p1[0])
    # p1 = p1 + 1


def max(p1: list) -> int:
    max = p1[0]
    for num in p1:
        if num > max:
            max = num
        return max


def longest_string(p1: list) -> str:
    max = p1[0]
    for word in p1:
        if len(word) > len(max):
            max = word
    return max


def acronym(p1: str) -> str:
    # p1 = "some set of words"
    # return "ssow"
    words = p1.split(" ")
    result = ""
    for w in words:
        result = result + w[0] + "."
    return result

mystr = "some set of words"
mystr.replace(" ", "", 2)
# returns "somesetof words"


mystr = "asedf"
mystr.count("")
# returns 6 so == to len(mystr) + 1

mylist = [1, 2, 3, 4]
for num in mylist:
    mylist.append(num)
# infinite loop

mylist = [1, 2, 3, 45]
myvar = mylist
myvar.insert(0, 12)
# returns [12, 1, 2, 3, 45]
