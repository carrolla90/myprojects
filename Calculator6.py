name = input("Hi! Please confirm your name ")
print("Welcome to my Python calculator " + name)

num1 = float(input("Please type a number: "))
op = input("Choose an operator. Enter + to add, - to minus, * to multiply or / to divide  : ")
num2 = float(input("Type a second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator. Please check again")
    