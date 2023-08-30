#Write a Python program to find the highest 3 values in a dictionary

d1={'1':'220','2':'410','3':'200','4':'230','5':'502'}
values = list(map(int, d1.values()))
values.sort()
print(values)
print(values[-1:-4:-1])


 
