def add(num1, num2):
    addition= num1+ num2
    return addition
def subtract(num1,num2):
    subtraction= num1-num2
    return subtraction
def product(num1, num2):
    multiplication= num1*num2
    return multiplication
def divide(num1,num2):
    division= num1/num2
    return division

print("Which operation do you want to use?")
print("1 .Addition")
print("2 .Subtraction")
print("3 .Multiplication")
print("4 .Division")
print("\n")

operation= int(input("Enter the operation number: "))
num1= int(input("Enter first value: "))
num2= int(input("Enter second value: "))
print("\n")

if operation == 1:
    print(num1,"+", num2,"=", add(num1,num2))
elif operation == 2:
    print(num1,"-", num2,"=", subtract(num1,num2))    
elif operation== 3:
    print(num1,"÷", num2,"=", divide(num1,num2))
elif operation==4:
    print(num1,"×", num2,"=", add(num1,num2))    
else:
    print("Invalid input!")    

