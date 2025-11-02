def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

print("Hello,welcome to calulator App")
print("Please select operation - \n")
print("1.add")
print("2. substract")
print("3. multiply")
print("4. divide")
print("5. exit")
ch=input("Enter your choice:")

if ch=="1":
    print("Addition")
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print("The sum is:",add(a,b))
elif ch=="2":
    print("subtraction")
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print("The diffrence is:",subtract(a,b))

    


