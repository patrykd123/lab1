def factorial(n):
    """
    Calculates the factorial of a given number n.

    Args:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of n.
    """
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        number = int(input("Enter a non-negative integer: "))
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"The factorial of {number} is {factorial(number)}.")
    except ValueError:
        print("Please enter a valid integer.")