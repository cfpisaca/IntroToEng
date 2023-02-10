def is_vowel(param: str) -> bool:
    if (len(param) == 1):
        if param in "aeiou":
            return True
    return False


def filter_vowels(p1: str) -> str:
    vowels = ""
    for i in range(len(p1)):
        if is_vowel(p1[i]):
            vowels += p1[i]
    return vowels


def contains(plist: list, p2: str) -> bool:
    for i in range(len(plist)):
        if p2 == plist[i]:
            return True

    return False


def index_of(plist: list, p2: str):
    for i in range(len(plist)):
        if p2 == plist[i]:
            return i

    return -1


def get_login(first_name: str, last_name: str):
    return first_name[0] + last_name[0:5]


def get_padded_login(first_name: str, last_name: str):
    login = ""
    if len(get_login(first_name, last_name)) < 6:
        login = login + get_login(first_name, last_name)
        if len(login) == 5:
            login = login + "0"
            return login
        elif len(login) == 4:
            login = login + "00"
            return login
        elif len(login) == 3:
            login = login + "000"
            return login
        elif len(login) == 2:
            login = login + "0000"
            return login
    return get_login(first_name, last_name)


def extract_name(p1: str):
    for i in range(len(p1)):
        if p1[i] == ":":
            list = p1.split(":")
            return list[1]
    return ""



def extract_full_name(p1: str):
    list1 = p1.split(",")
    if list1[0].startswith("f"):
        first = list1[0].split(":")
        last = list1[1].split(":")
        return first[1] + " " + last[1]
    if list1[0].startswith("l"):
        first = list1[0].split(":")
        last = list1[1].split(":")
        return last[1] + " " + first[1]

