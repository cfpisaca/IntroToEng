def get_item_at(p1: list, p2: int):
    for i in range(len(p1)):
        if 0 <= p2 < len(p1):
            return p1[p2]
    return -1


def get_first_digit(p1: str):
    for i in p1:
        if i.isdigit():
            return i
    return ""


def contains_boolean(p1: list):
    for state in p1:
        if type(state) == type(True):
            return True
    else:
        return False


def shorter_list(p1: list, p2: list):
    if len(p1) < len(p2):
        return p1
    elif len(p1) == len(p2):
        return []
    else:
        return p2


def first_two_items(p1: list):
    for i in range(len(p1)):
        if len(p1) == 1:
            return p1[:]
        if len(p1) >= 2:
            return p1[0:2]
    return []


def last_n_items(p1: list, p2: int):
    end = len(p1)
    start = len(p1)-p2
    for i in range(len(p1)):
        if len(p1) >= p2:
            return p1[start:end]
    return p1[0:]


def shortest_word(p1: list):
    if p1 == []:
        return ""
    else:
        return min(p1)


