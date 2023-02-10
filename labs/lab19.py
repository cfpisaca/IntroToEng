def string_to_dict(p1: str) -> dict:
    result = {}
    p1 = p1.split(" | ")
    names = p1[0].split(", ")
    scores = p1[1].split(", ")
    for i in range(len(names)):
        result[names[i]] = scores[i]
    return result


def write_list_to_file(plist: list, fname: str) -> None:
    with open(fname, "w") as f:
        for i in plist:
            f.write(i + "\n")


def max_and_min(fname: str) -> dict:
    with open(fname, "r") as f:
        lines = f.readlines()

    scores = []
    for line in lines:
        scores.append(line.strip().split(": ")[1])
    rmax = max(scores)
    rmin = min(scores)
    result = {"max": int(rmax), "min": int(rmin)}
    return result


def names_to_scores(fname: str) -> dict:
    with open(fname, "r") as f:
        lines = f.readlines()

    result = {}
    for line in lines:
        name, score = line.strip().split(": ")
        if name in result:
            result[name].append(score)
        else:
            result[name] = [score]
    return result


def scores_to_names(fname: str) -> dict:
    with open(fname, "r") as f:
        lines = f.readlines()

    result = {}
    for line in lines:
        name, score = line.strip().split(": ")
        if score in result:
            result[score].append(name)
        else:
            result[score] = [name]
    return result


