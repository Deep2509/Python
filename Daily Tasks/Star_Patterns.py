'''for i in range(5):
    for j in range(5):
        print("*", end="")
    print()


#First Task

for i in range(4):
    for j in range(i+1):
        print("1", end="")
    print()
'''


'''for i in range(5):
    for j in range (i):
        print("1","0",end="")
    print(1)'''

'''rows = 4
for i in range(1, rows+1):
    for j in range(i):
        if j % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()'''


'''for i in range(10):
    for j in range(i*i):
        print(i)
    print()'''


#task : 2
'''take user input as number and print the output table :'''

'''num=int(input ("Enter number:"))

for i in range(1,11):
    print(num, "*", i, '=', num*i)'''



#task : 3
num = int(input("Enter a number: "))

for i in range(1, num+1):
    print(f"Table of {i}:")
    
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()
