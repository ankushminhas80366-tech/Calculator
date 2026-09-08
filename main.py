"""Simple command-line calculator.

Supports addition, subtraction, multiplication, division, and modulo.
Run this file directly to start an interactive loop in the terminal.
"""


def add(a, b):
    """Return the sum of a and b."""
    # Addition works for both integers and floats.
    return a + b


def subtract(a, b):
    """Return the difference of a and b (a minus b)."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b.

    Raises:
        ValueError: If b is zero, since division by zero is undefined.
    """
    # Guard against a mathematically invalid operation.
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


def modulo(a, b):
    """Return the remainder of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot take modulo by zero!")
    return a % b


def get_number(prompt):
    """Prompt the user until a valid number is entered, then return it as float."""
    while True:
        try:
            # float() accepts values like 3, 3.14, and -2.5.
            return float(input(prompt))
        except ValueError:
            # Input could not be converted to a number; ask again.
            print("Invalid input! Please enter a valid number.")


def main():
    """Run the interactive calculator loop until the user types 'exit'."""
    print("Simple Calculator")
    print("Operations: +, -, *, /, %")
    print("Type 'exit' to quit.\n")

    # Keep asking for operations until the user chooses to quit.
    while True:
        try:
            # Ask which operation to perform, or allow the user to quit.
            operation = input("Enter operation (+, -, *, /, %) or 'exit': ").strip()

            if operation.lower() == "exit":
                print("Goodbye!")
                break

            # Only the symbols listed here are accepted.
            if operation not in ["+", "-", "*", "/", "%"]:
                print("Invalid operation! Please choose +, -, *, /, or %.")
                continue

            # Collect the two operands from the user.
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
            elif operation == "%":
                result = modulo(num1, num2)

            # Print a blank line after the result so the next prompt is easier to read.
            print(f"Result: {result}\n")

        except ValueError as e:
            # Covers divide-by-zero, modulo-by-zero, and similar value problems.
            print(f"Error: {e}\n")
        except Exception as e:
            # Catch-all so an unexpected failure does not crash the whole program.
            print(f"An unexpected error occurred: {e}\n")


# Start the calculator only when this file is run directly,
# not when it is imported as a module.
if __name__ == "__main__":
    main()
