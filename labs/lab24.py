def string_to_dict(p1: str) -> dict:
    p1 = p1.replace("[", " ")
    p1 = p1.replace("]", " ")
    p1 = p1.replace(" ", "")
    p1 = p1.split(",")
    keys = p1[0::2]
    vals = p1[1::2]
    ndict = {}
    for i in range(len(keys)):
        ndict[keys[i]] = int(vals[i])
    return ndict


def list_of_lists_to_dict(p1: list) -> dict:
    keys = []
    vals = []
    ndict = {}
    for i in range(len(p1)):
        keys.append(p1[i][0])
    for i in range(len(p1)):
        vals.append(p1[i][1:])
    for i in range(len(keys)):
        ndict[keys[i]] = vals[i]
    return ndict


def union(d1: dict, d2: dict) -> dict:
    ndict = {}
    for k, v in d1.items():
        ndict[k] = [v]
    for k, v in d2.items():
        if k in ndict:
            ndict[k].append(v)
        elif k not in ndict:
            ndict[k] = [v]
    return ndict


def intersection(d1: dict, d2: dict) -> dict:
    ndict = {}
    for k, v in d1.items():
        if k in d2.keys():
            ndict[k] = [v]
    for k, v in d2.items():
        if k in d1.keys():
            ndict[k].append(v)
    return ndict
