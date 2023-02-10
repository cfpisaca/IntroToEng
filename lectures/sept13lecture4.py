def one_or_the_other_is_true(p1: bool, p2: bool) -> bool:
    # 4 cases: p1 = True, p2 = True
    # p1 = True, p2 = False
    # p1 = False, p2 = True
    # p1 = False, p2 = False
    result = False
    if p1 == True:
        # do some work
        if p2 == True:
            result = False
        else:
            result = True
    else:
        # do some other work
        if p2 == True:
            result = True
        else:
            result = False

    return result



