#Write a Python function to calculate the factorial of a number (a nonnegative integer)

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

num = 5
result = factorial_recursive(num)
print(f"The factorial of {num} is {result}")
