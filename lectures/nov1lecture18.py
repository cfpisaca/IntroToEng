# three flags for open we care about: r (read), w (write), a (append)

# read -> keeps what's in the file, reads the file
# write -> deletes what's in the file, writes over file
# append -> keeps what's in the file,


# f = open("/Users/carlopisacane/PycharmProjects/ecs102_1/random.text", "w") ** RUN THIS INDIVIDUALLY
# lines = f.readlines()
# f.close()


# f = open("/Users/carlopisacane/PycharmProjects/ecs102_1/random.text", "w") ** RUN THIS INDIVIDUALLY
#
# f.write("asdf\n")
#
# f.close()


# f = open("/Users/carlopisacane/PycharmProjects/ecs102_1/random.text", "a") ** RUN THIS INDIVIDUALLY
#
# print("some text", file=f) -> similar to writing to a file
#
# f.close()


# f = open("/Users/carlopisacane/PycharmProjects/ecs102_1/random.text", "r")
# type(f)
# returns <class '_io.TextIOWrapper'>


# readlines -> reads all lines
# readline -> reads lines one by one
# read -> returns whole file as string

wc = {}
f = open("/random.text", "r")
lines = f.readlines()
f.close()
lines
# returns ['some text\n', 'some text\n', 'some text\n', 'one text two text one more\n', '\n']

for l in lines:
    l = l.strip()
    words = l.split()
    for w in words:
        if w in wc.keys():
            wc[w] = wc[w] + 1
        else:
            wc[w] = 1

# returns {'some': 3, 'text': 5, 'one': 2, 'two': 1, 'more': 1}
