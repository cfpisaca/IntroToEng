# mostly review prior to this

mystr = "hello"  # once you make a string you can't change it
mystr[3]  # statement doesn't work

mystr.replace("e", "E")  # doesn't change string
mystr = mystr.replace("e", "E")  # changes physical string


# ~for lab

mystr = "a"
mystr = "e"
mystr = "ae"  # if in same order as "aeiou"
# "ea" will return false

mystr in "aeiou"
# returns True

mylist = ["asdf", "qwer", "asd", "asdfff"]

"asdf" in mylist
# returns True

"asd" in mylist
# returns True

"sdf" in mylist
# returns False

"sdf" not in mylist
# returns True

# equivalent of != & ==


# ~while loops

# definite loop vs indefinite loop

mylist = ["asdf", "qwer", "asd", "asdfff"]
index = 0

while index < len(mylist):
    print(mylist[index])
    index += 1  # prevents an infinite loop by updating the variable

# control c to stop infinite loop

