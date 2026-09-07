"""Simple command-line calculator.

Supports addition, subtraction, multiplication, and division.
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


def get_number(prompt):
    """Prompt the user until a valid number is entered, then return it as float."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            # Input could not be converted to a number; ask again.
            print("Invalid input! Please enter a valid number.")


def main():
    """Run the interactive calculator loop until the user types 'exit'."""
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            # Ask which operation to perform, or allow the user to quit.
            operation = input("Enter operation (+, -, *, /) or 'exit': ").strip()

            if operation.lower() == "exit":
                print("Goodbye!")
                break

            if operation not in ["+", "-", "*", "/"]:
                print("Invalid operation! Please choose +, -, *, or /.")
                continue

            # Collect the two operands.
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            # Dispatch to the matching arithmetic function.
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
            # Covers divide-by-zero and similar input/value problems.
            print(f"Error: {e}\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")


# Start the calculator when this file is run directly.
if __name__ == "__main__":
    main()
