#Write a Python script to sort (ascending and descending) a dictionary by value.

d1={'Deep':32, 'Mitesh':87, 'Raman':12, 'Ankit':69, 'Disha':10}
sorted_values_asc=sorted(d1.values())
sorted_values_des=sorted(d1.values(), reverse=True)
print(sorted_values_asc)
print(sorted_values_des)
        

