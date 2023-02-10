# with open(<filename>, "r") as f:
#   code here
#   print(<result>, file=f)

# asdf asdf
#     <--- empty space with be solved with continue
# qwer
# asdf

adict = {"k1": 123}
bdict = {"k2": 99}
adict.update(bdict)
adict
# returns {'k1': 123, 'k2': 99}
bdict
# returns {'k2': 99}


s1 = {"suid": 123, "name": "joe"}
s2 = {"suid": 342, "name": "jane"}

a = print()
print(a)
# returns None

a = print
a("hi there")
# returns hi there

s1["printfunc"] = a
s1["printfunc"]("running from s1")
# returns running from s1


class User:
    name = ""
    suid = -1

    def print(self):
        print(self.name)

import nov10lecture21
s1 = nov10lecture21.User()
type(s1)
# returns <class 'nov10lecture21.User'>
s1.name
# returns ''
s1.suid
# returns -1
s1.print
# returns <bound method User.print of <nov10lecture21.User object at 0x101b29910>>
s1.print()
#
s1.name = "jen"
s1.print()


class Student(User):
    suid = -1

    def print_details(self):
        print(self.name, self.suid)

s1 = nov10lecture21.Student()
s1.name = "jen"
s1.suid = 123
s1.print_deials()
# returns jen 123
s1.print()
# returns jen
u1 = nov10lecture21.User()
u1.name = "joe"
u1.suid = 343
u1.print()
# returns joe
u1.print_details()
# returns error
