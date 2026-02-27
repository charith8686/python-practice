x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
def find_max(x,y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return "Both numbers are equal"
print("The maximum of numbers is", find_max(x,y))