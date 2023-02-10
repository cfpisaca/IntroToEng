# dictionary - group of key-val pairs

adict = {}
print(adict)
# returns {}

adict = {1: "a", 2: "b"}
adict[1]
# returns 'a'

adict[123]
# *** KeyError -> Review errors?

adict[3] = "three"
adict
# returns {1: 'a', 2: 'b', 3: 'three'}

adict[4] = [1, 2, 3]
adict
# returns {1: 'a', 2: 'b', 3: 'three', 4: [1, 2, 3]}

adict[5] = {123: "asdf"}
adict
# returns {1: 'a', 2: 'b', 3: 'three', 4: [1, 2, 3], 5: {123: 'asdf'}}


# example
# employee object
# suid, name, courses

employee = {"suid": 82346, "name": "jane doe", "courses": ["ecs102_1", "ecs101"]}
s2 = {"suid": 82377, "name": "jane doe", "courses": ["ecs102_1", "ecs101", "calc1"]}


mystr = "one and two and one again"
# result one: 2, and: 2, two: 1, again: 1

words = mystr.split()  # words should be a list
# *** use this syntax   ^^^   get used to doing this so you don't mix up dicts and lists
len(words)
# returns 6

result = {}

for w in words:
    if w in result.keys():
        curr_count = result[w]
        result[w] = result[w] + 1
    else:
        result[w] = 1

result
# return {'one': 2, 'and': 2, 'two': 1, 'again': 1}


# *** data files
# f = open("<file location>", "r")
# r means read from file

# type(f)
# returns <class '_io.TextIOWrapper'>

# lines = f.realines()

# type(lines)
# returns <class 'list'>

# lines
# returns ['line on\n', 'one two three\n', 'one plus one\n']

# f.close() -> closes file
# f.readlines()
# returns ERROR
