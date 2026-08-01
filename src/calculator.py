import math

def sqrt(x):
    if x < 0:
        return "Error! Square root of negative number."
    return math.sqrt(x)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    return x ** y

def main():
    print("--- Simple Python Calculator ---")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")

    while True:
        choice = input("\nEnter choice (1/2/3/4/5/6) or 'q' to quit: ")

        if choice.lower() == 'q':
            print("Exiting calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5', '6'):
            try:
                if choice == '6':
                    num1 = float(input("Enter number: "))
                    num2 = None # Square root only needs one number
                else:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            elif choice == '5':
                print(f"{num1} ** {num2} = {power(num1, num2)}")
            elif choice == '6':
                print(f"sqrt({num1}) = {sqrt(num1)}")
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()