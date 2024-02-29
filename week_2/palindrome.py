#program that checks whether a string is a palindrome
#date:22/2/2024
#name: Sandra

def  ispalindrome(s):
    return s ==s[::-1]

s= "civic"
ans = ispalindrome(s)

if ans:
    print("Yes the string you have entered is a palindrome")
else:
    print("no the string you have entered is not a palindrome")