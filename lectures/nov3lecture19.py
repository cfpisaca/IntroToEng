# reviewed lab 18

adict = {}
adict["key"] = 12
adict
# returns {'key': 12}
adict["key"] = 1299
adict
# returns {'key': 1299}

adict["key"] = [12]
adict
# returns {'key': [12]}
adict["key"].append(1299)
adict
# returns {'key': [12, 1299]}
mylist = adict["key"]
mylist.append(1299)

result = {}
result["some"] = 2
result["and"] = 2
result["text"] = 1
result["here"] =1
result
# returns {'some': 2, 'and': 2, 'text': 1, 'here': 1}


count_to_words = {}
for k, v in result.items():
    if v not in count_to_words.keys():
        count_to_words[v] = [k]
    else:
        mylist = count_to_words[v]
        mylist.append(k)

count_to_words
# returns {2: ['some', 'and'], 1: ['text', 'here']}