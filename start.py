num1=int(input("enter num1 value:"))
operation= input("enter operation (+, -, *, /): ")
num2=int(input("enter num2 value: "))
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/":
    print(num1/num2)
else:
    print("invalid operation")