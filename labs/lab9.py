def filter_strings(plist: list, pstr: str):
    vlist = []
    for i in range(len(plist)):
        if plist[i].startswith(pstr):
            vlist.append(plist[i])
    return vlist


def average_list(plist: list):
    total = 0
    count = 0
    for i in range(len(plist)):
        total += plist[i]
        count += 1
    if total == 0:
        return 0
    return total / count


def first_name_first(p1: str):
    names = p1.split(", ")
    return names[1] + " " + names[0]


def last_name_first(p1: str):
    if p1.count(" ") == 1:
        name1 = p1.split(" ")
        return name1[1] + ", " + name1[0]
    if p1.count(" ") == 2:
        if p1.count(".") == 1:
            name2 = p1.split(" ")
            return name2[2] + ", " + name2[0] + " " + name2[1]
        if p1.count(".") == 0:
            name3 = p1.split(" ")
            return name3[2] + ", " + name3[0] + " " + name3[1]


def find_min(plist: list):
    plist.sort()
    return plist[0]


def two_smallest_ints(plist: list):
    plist.sort()
    total = []
    total.append(plist[0])
    total.append(plist[1])
    return total

