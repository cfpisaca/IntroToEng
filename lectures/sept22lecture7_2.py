mylist = [12, 3, 23, 77, 8, 3] # 1 test these in console
total = 0

for num in mylist:
    total += num
print(total)


max_seen = mylist[0] # 2

for num in mylist:
    if num > max_seen:
        max_seen = num


total = 0 # 3
for num in mylist:
    if num % 2 == 0:
        total += num


for i in range(len(mylist)): # 4 find sum of even numbers
    if mylist[i] % 2 == 0:
        total += mylist[i]


for i in range(len(mylist)): # 5 find sum of the odd items in the list
    if i % 2 == 1:
        total += mylist[i]


for i in range(1, len(mylist), 2): # same as one above, just better
    total += mylist[i]


myvar = "name:value"
split()

myvar.split(":")