print("Welcome to Registration Process")
email=input("Enter Email: ") 
Pswd=input("Enter Password: ")


d1={}
if len(Pswd)>4 and len(Pswd)<8:
    d1['email']=email
    d1['pswd']=Pswd
    print(d1)
else:
    print("Password invalid")



em=input("Enter Email: ")
ps=input("Enter Password: ")

if email == d1['email'] and Pswd==ps:
    print("Login Success")

else:
    print("Access Denied")
    
