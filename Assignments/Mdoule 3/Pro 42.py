#Write a Python program to print all unique values in a dictionary.

'''d1={1:'Deep',2:'Mitesh',3:'Deep'}

d2=set()

 for i in d1.values():
    d2.add(i)

print("Unique values are: ", d2)'''



d1={1:'Deep',2:'Mitesh',3:'Deep'}

l1=[]

for i in d1.values():

    if i not in l1:
        l1.append(i)

print("Unique values are: ",l1)
    
    
    
        
