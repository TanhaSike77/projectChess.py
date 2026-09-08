def calc():   
    num1=int(input("enter num1 value:"))
    operation= input("enter operation (+, -, *, /): ")
    num2=int(input("enter num2 value: "))
    if operation == "+":
        print(num1,"+", num2, "=",num1 + num2)
    elif operation == "-":
        print(num1, "-", num2, "=",num1-num2)
    elif operation == "*":
        print(num1, "*", num2, "=",num1*num2)
    elif operation == "/":
        if num2 == 0:
            print("ZeroDivisionError: division by zero")
        else:
            print(num1, "/", num2, "=",num1/num2)
    else:
        print("Invalid operation! Please enter one of the following: +, -, *, /")
    repeat = input("Do you want to perform another calculation? (y/n): ")
    if repeat.strip().casefold()== "yes" or repeat.strip().casefold()== "y":
            calc()
    else:
        print("Thank you for using the calculator!")
calc()

