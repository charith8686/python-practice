list=list(map(int,input("Enter a list of numbers:").split()))
count=0
for num in list:
    if num%2==0:
        count+=1
print("The count of even numbers in the list is:",count)