# string.format()
def index_to_val(plist: list, p1: int):
    if p1 > 3:
        return ""
    else:
        return str(p1) + " -> " + str(plist[p1])


def val_to_index(plist: list, p1: type):
    if plist.count(p1) == 0:
        return ""
    else:
        for i in range(len(plist)):
            if plist[i] == p1:
                return str(i) + " -> " + str(plist[i])


def list_pretty_print(plist: list):
    empty = ""
    for i in range(len(plist)):
        if i is not len(plist)-1:
            empty = empty + str(i) + " -> " + str(plist[i]) + "\n"
        else:
            empty = empty + str(i) + " -> " + str(plist[i])
    return empty


def list_to_dict(plist: list):
    pdict = {}
    for i in range(len(plist)):
        pdict[i] = plist[i]
    return pdict


def two_lists_to_dict(p1: list, p2: list):
    fdict = {}
    if len(p1) != len(p2):
        return fdict
    if len(p1) == len(p2):
        for i in range(len(p1)):
           fdict[p1[i]] = p2[i]
    return fdict












