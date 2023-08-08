
 
def area_circle(r):
    pie=3.14
    return pie*r**2

    

def traingle_area(Breadth,Height):
    return 1/2*Breadth*Height

 
def rectangle_area(Length,B):
        return Length*B
    

def main():
    print("=============Area Finder=============")
    print("1. Circle")
    print("2. Triangle")
    print("3. Rectangle")

    choice = int(input("\nEnter Your Choice: "))

    
   
      

    if choice==1:
        
        r=float(input("Please enter the radius: "))
        result= area_circle(r)
    elif choice==2:
        Breadth=int(input("Enter the breadth:"))
        Height=int(input("Enter the height:"))
        result=traingle_area(Breadth,Height)
    elif choice==3:
        Length=int(input("Enter the length:"))
        B=int(input("Enter the breadth:"))
        result=rectangle_area(Length,B) 
    

    print(f"\nYour Answer: {result}")


main()
        

main()           

