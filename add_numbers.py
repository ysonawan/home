#!/usr/bin/env python3
"""
A simple Python script to add two numbers.
"""


def add_two_numbers(a, b):
    """
    Add two numbers together.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        The sum of a and b
    """
    return a + b


def main():
    """
    Main function to demonstrate adding two numbers.
    """
    # Example usage
    num1 = 10
    num2 = 20
    result = add_two_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")

    # Interactive mode
    print("\nInteractive mode:")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = add_two_numbers(num1, num2)
        print(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")


if __name__ == "__main__":
    main()
