#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#result = int(num1) + int(num2)

#print(result)


#Here, the calculator works the same way but the
#Arithmetic operations need to be changed manually

print("Select an operation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation == "1":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) / int(num2)))
else:
    print("Invalid Entry")

#Here is a more complex calulator where it can accept
#User input and can choose between the addition,
#Subtraction, multiplication and division
#If no input is entered, then it returns ("Invalid Entry")