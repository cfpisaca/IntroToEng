l1 = ["name", "lab1", "midterm"]
l2 = list(range(3))
l1
# returns ['name', 'lab1', 'midterm']
l2
# returns [0, 1, 2]

zip(l1, l2)
# returns <zip object at 0x104458780>
list(zip(l1, l2))
# returns [('name', 0), ('lab1', 1), ('midterm', 2)]
dict(zip(l1, l2))
# returns {'name': 0, 'lab1': 1, 'midterm': 2}
for k, v in zip(l1, l2):
    print("tuple : ", k, v)
# returns
# tuple: name 0
# tuple: lab1 1
# tuple: midterm 2

l1.append("final")
l1
# returns ['name', 'lab1', 'midterm', 'final']
l2
# returns [0, 1, 2]
zip(l1, l2)
# returns <zip object at 0x104282c00>
dict(zip(l1, l2))
# returns {'name': 0, 'lab1': 1, 'midterm': 2}
l2.append(3)
l2.append(4)
l2
# returns [0, 1, 2, 3, 4]
l1
# returns ['name', 'lab1', 'midterm', 'final']
dict(zip(l1, l2))
# returns {'name': 0, 'lab1': 1, 'midterm': 2, 'final': 3}
dict(zip(l1, l2, strict=True))
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: zip() takes no keyword arguments

# ----------------------------------------------------------------

gradebook = [{"name": "sue", "lab1": 88}, {"name": "sue", "lab1": 88}, {"name": "sue", "lab1": 88}]

# matrix
v1 = [1, 2]
list_v = [v1]
list_v
# returns [[1, 2]]
list_v.append([2, 1])
list_v
# returns [[1, 2], [2, 1]]
list_v[0]
# returns [1, 2]
list_v[0][0]
# returns 1
list_v[0][1]


# returns 2


class User:
    suid = -1
    name = ""


u1 = User()
type(u1)
# returns <class '__main__.User'>
u1.suid = 123
print(u1)
# returns <__main__.User object at 0x104483d30>
u2 = User()
u2.suid
# returns -1
u3 = User()
u3.suid
# returns -1

# *** dir(type)

class User:
    suid = -1
    name = ""

    def __init__(self, id, n):
        self.suid = id
        self.name = n

u1 = User(123123, "jane doe")
u1.suid
# 123123
u1.name
# 'jane doe'