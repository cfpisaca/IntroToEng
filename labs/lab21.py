def convert_list(scores: list) -> None:
    for i in range(len(scores)):
        scores[i] = [scores[i]]


def avg_score(score: dict) -> int:
    total = sum(score.values())
    n = len(score.values())
    return total // n


def dict_from_file2(fname: str) -> dict:
    with open(fname, "r") as f:
        lines = f.readlines()

    result = {}
    for l in lines:
        pairs = l.split(", ")
        for p in pairs:
            name, score = p.strip("()\n").split(" ")
            score = int(score)
            if name in result:
                result[name].append(score)
            else:
                result[name] = [score]
    return result


def read_two_files(fname1: str, fname2: str) -> dict:
    with open(fname1, "r") as f:
        lines = f.readlines()
    with open(fname2, "r") as g:
        lines = lines + g.readlines()

    result = {}
    for l in lines:
        pairs = l.split(", ")
        for p in pairs:
            name, score = p.strip("()\n").split(" ")
            score = int(score)
            if name in result:
                result[name].append(score)
            else:
                result[name] = [score]
    return result


def write_dict_to_file(scores: dict, fname: str) -> None:
    with open(fname, "w") as f:
        for i in scores.items():
            f.write(i[0] + ": " + ", ".join(i[1]) + "\n")