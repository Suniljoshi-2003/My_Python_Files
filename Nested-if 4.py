# 4. Nested if-else statement
# if-else inside if-else statement
# multiple conditions depend on each other
# Q: positive, negative & zero. Postive  - even / odd

number = int (input("Enter a number: "))

if number > 0: # checking positive number
    if number % 2 == 0:
        print("This is a eben number")
    else:
        print("This is a odd number")
else:
    if number == 0:
        print("This is zero")
    else:
        print("This is a negative number")
