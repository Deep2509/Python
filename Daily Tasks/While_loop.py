
status=True

while(status):
    a=input("Please Enter your name: ")
    print("Your name is: ",a)

    ip=input("Do you want to continue? '{y}'/'{n}'")

    if ip=='y' or ip=='Y':
        print(a)
    else:
        status=False
    
