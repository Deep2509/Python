#Write a Python program to remove an empty tuple(s) from a list of tuples

l1=[(), ('ram','15','8'), (), ('laxman', 'sita'),('krishna', 'akbar', '45'), ('',''),()]


for i in l1:
    if(len(i)==0 or i.__contains__('')):
        print(i)
        l1.remove(i)
