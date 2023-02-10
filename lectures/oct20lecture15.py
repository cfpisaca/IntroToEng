def f0(p1: str, p2: str) -> str:
    tokens = p1.split(", ")  # ["lab1: 89", "lab2: 88" ]
    for t in tokens:
        if t.startswith(p2):
            l1 = t.split(": ")
            return l1[1]


mylist = ["asdf", "qwer"]
" ".join(mylist)


# returns 'asdf', 'qwer'


def f1(plist: list) -> str:
    result = ""
    for item in plist:
        result = result + " " + str(item)
    return result.strip()


def f2(plist: list) -> str:
    plist[0] = str(plist[0])
    plist[-1] = str(plist[-1])


def f3(plist: list) -> list:
    words = []
    for s in plist:
        if s.count(" ") == 0:
            words.append(s)
    return words


def f4(plist: list, p2: int) -> str:
    words = ""
    for i in plist:
        if i.coint(" ") + 1 == p2:
            words = i
    return words


# same as previous
def f5(plist: list, p2: int) -> str:
    result = ""
    for item in plist:
        l1 = item.split(" ")
        if len(l1) == p2:
            result = item
    return result


# ["oneword", "runonsentence", "one two three", "a b c d e"]
def f6(plist: list) -> list:
    words = []
    for item in plist:
        if item.count(" ") == 0:
            words.append(item)
            # plist.remove(item) will change the len of plist
    # at this point, words has all words in plist
    for w in words:
        plist.remove(w)
    # at this point plist has only sentences
    return words + plist


def f7(p1: str) -> str:
    words = p1.split(" ")
    result = ""
    for w in words:
        result = result + w[0]
    return result


def f8(p1: str) -> str:
    words = p1.split("")
    return words[0][0] + words[1][0]


def f9(p1: str) -> str:
    words = p1.split(" ")
    result = ""
    for w in words:
        result = result + w[0]
    return result.upper()


"ny".upper()
# returns 'NY'
"ny".capitalize()
# returns 'Ny'

