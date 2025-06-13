#Task2) Write a Python program that asks the user to enter a number and prints whether it is positive, negative, or zero.

number=int(input("Enter any number to see if it is positive, negative or zero: "))

if number < 0:
    print(f"negative")
elif number == 0:
    print(f"zero")
elif number > 0:
    print(f"positive")

