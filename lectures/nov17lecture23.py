def f1() -> str:
    return "world"


def f2(p1: str) -> str:
    return p1 + f1()


def f3(p1: str) -> str:
    return f2(p1) + "!"

# from nov17lecture23 import *
# f3("asdf")
# # 'asdfworld!'
# f3("hello ")
# # 'hello world!'

a = "hello"
b = f3(a)  # debug here
print(b)

# def f1() -> None:  # debug here
#     f1()
#
# f1()

# -----------------------------------------------------

# factorial of n = n * (n-1) * (n-2) ... * 2

def factorial1(n: int) -> int:
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result


def factorial2(n: int) -> int:
    if n <= 1:
        return 1
    result = 1
    loop_var = 1
    while loop_var < n:
        result = result * loop_var
        loop_var = loop_var + 1
    return result

def factorial4(n: int) -> int:
    if n < 1:
        return 1
    if n == 1:
        return 1
    return n * factorial4(n-1)


def factorial3(n: int, p1: list) -> int:
    p1.append(n)
    if n < 1:
        return 1
    if n == 1:
        return 1
    return n * factorial3(n-1, p1)

mylist = []
a = factorial3(6, mylist)
print(mylist)


def f1():
    print("in f1")
    def f2():
        print("in f2")
    print("back in f1")
    f2()

# -----------------------------------------------------

mylist = [2, 5, 7, 34, 99, 120]

def find(n: int, p1: list)-> bool:
    for item in p1:
        if item == n:
            return True
        return False

