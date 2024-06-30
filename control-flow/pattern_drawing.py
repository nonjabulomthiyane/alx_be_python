size = int(input("Enter the size of the pattern: "))
if size <= 0:
    print("Please enter a positive integer.")
    exit()
row = 0
while row < size:
    column = 0
    while column < size:
        print("*", end="")
        column += 1
    print()  
    row += 1
