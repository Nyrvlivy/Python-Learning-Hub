def main():
    """
    This program takes two floating-point numbers as input and performs basic arithmetic operations with them. It calculates the sum, difference, product, and quotient of the two numbers. Finally, the program displays the input numbers and the results of the arithmetic operations.

    Input:
    - Enter two floating-point numbers when prompted.

    Output:
    - The program will display the input numbers and the results of the arithmetic operations.

    Example:
    Enter the first number: 7
    Enter the second number: 5
    Number 1: 7.0
    Number 2: 5.0
    Total: 12.0
    Difference: 2.0
    Product: 35.0
    Quotient: 1.4
    """

    # Inputs
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Print inputs
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")

    # Variables
    total = num1 + num2
    difference = num1 - num2
    product  = num1 * num2
    quotient = num1 / num2

    # Print Results
    print(f"Total: {total}")
    print(f"Difference: {difference}")
    print(f"Product: {product}")
    print(f"Quotient: {quotient}")

if __name__ == "__main__":
    main()
    