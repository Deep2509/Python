#Write a Python program to find the repeated items of a tuple.

t1=(25,65,12,25,89,78)
for i in t1:
    if t1.count(i)>1: #here we can find repeated item using count method and using for loop
        print(i)
