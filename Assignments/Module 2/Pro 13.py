#Write a Python program to count the number of characters (character frequency) in a string

count=0

str1=input("Enter your str: ")

char=input("Your character: ")

for i in str1:
    print(i)

    if (i==char):
        count+=1
print("Count is:",count)
