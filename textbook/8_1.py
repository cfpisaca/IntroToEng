def main():
    n = int(input("How many numbers do you have?"))
    total = 0
    for i in range(n):
        x = float(input("Enter a number >> "))
        total += x
    print("\nThe average of the numbers is", total / n)

main()

