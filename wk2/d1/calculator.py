def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mult(x,y):
    return x * y
def divide(x,y):
    return x / y

while True:


    options = ['1','2','3','4']

    choice = input("Please enter the number of the operation you wish to perform:\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n ")

    if choice in options:
        num1 = float(input("Please enter your first number: "))
        num2 = float(input("Please enter your second number: "))

    #print(f"{num1},{num2}")
        print("Your answer is: ")
        if choice == '1':
            print(add(num1,num2))
        elif choice == '2':
            print(sub(num1,num2))
        elif choice == '3':
            print(mult(num1,num2))
        elif choice == '4':
            print(divide(num1,num2))
        next_calculation = input("Would you like to do another calculation? (y/n): ")
        if next_calculation == "n":
            print("Ok, bye!")
        
            break
    else:
        print(f"Please make a valid selection from {options}")

