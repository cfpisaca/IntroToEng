# read file
# first line is header:
# name, lab1, lab2, lab3, midterm, lab4, lab5, final
# rest of lines are data:
# jen, 88, 81, 82, 90, 80, 84, 90
# joe, 88, 81, 82, 90, 80, 84, 90
# return list of dicts
def gradebook1(fname: str) -> list:
    with open(fname, "r") as f:
        lines = f.readlines()

    header = lines[0]
    keys = header.strip().split(", ")
    data = lines[1:]
    result = []
    for line in data:
        vals = line.strip().split(", ")
        curr = dict(zip(keys, vals))
        result.append(curr)
    return result

    # result = []
    # nline = 0
    # headers = []
    # for l in lines:
    #     name_scores = []
    #     if nline == 0:
    #         nline = nline + 1
    #         headers = l.strip().split(", ")
    #     elif nline == 1:
    #         pairs = l.strip().split(", ")
    #         name = pairs[0]
    #         scores = pairs[1:]
    #         name_scores.append(name)
    #         for i in scores:
    #             name_scores.append(i)
    #         tdict = dict(zip(headers, name_scores))
    #         result.append(tdict)
    # return result




# return dict of lists
# {"name": ["jen", "joe"], lab1:[]...}
def gradebook2(fname: str) -> dict:
    with open(fname, "r") as f:
        lines = f.readlines()

    result = {}
    keys = lines[0].strip().split(", ")
    for k in keys:
        result[k] = []
    values = lines[1:]
    for v in values:
        vals = v.strip().split(", ")
        for i in range(len(keys)):
            k = keys[i]
            v = vals[i]
            result[k].append(v)
    return result


    # nline = 0
    # headers = []
    # fitems = []
    # for l in lines:
    #     if nline == 0:
    #         nline = nline + 1
    #         headers = l.strip("\n").split(", ")
    #     elif nline == 1:
    #         nline = nline + 1
    #         pairs = l.strip("\n").split(", ")
    #         for i in pairs:
    #             fitems.append([i])
    #     elif nline == 2:
    #         pairs = l.strip("\n").split(", ")
    #         for i in range(len(pairs)):
    #             fitems[i].append(pairs[i])
    # result = dict(zip(headers, fitems))
    # return result
