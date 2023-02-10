i = True
type(i) == type(True)
# have to write type for True

mystr = "asdfas"

for i in range(len(mystr)):
    print(i, " -> ", mystr[i])

# prints
# 0  ->  a
# 1  ->  s
# 2  ->  d
# 3  ->  f
# 4  ->  a
# 5  ->  s

mydict = {}
# dictionary

mydict[0] = "asdf"
mydict
# returns {0: 'asdf'}

mydict["a"] = "qwer"
# returns {0: 'asdf', "a": 'qwer'}

# *** "a" is a key, 'qwer' is value

mylist = []
mydict["asdf"] = mylist
# returns {0: 'asdf', "a": 'qwer', 'asdf': []}


mylist = [1, 2, 3]
mydict = {98: "asdf", 77: "qwer"}
mydict
# returns {98: 'asdf', 77: 'qwer'}

mydict[77]
# returns 'qwer'
mydict[77] = "p"
mydict
# returns {98: 'asdf', 77: 'p'}


mydict.keys()  # *** this is a dictionary method
# returns dict_keys([98, 77])

for k in mydict.keys():
    print(k, " -> ", mydict[k])
# returns
# 98 -> asdf
# 77 -> p

mydict.items()
# returns dict_items([(98, 'asdf'), (77, 'p')])

for k, v in mydict.items():
    print(k, "->", v)
# returns
# 98 -> asdf
# 77 -> p

names = ["john", "jane", "bill"]
scores = [88, 68, 99]

mydict = {"john": [88, 34, 67, 99]}
mydict["john"]
# returns [88, 34, 67, 99]

for k, v in mydict.items():
    print(k)
    print(v)
# returns [88, 34, 67, 99]

mydict["john"][1]
# returns 34

# *** tuple
