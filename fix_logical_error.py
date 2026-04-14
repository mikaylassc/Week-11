""" 
Mikayla Settles-Chambers
CMSC 111
Spring 2026
AI Used: GPT-5.3-based Chat GPT
Assignment 2: Debugging Logical Errors
"""
# This program fixes a logical error and safely multiplies two values

def multiply(a, b):
    """
    Returns the product of two numbers.
    Includes basic error handling to ensure valid numeric input.
    """
    try:
        # Attempt multiplication
        product = a * b
        return product
    except TypeError:
        # Handle cases where inputs are not numbers
        print("Error: Both inputs must be numbers.")
        return None

# Test the function with correct values
result = multiply(5, 2)

# Only print if a valid result was returned
if result is not None:
    print(result)