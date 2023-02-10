mystr = "one and two and three" # review for lab9
# print(mystr.count("and))

def f1(p1: str, p2: str):
    return p1.count(p2)

print("func execution from script\n", f1(mystr, "and"))
