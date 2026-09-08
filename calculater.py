def calculator():

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    operater = input("Enter an operator: ")

    if operater  == "+":
        print(num1 + num2)
    elif operater == "-":
        print(num1 - num2)
    elif operater == "/":
        if num2 == 0:
            print("Zero error")
        else:
            print(num1 / num2)
    elif operater == "*":
        print(num1 * num2)
    else: 
        print("Invalid Operator")

calculator()
