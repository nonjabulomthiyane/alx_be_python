number = int(input("Enter a number to see its multiplication table: "))
for i in range(1, 11):  # iterate from 1 to 10
    result = number * i
    print(f"{number} * {i} = {result}")
