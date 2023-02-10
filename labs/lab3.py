def add_dashes(p1: str) -> str:
    return "-" + p1 + "-"


def reverse_order(p1: str, p2: str) -> str:
    return p2 + p1


def print2_return1(p1: str, p2: str, p3: str) -> str:
    print(p3 + p1)
    return p2


def broken_function(param1: str, param2: str, param3: str) -> str:
    v = print(param1, param2, param3)
    return v


def broken_function2(param1: str, param2: str, param3: str) -> str:
    print(param1, param2, param3)
    return param1, param2, param3


def my_version_of_min(param1: int, param2: int) -> int:
    if param1 < param2:
        return param1
    else:
        return param2


def shorter_string(param1: str, param2: str) -> str:
    if len(param1) < len(param2):
        return param1
    else:
        return param2

