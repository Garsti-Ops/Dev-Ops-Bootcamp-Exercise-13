def getInputs():
    global input1
    global input2
    global operator
    input1 = input("Enter number 1 or exit\n")
    input2 = input("Enter number 2 or exit\n")
    operator = input("Enter operator or exit\n")


getInputs()

print(input1)
while input1 != "exit" and input2 != "exit" and operator != "exit":
    num1 = int(input1)
    num2 = int(input2)

    if operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    elif operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    else:
        print("Wrong operator")

    getInputs()