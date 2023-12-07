#Palindrome checker

s=input("Enter a word: ")
if s[::-1]==s:
    print("The given word is a palindrome.")
else:
    print("The given word is not a palindrome.")