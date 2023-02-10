def square_of_numbers(nums: list):
    sqr = []
    for i in nums:
        v = i * i
        sqr.append(v)
    return sqr


def is_leap_year(p1: int):
    if p1 % 100 == 0:
        if p1 % 400 == 0:
            return True
        else:
            return False
    else:
        if p1 % 4 == 0:
            return True
        else:
            return False


def greatest_common_divisor(n: int, m: int):
    numList = [n, m]
    v = 1
    while v > 0:
        v = numList[0] % numList[1]
        numList.remove(numList[0])
        numList.append(v)
    return numList[0]






