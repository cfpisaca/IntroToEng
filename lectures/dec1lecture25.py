# seed emulator

l1 = [100, 3, 88, 99]
l1
# returns [100, 3, 88, 99]

for i, v in enumerate(l1):
    print(i, v)
# returns
# 0 100
# 1 3
# 2 88
# 3 99


ndict = {"k1": 33, "k2": 22, "k9": 99}

for i, t in enumerate(ndict.items()):
    print(i, t)
# returns
# 0 ('k1', 33)
# 1 ('k2', 22)
# 2 ('k9', 99)