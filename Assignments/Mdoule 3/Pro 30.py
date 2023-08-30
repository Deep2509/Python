#Write a Python program to convert a list of tuples into a dictionary.

inputTuple = ((5, "Deep"), (6, "Mitesh"), (7, "XYZ"))
print("The input Tuple:", inputTuple)

# Here we are iterating through each element of the tuple using dictionary comprehension and converting it to the dictionary
resultDictionary = dict((x, y) for x, y in inputTuple)

print("The result dictionary:", resultDictionary)
