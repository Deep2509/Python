#Write a Python program to get unique values from a list

l1 = [10, 20, 30, 40, 20, 50, 60, 40]
print("Original List : ",l1)
my_set = set(l1)  #Have used set function to get unique element from the list
my_new_list = list(my_set)
print("List of unique numbers : ",my_new_list)
