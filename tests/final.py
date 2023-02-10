def two_authors_middle_initial(p1: str) -> str:
    p1 = p1.split(", ")
    fn1, fn2 = p1[0].split(" ")[0], p1[1].split(" ")[0]
    if len(p1[0].split(" ")) == 2:
        ln1 = p1[0].split(" ")[1]
    else:
        ln1 = p1[0].split(" ")[2]
    if len(p1[1].split(" ")) == 2:
        ln2 = p1[1].split(" ")[1]
    else:
        ln2 = p1[1].split(" ")[2]
    return str.format("{}, {} and {} {}", ln1, fn1, fn2, ln2)


def put_ints_in_list(p1: list) -> None:
    for i in range(len(p1)):
        if type(p1[i]) == int:
            p1[i] = [p1[i]]


def total_len_of_strs(p1: list) -> int:
    total = 0
    for i in range(len(p1)):
        if type(p1[i]) == str:
            total += len(p1[i])
    return total


def lab_scores_as_string(p1: dict) -> str:
    total = 0
    for i in p1.items():
        if i[0].startswith("lab"):
            total += int(i[1])
    return str(total)
