#Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Sample data: {'1': ['a','b'], '2': ['c','d']}

d1={'1': ['a','b'], '2': ['c','d']}

print(d1['1'][0]+d1['1'][1])
print(d1['1'][0]+d1['2'][0])
print(d1['1'][1]+d1['2'][0])
print(d1['1'][1]+d1['2'][1])

