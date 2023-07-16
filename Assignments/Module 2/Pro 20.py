#Write a Python function that takes a list of words and returns the length of the longest one.

words=input("Enter words: ")
max_length = 0

for word in words:
    length = len(word)
    if length > max_length:
        max_length = length
    return max_length

