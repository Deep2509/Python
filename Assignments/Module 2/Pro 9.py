#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

x=int(input("Enter first num. ="))
y=int(input("Enter second num. ="))
z=int(input("Enter third num. ="))

if x==y or y==z or z==x:  #if any two number matches then we can simply print the 0 in our output.
    print(0)
    
else:
    print("Addition would be:",x+y+z)
    

