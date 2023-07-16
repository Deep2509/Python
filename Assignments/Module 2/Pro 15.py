#Write a Python program to count occurrences of a substring in a string.

str1=input("Enter String: ")
substr=input("Enter Substring: ")

count=0

for i in str1:

    
    if(str1==substr):
        count+=1
print("Number of substring is: ",count)
    
