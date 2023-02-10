# p1 [1, 2, 3]
# after function runs
# p1 = [1, 4, 9]

def squares(p1: list) -> None:
    for i in range(len(p1)):
        curr_num = p1[i]
        square_val = curr_num * curr_num
        p1[i] = square_val

mylist = [1, 2, 3]
print(mylist)
squares(mylist)
print(mylist)
