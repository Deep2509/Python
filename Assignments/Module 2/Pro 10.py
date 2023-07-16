#Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

x=int(input("Enter first number: "))
y=int(input("Enter second number: "))

if (x==y) or (x-y==5) or (x+y==5):  #we can check if the given numbers have difference or sum 5.
    print("True")
else:
    print("False")


