#Write a Python program to add 'ing' at the end of a given string (lengthshould be at least 3). If the given string already ends with 'ing' then add'ly' instead if the string length of the given string is less than 3, leave itunchanged.

a = input('Enter a string: ')
b = a[-3:]
if(a[-3:] == 'ing'):
    b = a +'ly'
elif(len(b) <3):
    print(b)
else:
    b =a+'ing'
print(b)
