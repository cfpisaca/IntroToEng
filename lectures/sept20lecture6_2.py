def return_total_of_list(p1: list) -> int:
    total = 0
    for num in p1:
        total += num
    return total


mylist = [1, 23, 2, 4, 5]
myresult = return_total_of_list(mylist)
