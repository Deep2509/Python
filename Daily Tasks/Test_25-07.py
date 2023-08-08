'''def sq_root(a):
    return a**(1/2)
a=int(input("Enter the number: "))

print("Square root is: ",sq_root(a))'''


'''def fibo(b):
    return fibo(b-1)+fibo(b-2)
b=int(input("ENter the number: "))

print("Fibonacci series: ",fibo(b))'''

'''def fact(a):
    fact = 1
    for num in range(2, a + 1):
        fact *= num
    return fact

a=int(input("Enter the number: "))

print("Factorial is: " ,fact(a))'''




#List Tasks

l1=[21,15,23,54,20,31,10,9,12,15]

'''l2=[]

for i in l1:

    if i not in l2:
        l2.append(i)
                
print(l2)'''


#List Task 3
l1.sort()
print(l1)

#List Task 2

l=len(l1)

for i in range(l-1,-1,-1):
    print(l1[i],end=' ')
