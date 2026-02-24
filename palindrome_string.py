string=input("Enter a string:")
def palindrome_check():
    if string==string[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
palindrome_check()