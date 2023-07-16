#Write python program that swap two number with temp variable and without temp variable.

#1.
x = 5
y = 10

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

#2.

x = 3
y = 6

x, y = y, x

print('x equals: ', x)
print('y equals: ', y)


