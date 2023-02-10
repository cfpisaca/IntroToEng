def convert_str_and_merge(p1: str, p2: str):
    p1 = p1.replace(" ", "")
    p2 = p2.replace(" ", "")
    p1 = p1.replace("'", "")
    p2 = p2.replace("'", "")
    p3 = p1 + "," + p2
    p3 = p3.split(",")
    e = []
    for i in p3:
        e.append(int(i))
    return e


def filter_even_numbers(p1: list):
    even = []
    for i in p1:
        if i % 2 == 0:
            even.append(i)
    return even


def word_counts(p1: list):
    empty = []
    for i in p1:
        e = 0
        e = e + i.count(" ")
        e = e + 1
        empty.append(e)
    return empty


def more_consonants_than_vowels(p1: str):
    vowel = 0
    con = 0
    for i in p1:
        if i in "aeiou":
            vowel = vowel + 1
        else:
            con = con + 1
    return con > vowel



def insert_duplicate(p1: list, p2: int):
    for i in range(len(p1)):
        if p1[i] == p2:
            p1.insert(i, p1[i])
            return



