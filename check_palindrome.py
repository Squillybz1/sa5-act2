def check_palindrome(text):
    if text == text[::-1]:
        print(f"{text} is a palindrome")
    else:
        print(f"{text} is not a palindrome")


<<<<<<< HEAD
text = input("Enter text to check for palindrome: ")
check_palindrome(text)
=======
try:
    filepath = input("Enter filepath for palindrome check: ")
    text = open(filepath, "r").read()
    check_palindrome(text)
except OSError:
    print(f"Unable to process file at {filepath}")
>>>>>>> a352e06 (Replaced hardcoded text string with filepath input and read file content)
