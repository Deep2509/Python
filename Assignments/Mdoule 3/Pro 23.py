# Write a Python program to find the length of a tuple.

tuple1=('H','E','L','L','O','D','E','E','P')
'''print(type(tuple1))
print(len(tuple1)) ''' # Here i have used built in len function to find out length of the tuple

count=0
for i in tuple1:
    if i in tuple1:
        count+=1
print("Length of tuple is ",count) #Have used for loop to find out length
    
