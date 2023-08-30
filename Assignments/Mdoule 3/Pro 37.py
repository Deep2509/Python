#Write a Python script to print a dictionary where the keys are numbersbetween 1 and 15.
d=dict()
for x in range(1,16):  #We can use range to specify the limit 
    d[x]=x**2
print(d)
