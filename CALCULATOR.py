a = int(input("enter your first number "))
b = int(input("enter your second number "))
operator = input("enter your operator( + , - , / , * ): ")

if operator == "+" :
    print(a+b)
elif operator == "-":
    print(a-b)
elif operator == "*":
    print(a*b)
elif operator == "/":
    print(a/b)
else :                                                                                                                                                                                                                                                               
    print("invalid operator")