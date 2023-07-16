 #Write a Python program to check if a number is positive, negative or zero.

num=int(input("Enter any number: "))


if num > 0:                         #With the help of if...elif condition we can get it checked.
    print("Positive number")
elif num == 0:
    print("Number is zero")
else:
    print("Negative number")
