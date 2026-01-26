def calculator():
    operations = {'1': '+', '2': '-', '3': '*', '4': '/'}
    print("Select operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))

    if choice in operations:
        if choice == '4' and num2 == 0:
            print("Error! Division by zero.")
        else:
            result = eval(f"{num1} {operations[choice]} {num2}")
            print(f"Result: {result}")
    else:
        print("Invalid choice")

calculator()
