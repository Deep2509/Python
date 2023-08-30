#Write a Python function that checks whether a passed string is palindrome or not

def isPalindrome(s):
    return s == s[::-1]
 
 

s = "cake"
ans = isPalindrome(s)
 
if ans:
    print("It is a palindrome")
else:
    print("It is not palindrome")
