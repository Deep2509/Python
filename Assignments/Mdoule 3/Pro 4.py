#Write a Python function to get the largest number, smallest num and sum of all from a list.

lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))  #We can use min,max and sum to achieve this task.
    lst.append(numbers)
print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst) , "\nSum of all elements in the list is :", sum(lst)) 




