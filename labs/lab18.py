def two_lists_to_dict(p1: list, p2: list) -> dict:
    ndict = {}
    if len(p1) <= len(p2):
        for i in range(len(p1)):  # use index to reference items in two different lists
            ndict[p1[i]] = p2[i]  # <dictionary>[<key>] = <value> -> Ex: ndict[p1[i]] = p2[i]
    if len(p1) > len(p2):
        for i in range(len(p1)):
            if i < len(p2):
                ndict[p1[i]] = p2[i]
            else:
                ndict[p1[i]] = None
    return ndict


def dict_from_file(fname: str) -> dict:
    f = open(fname, "r")
    lines = f.readlines()
    f.close()
    ndict = {}
    l = lines[0].strip()
    a = l.split(", ")
    l = lines[1].strip()
    b = l.split(", ")
    for i in range(len(a)):
        ndict[a[i]] = b[i]
    return ndict
    # with open(fname, "r") as f:
    #     lines = f.readlines()
    # print(lines)
    # keys = lines[0].strip().split(", ")
    # vals = lines[0].strip().split(", ")
    # return two_lists_to_dict(keys, vals)
    # result = {} *** this is replaced by the previous function we created -> two_lists_to_dict()
    # for i in range(len(keys)):
    #   key = keys[i]
    #   val = vals[i]
    #   result[key] = val
    # return reult


def list_word_count(p1: list, result: dict) -> None:
    for i in p1:
        if i in result.keys():
            result[i] = result[i] + 1
        else:
            result[i] = 1


def file_total_words(fname: str, result: dict) -> None:  # UP TO HERE
    f = open(fname, "r")
    lines = f.readlines()
    f.close()
    # with open(fname, "r") as f:
    #   lines = f.readlines()
    words = lines[0].strip()
    l = words.split(" ")
    result["numWords"] = len(l)


def file_distinct_words(fname: str, result: dict) -> None:
    f = open(fname)
    lines = f.readlines()
    f.close()
    for l in lines:
        l = l.strip()
        words = l.split()
        for w in words:
            if w in result.keys():
                result[w] = result[w] + 1
            else:
                result[w] = 1