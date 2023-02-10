# final -> 1 string, 2 lists, 1 dictionary

str.format("{0} some message {1}", "hi", "there")
# return 'hi some message there'

str = "hi" + " " + "some message" + " " + "there"
str
# return 'hi some message there'


mystr = "asdomeasdfasdf"
mystr[::-1]
# return 'fdsafdsaemodsa'

rstr = ""
for char in mystr:
    rstr = char + rstr
# return 'fdsafdsaemodsa'


input = "Jane Doe, John Doe"
l1 = input.split(", ")
result = []
for name in l1:
    first, last = name.split()
    result.append(last + " " + first)
# return ['Doe Jane', 'Doe John']