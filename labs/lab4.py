def test_if_true(p1: bool) -> bool:
    if p1 == True:
        return True
    else:
        return False


def test_if_empty(p1: str) -> str:
    if p1 == "":
        return True
    else:
        return False


def return_smaller_int(p1: int, p2: int) -> int:
    if p1 < p2:
        return p1
    else:
        return p2


def return_shorter_param(p1: str, p2: str) -> str:
    if len(p1) < len(p2):
        return p1
    else:
        return p2


def either_or_true(p1: bool, p2: bool):
    if p1 == True and p2 == True:
        return False
    if p1 == True or p2 == True:
        return True


def either_or_even(p1: int, p2: int):
    if p1 % 2 == 0 and p2 % 2 == 0:
        return False
    if p1 % 2 == 0 or p2 % 2 == 0:
        return True
