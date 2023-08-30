 #Write a Python function that takes two lists and returns true if they have at least one common member.

def common_data(list1, list2):
     'result = False'
     for x in list1:
         for y in list2:  #If there will be any element which is common the result will be true and it will return the same.
             if x == y:
                 result = True
                 return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))
