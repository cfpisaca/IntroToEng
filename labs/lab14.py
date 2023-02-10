def remove_all_even_numbers(plist: list):
    empty = []
    for i in range(len(plist)):
        if plist[i] % 2 != 0:
            empty.append(plist[i])
    plist.clear()
    for i in range(len(empty)):
         plist.append(empty[i])
    return


def num_vowels_gt(p1: str, p2: int):
    empty = ""
    for i in p1:
        if i in "aeiou":
            empty = empty + i
    if len(empty) > p2:
        return True
    else:
        return False


def most_words(plist: list):
    current = []
    count = plist[0].count(" ")
    current.append(plist[0])
    for i in range(1, len(plist)):
        if plist[i].count(" ") > count:
            current.clear()
            current.append(plist[i])
    current = str(current)
    current = current.replace("[", "")
    current = current.replace("]", "")
    current = current.replace("'", "")
    return current


def vowels_consonants(p1: str):
    vowel = ""
    con = ""
    for i in p1:
        if i in "aeiou":
            vowel = vowel + i
        else:
            con = con + i
    return vowel + con


def university_name_to_email(p1: str):
    if p1.count(" ") >= 2:
        abbrev = p1.split(" ")
        result = ""
        for i in abbrev:
            result = result + i[0]
        return result + ".edu"
    if p1.count(" ") <= 1:
        first = p1.split(" ")
    return first[0] + ".edu"
    # carnegie melon university -> cmu.edu
    # syracuse university -> syracuse.edu
    # massachussets institute technology -> mit.edu
    # tufts university -> tufts.edu
