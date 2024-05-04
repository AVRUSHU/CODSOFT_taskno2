def add(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    if b!=0:
        return(a/b)
    else:
        return " error!dividing by zero"
print("welcome to simple calculator")
a=float(input("enter the first number: "))
b=float(input("enter the second number: "))
print("1=addition")
print("2=subtraction")
print("3=multiplication")
print("4=division")
print("enter choice")
choice=(int(input("enter choice(1/2/3/4):")))
if choice == 1:
        print("addition of two numbers (a+b)",add(a,b))
elif choice == 2:
    print("subtraction of two numbers (a-b)",subtract(a,b))
elif choice == 3:
    print("multiplication of two numbers (a*b)",multiply(a,b))
elif choice == 4:
    print("division of two numbers (a/b)",divide(a,b))
else:
    print("invalid number")
