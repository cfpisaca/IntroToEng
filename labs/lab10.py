def sum_range(plist: list, beg: int, end: int):
    result = 0
    for i in range(len(plist)):
        if i >= beg and i < end:
            result = result + plist[i]
    return result

def every_other_item(plist: list):
    return plist[::2]


def last_half(plist: list):
    var = len(plist)//2
    return plist[var:]


def last_half_backwards(plist: list):
    var = len(plist)//2
    half = plist[var:]
    half.reverse()
    for i in half:
        plist.remove(i)
    return half


def selection_sort(plist: int):
    result = []
    while plist != []:
        for num in plist:
            if num == min(plist):
                plist.remove(num)
                result.append(num)
    return result
