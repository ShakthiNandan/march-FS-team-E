# Function to calculate factorial using recursion
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Input from the user
number = int(input("Enter a number to find its factorial: "))

# Check for negative input, as factorial is not defined for negative numbers
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calculate and print the factorial
    result = factorial(number)
    print(f"The factorial of {number} is {result}.")
