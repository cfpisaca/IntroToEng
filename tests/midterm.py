def zip_code_city(p1: str):
    new1 = p1.split(", ")
    new2 = new1[1].split(" ")
    final = ""
    final = final + new2[-1] + ": " + new1[0]
    return final


def list_multiples_3(plist: list):
    elist = []
    for i in plist:
        if i % 3 == 0:
            elist.append(i)
    return elist


def multiples_of5_first(plist: list):
    llist = []
    for i in plist:
        if i % 5 != 0:
            llist.append(i)
    elist = []
    for i in plist:
        if i % 5 == 0:
            elist.append(i)
    return elist + llist


def nfl_team_abbreviation(p1: str):
    if p1.count(" ") == 1:
        p1 = p1.split(" ")
        if p1[0] + " " + p1[1] == "New York":
            return ""
        new = p1[0][0] + p1[0][1] + p1[0][2]
        return new.upper()
    elif p1.count(" ") == 2:
        p1 = p1.split(" ")
        if p1[0] + " " + p1[1] == "New York":
            return ""
        new = p1[0][0] + p1[0][1]
        return new.upper()

