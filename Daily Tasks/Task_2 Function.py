def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b 

def modulo(a, b):
    return a % b

def calculator():
    status=True
    while status:
        print("\n============== Choice Board ==============")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulo")
        print("6. Exit")

        choice = int(input("\nEnter Your Choice: "))

        if choice == 6:
            print("\nThank You")
            break

        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:
            result = addition(num1, num2)
        elif choice == 2:
            result = subtraction(num1, num2)
        elif choice == 3:
            result = multiplication(num1, num2)
        elif choice == 4:
            result = division(num1, num2)
        elif choice == 5:
            result = modulo(num1, num2)
        else:
            print("\nInvalid Choice. Please select a valid option.")
            continue

        print(f"\nYour Answer: {result}")

        repeat = input("Do You Want to continue? ['y' or 'n']: ")
        
