def f1(p1: str) -> str:
    return "hi" + p1


def f2(p1: int, p2: int) -> bool:
    v = p1 > 0
    u = p2 > 0
    w = v and u
    return w


def f3(p1: int) -> bool:
    if p1 % 2 == 0:
        print("p1 is even!")
    result = p1 % 2 == 0
    return result