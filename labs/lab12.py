def get_list_of_words(p1: str):
    vlist = []
    vlist = vlist + p1.split(" ")
    return vlist

def make_sentence(p1: list):
    num = 0
    nlist = ""
    while num < len(p1):
        if num == len(p1)-1:
            nlist = nlist + p1[0+num]
            return nlist
        nlist = nlist + p1[0+num] +  " "
        num += 1
    return nlist

def reverse_words(p1: str):
    nlist = get_list_of_words(p1)
    nlist.reverse()
    flist = make_sentence(nlist)
    return flist


def floor_log_base_2(p1: int):
    count = 0
    num = 2
    while num > 1:
        count = count + 1
        p1 = p1 // 2
        num = p1
    return count


def next_char(p1: str) -> str:
    if len(p1) != 1 or not p1.islower():
        return p1

    val = ord(p1) + 1
    if val > ord("z"):
        val -= 26
    return chr(val)


def next_vowel(p1: str) -> str:
    while p1 not in "aeiou":
        p1 = next_char(p1)
    return p1

