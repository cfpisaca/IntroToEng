# p1 is a string of 4 words
# return the words in this order: 2, 1, 4, 3
def reorder_words(p1: str):
    p1 = p1.split(" ")
    return str.format("{} {} {} {}", p1[1], p1[0], p1[3], p1[2])

# p1 is a string of words
# return the first initial from each word in p1 concatenated together
def acronym(p1: str):
    p1 = p1.split(" ")
    return str.format("{}{}{}", p1[0][0].upper(), p1[1][0].upper(), p1[2][0].upper())

# p1 is a string
# return the first 3 chars of p1, capitalized
def first_three_chars(p1: str):
    return str.format("{}", p1[:3].upper())


# p1 has two or three words
# if p1 has 2 words, return the first 3 chars of the first word
# if p1 has 3 words, return the first 3 letters of each word concatenated together
def two_cases(p1: str):
    if len(p1.split(" ")) == 2:
        return str.format("{}", p1[:3].upper())
    if len(p1.split(" ")) == 3:
        p1 = p1.split(" ")
        return str.format("{}{}{}", p1[0][0].upper(), p1[1][0].upper(), p1[2][0].upper())