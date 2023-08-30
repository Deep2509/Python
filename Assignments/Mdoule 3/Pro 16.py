#Write a Python program to check whether a list contains a sublist.

l1=[1,56,'Deep','Hello',54]
l2=[54]

for i in l2:
    if i in l1:            #We are checking if any element of l1 exists in l2 then we will print true or else False.
        print("True")
    else:
        print("False")
        



