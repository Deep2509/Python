'''def reverse(x):
    if x<=0:
        return 0
    else:
        return reverse(x-1)

num=10
print(f"reverse numbers from {num} is:",reverse(num))


x=10'''

def reverse_number(n):
    if n < 10:
        return 10
    else:
        last_digit = n % 10
        remaining_digits = n // 10
        return int(str(last_digit) + str(reverse_number(remaining_digits)))

num = 123456789
reversed_num = reverse_number(num)
print("Original number:", num)
print("Reversed number:", reversed_num)
 
