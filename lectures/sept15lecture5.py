def xor(p1: bool, p2: bool) -> bool:
    # p1 = True p2 = True return False  self.assertFalse(True, True)
    # p1 = True p2 = False return True
    # p1 = False p2 = False return False
    # p1 = False p2 = True return True
    if p1:
        if p2 == True:
            return False
        else:
            return True
    else:
        if p2 == True:
            return True
        else:
            return False

