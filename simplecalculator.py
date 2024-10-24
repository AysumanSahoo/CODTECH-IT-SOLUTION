#simple calculator create by using python compiler....
# Addition Function
def addition(x, y):
    return x + y

# Subtraction Function
def subtraction(x, y):
    return x - y

# Multiplication Function
def multiplication(x, y):
    return x * y

# Division Function
def division(x, y):
    return x / y

print("...........SIMPLE CALCULATOR.....................")
print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", addition(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtraction(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiplication(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", division(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input try again......")
