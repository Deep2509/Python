#Write a Python program to find the second smallest number in a list.

def find_len(list1):
    length = len(list1)
    list1.sort()  # We can sort it first so automatically whichever element on the 1st position will be out second smallest number.
    print("Second Largest element is:", list1[length-2])
    print("Second Smallest element is:", list1[1])
 
# Driver Code
list1=[12, 45, 2, 41, 31, 10, 8, 6, 4]
Largest = find_len(list1)
