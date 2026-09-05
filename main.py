def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            operation = input("Enter operation (+, -, *, /) or 'exit': ").strip()

            if operation.lower() == "exit":
                print("Goodbye!")
                break

            if operation not in ["+", "-", "*", "/"]:
                print("Invalid operation! Please choose +, -, *, or /.")
                continue

            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if operation == "+":
                result = add(num1, num2)
            elif operation == "-":
                result = subtract(num1, num2)
            elif operation == "*":
                result = multiply(num1, num2)
            elif operation == "/":
                result = divide(num1, num2)

            print(f"Result: {result}\n")

        except ValueError as e:
            print(f"Error: {e}\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")

if __name__ == "__main__":
    main()
