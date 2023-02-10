s2 = ["77", "88"]

for i in range(len(s2)):
    curr = s2[i]
    s2[i] = int(curr)


keys = ["a", 1, 23, 43, 54]
vals = [32, 34, 54]
dict(zip(keys, vals))

d1 = {}
for i in range(len(keys)):
    if i < len(vals):
        k = keys[i]
        v = vals[i]
        d1[k] = v
    else:
        k = keys[i]
        d1[k] = None