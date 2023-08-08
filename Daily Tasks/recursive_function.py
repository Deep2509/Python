def add(x):
    if x<=0:
        return 0
    else:
        return x+add(x-1)

num=int(input("Enter the number:"))
print(f"addition of {num} is: ",add(num))
