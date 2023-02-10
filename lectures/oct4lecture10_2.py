def filter_strings(p1: list, p2: str) -> list:
    result = []
    for word in p1:
        if len(p2) < len(word):
            result.append(word) # you can also use result = result + word
    return result

