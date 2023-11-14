# Basic Calculator
#Welcome message and menu of operators
print("---Basic Calculator---")
print("Welcome User!")
print("Description: This is a simple calculator.")
print(" ")

# Defining Operators as a function
#Addition
def add(num1, num2):
   return(num1 + num2)
#Subtraction
def subtract(num1, num2):
    return(num1 - num2)
#Multiply
def multiply(num1, num2):
    return(num1 * num2)
#Divide
def divide(num1, num2):
    if num2 !=0:
        return(num1 / num2)
    else:
        print("Undefined Answer:Division Error")
        return None

#Looping the calculator
while True:
    #User will input operator
    print("  ")
    print("Please select operator from the following list only: ")
    print("Addition :        +")
    print("Subtraction :     -")
    print("Multiplication :  *")
    print("Division :        / ")
    print("  ")
    operator = input("Enter your operator: ")

    try:
    #USer will input number to be computed
        firstNumber = float(input("Enter your first number: "))
        secondNumber = float(input("Enter your second number: "))
    except ValueError:
        print("Value Error: Please enter valid numeric values.")
        continue

    #Print the following calculations   
    if operator == "+":
        print("Answer is: ", add(firstNumber,secondNumber))
    elif operator == "-":
        print("Answer is" , subtract(firstNumber,secondNumber))
    elif operator == "*":
        print("Answer is", multiply(firstNumber,secondNumber))
    elif operator == "/":
        result = divide(firstNumber,secondNumber)
        if result is not None:
            print("Answer is" , result)
    else:
        print("Syntax Error, Please Enter correct operator")
        continue
    #Choose if you want to continue or not
    choice = input("Do you want to contiune to calculate, Y/N ? ").upper()
    if choice == "Y":
        print("Perfect!")
        continue
    if choice == "N":
        print ("Bye!, Exiting Calculator...")
        break