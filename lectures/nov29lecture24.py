# Final content: strings, lists, dictionary

# constructor functions:
# bool, int, str, list, dict


# len -> used for str/list (useful for str)


# uses for max, min, sum
# max, min, sum value of list


# isinstance(<variable>, <type>)
# instead of
# type(<variable>) == type(<type>)
# Ex:
# a = "asdf"
# type(a) == type("")
# True
# type(a) == type(1)
# False
# isinstance(a, dict)
# False
# isinstance(a, str)
# True

# -------------------------------------------------

# there can not be more keys than values
# there can be more values than keys

l1 = [1, 2, 34]
l2 = [23, 33, 44, 55, 66]
dict(zip(l2, l1))
# return {23: 1, 33: 2, 44: 34}

i = 0
while i < (len(l2)-len(l1)):
    l1.append(None)

l2
# return [23, 33, 44, 55, 66]
l1
# return [1, 2, 34, None, None]
dict(zip(l2, l1))
# return {23: 1, 33: 2, 44: 34, 55: None, 66: None}



