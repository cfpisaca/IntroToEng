def package_dicts(d1: dict, d2: dict) -> list:
    nlist = [{}, {}]
    nlist[0] = d1
    nlist[1] = d2
    return nlist


def cumulative_grade(d1: dict) -> dict:
    ndict = {}
    name = d1["name"]
    lab = 0
    midterm = d1["midterm"]
    final = d1["final"]
    count = 0
    for i in d1.keys():
        if i.startswith("lab"):
            lab = lab + d1[i]
            count = count + 1
    cumulative_grade = (0.6 * lab)/count + 0.2 * midterm + 0.2 * final
    ndict["name"] = name
    ndict["cumulative_grade"] = cumulative_grade
    return ndict


def gradebook(key_names: list, fname: str) -> list:
    with open(fname, "r") as f:
        lines = f.readlines()

    result = []
    for l in lines:
        pairs = l.strip("\n").split(" ")
        name = pairs[0]
        scores = pairs[1].split(":")
        name_scores = []
        name_scores.append(name)
        for i in scores:
            name_scores.append(i)
        result.append(dict(zip(key_names, name_scores)))
    return result


def dict_from_file3(fname: str) -> dict:
    with open(fname, "r") as f:
        lines = f.readlines()

    result = {}
    for l in lines:
        pairs = l.strip("\n").split(" ")
        name = pairs[0]
        scores = pairs[1].split(":")
        result[name] = scores
    return result
