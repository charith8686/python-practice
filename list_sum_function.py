list=list(map(int,input("Enter list numbers: ").split()))
def find_sum(list):
    sum=0
    for i in list:
        sum+=i
    return sum
print("The sum of numbers is", find_sum(list))