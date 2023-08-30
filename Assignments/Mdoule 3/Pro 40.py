#Write a Python program to map two lists into a dictionary 


keys = ['name', 'age', 'job']
values = ['John', 25, 'Developer']

myDict = {k: v for k, v in zip(keys, values)}
print("Dictionary Items  :  ",  myDict)
