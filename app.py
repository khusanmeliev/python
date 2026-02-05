operator = input("enter an operator (+,-,*,/): ")

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

if operator == "+":
    print((num1 + num2))
elif operator == "-":
    print(round(num1 - num2))
elif operator == "*":
    print(f"{num1} multipled by {num2} is {round(num1*num2)}")
else:
    print(round(num1 / num2))
