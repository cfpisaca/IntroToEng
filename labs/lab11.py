import string


def combo(string_param1: str, string_param2: str):
    if len(string_param1) > len(string_param2):
        return string_param1 + string_param2 + string_param1
    elif len(string_param2) > len(string_param1):
        return string_param2 + string_param1 + string_param2
    elif len(string_param1) == len(string_param2):
        return "equal"


def convert_string_to_list(string_param: str):
    string_param = string_param.replace("[", "")
    string_param = string_param.replace("]", "")
    string_param = string_param.split(", ")
    return(string_param)


def convert_string_to_list2(string_param: str):
    string_param = string_param.replace("[", "")
    string_param = string_param.replace("]", "")
    string_param = string_param.replace(" ", "")
    string_param = string_param.split(",")
    empty = []
    for i in range(len(string_param)):
        empty.append(int(string_param[i]))
    return empty


def merge_wo_dupes(p1: list, p2: list):
    p1 = p1 + p2
    new = []
    for i in range(len(p1)):
        if p1[i] not in new:
            new.append(p1[i])
    return new

# i = index # : [0, 1, 2, 3, ....]
# p1[i] = item [1, 1, 2, 2, 5, 23, 23, ....]


def intersection(p1: list, p2: list):
    new = p1 + p2
    final = []
    for i in range(len(p1)):
        if p1[i] not in new:
            new.append(p1[i])
    for i in range(len(new)):
        if new[i] in p1 and new[i] in p2 and new[i] not in final:
            final.append(new[i])
    return final


