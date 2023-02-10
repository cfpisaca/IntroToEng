# indexing into a string and slices

# p1 = "abcde" -> "c"
# p1 = "easy" -> "s"
def third_char(p1: str) -> str:
    if len(p1) > 2:
        return p1[2]
    else:
        return ""

# p1 = "abcde", n = 0 -> ""
# p1 = "abcde", n = 1 -> "a"
# p1 = "abcde", n = 5 -> "e"
# p1 = "abcde", n = 6 -> ""
def nth_char(p1: str, n: int) -> str:
    if n == 0 or n >= len(p1) + 1:
        return ""
    else:
        return p1[n-1]

# p1 = "abcde", n = 0 -> ""
# p1 = "abcde", n = 1 -> "ab"
# p1 = "abcde", n = 4 -> "de"
# p1 = "abcde", n = 5 -> "e"
# p1 = "abcde", n = 6 -> ""
def two_chars_at_index_n(p1: str, n: int) -> str:
    return p1[n-1:n+1]

def m_chars_at_index_n(p1: str, m: int, n: int) -> str:
    return p1[n-1:m]

def first_n_chars(p1:str, n: int) -> str:
    return p1[:n]

def last_n_chars(p1: str, n: int) -> str:
    return p1[-n:]

# p1 = ["one", "and", "two", "three] -> "oatt"
def first_letter_of_each_string(p1: list) -> str:
    result = ""
    for item in p1:
        result = result + item[0]
    return result

# p1 = ["one", "and", "two", "three] -> "nnwr"
def second_letter_of_each_string(p1: list) -> str:
    result = ""
    for item in p1:
        result = result + item[1]
    return result

# 1st letter of 1st word, 2nd letter of 2nd word, and so on
# p1 = ["one", "and", "two", "three] -> "onwh"
def complicated(p1: list) -> str:
    result = ""
    for item in range(len(p1)):
        result = result + p1[item][item]
    return result


# split method

# p1 = "one two three" -> "two"
def second_word(p1: str) -> str:
    p1 = p1.split(" ")
    return p1[1]

# p1 = "one two three", n = 0 -> ""
# p1 = "one two three", n = 1 -> "one"
# p1 = "one two three", n = 3 -> "three"
# p1 = "one two three", n = 4 -> ""
def nth_word(p1: str, n: int) -> str:
    p1 = p1.split(" ")
    if n == 0 or n >= len(p1)+1:
        return ""
    return p1[n-1]

# split, modify list and then join
# p1 = "one two three" -> "one three"
def remove_second_word(p1: str) -> str:
    p1 = p1.split(" ")
    p1.remove(p1[1])
    p1 = " ".join(p1)
    return p1

# p1 = "one two three", n = 0 -> ""
# p1 = "one two three", n = 1 -> "two three"
# p1 = "one two three", n = 2 -> "one three"
# p1 = "one two three", n = 3 -> "one two"
# p1 = "one two three", n = 4 -> ""
def remove_nth_word(p1:str, n: int) -> str:
    p1 = p1.split(" ")
    if n == 0 or n >= len(p1)+1:
        return ""
    p1.remove(p1[n-1])
    p1 = " ".join(p1)
    return p1

# multiple splits
# p1 = "one:1 two:23 three:34" -> "23"
def second_half_of_second_word(p1: str) -> str:
    p1 = p1.split(" ")
    result = p1[1].split(":")
    return result[1]

# p1 = "one:1 two:23 three:34", n = 0 -> ""
# p1 = "one:1 two:23 three:34", n = 1-> "1"
# p1 = "one:1 two:23 three:34", n = 2-> "23"
# p1 = "one:1 two:23 three:34", n = 3 -> "34"
# p1 = "one:1 two:23 three:34" n = 4 -> ""
def second_half_of_nth_word(p1: str, n: int) -> str:
    p1 = p1.split(" ")
    if n == 0 or n >= len(p1)+1:
        return ""
    result = p1[n-1].split(":")
    return result[1]

# p1 is a multiple line string
# p1 = "soem words\nmore words\nlast line" -> "some more last"
def first_word_from_each_line(p1: str) -> str:
    result = ""
    p1 = p1.split("\n")
    for item in p1:
        result = result + item.split(" ")[0] + " "
    result = result.strip(" ")
    return result


# 1st word from 1st line, 2nd word from 2nd line and so on
# p1 = "soem words here\nmore words there\nlast line ends" -> "some words ends"
def complicated_word_line(p1: str) -> str:
    result = ""
    p1 = p1.split("\n")
    for item in range(len(p1)):
        result = result + p1[item].split(" ")[item] + " "
    result = result.strip(" ")
    return result

# split and join
# p1 = "one and two and three four" -> "one-and-two"
def first_half_joined_with_dashes(p1: str) -> str:
    p1 = p1.split(" ")
    return "-".join(p1[:3])


# p1 = "one and two or three four maybe five", p2="and" -> "one two or three four maybe five"
def filter_out_word(p1: str, p2: str) -> str:
    p1 = p1.split(" ")
    for i in p1:
        if i.startswith(p2):
            p1.remove(i)
    return " ".join(p1)

# p1 = "one and two or three four maybe five", p2=["and", "or", "maybe"] -> "one two three four five"
def filter_out_all_words_in_p2(p1: str, p2: list) -> str:
    p1 = p1.split(" ")
    for w in p2:
        for i in p1:
            if i.startswith(w):
                p1.remove(i)
    return " ".join(p1)

# p1 = "one and two or three four maybe five", p2="and or maybe" -> "one two three four five"
def filter_out_all_words_in_p2_str(p1: str, p2: str) -> str:
    p1 = p1.split(" ")
    p2 = p2.split(" ")
    for w in p2:
        for i in p1:
            if i.startswith(w):
                p1.remove(i)
    return " ".join(p1)
