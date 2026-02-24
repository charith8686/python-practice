string=input("Enter a string:")
def vowel_count():
    count=0
    string=string.lower()
    for i in string:
        if i in 'aeiou':
            count+=1
    print("Number of vowels in the string is:",count)
vowel_count()