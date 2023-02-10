def right_justify(p1: str) -> str:
    if len(p1) > 3:
        return "---"
    elif len(p1) == 3:
        return p1
    elif len(p1) == 2:
        return " " + p1
    elif len(p1) == 1:
        return "  " + p1
    else:
        return "   "


def sum_up_to(p1: int) -> int:
    result = 0
    for i in range(p1):
        result = result + i
    return result


def sum_beg_end(p1: int, p2: int) -> int:
    result = 0
    if p1 > p2:
        return 0
    if p1 <= p2:
        for i in range(p1, p2):
            result = result + i
        return result


def is_vowel(p1: str) -> bool:
    if len(p1) > 1:
        return False
    if len(p1) == 1:
        if p1 == "a":
            return True
        elif p1 == "e":
            return True
        elif p1 == "i":
            return True
        elif p1 == "o":
            return True
        elif p1 == "u":
            return True
        else:
            return False


def prepend_if_even(p1: int, p2: str):
    if p1 % 2 != 0:
        return p2
    else:
        return "even" + p2


def fizzbuzz(p1: int):
    if p1 % 3 == 0 and p1 % 5 == 0:
        return "fizzbuzz"
    if p1 % 5 == 0:
        return "buzz"
    if p1 % 3 == 0:
        return "fizz"
    else:
        return ""


