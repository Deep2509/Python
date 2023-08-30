#Write a Python program to check multiple keys exists in a dictionary

d1={1:"Tops", 2:"Technologies", 3:"Maninagar", 2:"CG Road"}
v1=[]
for i in d1.keys():
    print(d1[i])
print(v1)


'''d1 = {1: "Tops", 2: "Technologies", 3: "Maninagar", 2: "CG Road"}  
keys_to_check = [2,3,5]  

for key in keys_to_check:
    if key in d1:
        print(f"Key {key} exists in the dictionary.")
    else:
        print(f"Key {key} does not exist in the dictionary.")'''
