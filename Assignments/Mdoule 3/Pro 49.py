#Write a Python function to check whether a number is in a given range

def range_test(n):
    if n in range(1,9):   #HEre we have used range function to check if our number is in range or not
        print("This number is in the range")
    else:
        print("This number is not in the range")

n1=int(input("ENter the number: "))
range_test(n1)
