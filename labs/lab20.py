def populate_dict(keyNames: list, fname: str) -> dict:
    result = {}
    with open(fname, "r") as f:
        lines = f.readlines()
    for line in lines:
        item = line.strip().split(", ")
        for i in range(len(keyNames)):
            result[keyNames[i]] = item[i]
    return result


def dict_from_file(fname: str) -> dict:
    result = {}
    with open(fname, "r") as f:
        line = f.readline().strip().split(", ")
        for i in range(len(line)):
            line[i] = line[i].strip("(").strip(")").split(" ")
        for k, i in line:
            result[k] = int(i)
    return result


def write_dict_to_file(score: dict, fname: str) -> None:
    with open(fname, "w") as f:
        for i in score.keys():
            f.write(i + ": " + str(score[i]) + "\n")


def num_failing_scores(gradebook: dict) -> int:
    count = 0
    for i in gradebook.keys():
        if gradebook[i] < 50:
            count = count + 1
    return count

