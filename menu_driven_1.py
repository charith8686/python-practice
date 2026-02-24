string=input("Enter a string:")
def reverse_string():
     print("Reversed string is:",string[::-1])
def vowel_count():
    count=0
    s=string.lower()
    for i in s:
        if i in 'aeiou':
            count+=1
    print("Number of vowels in the string is:",count)
def palindrome_check():
    if string==string[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
while True:
    print("\nMenu:")
    print("1. Reverse the string")
    print("2. Count the number of vowels in the string")
    print("3. Check if the string is a palindrome")
    print("4. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        reverse_string()
    elif choice==2:
        vowel_count()
    elif choice==3:
        palindrome_check()
    elif choice==4:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")