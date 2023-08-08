#Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(l):
  x = []
  for a in l:
    if a not in x: #Have used membership operator to accomplish this.
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 
