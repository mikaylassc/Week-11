""" 
Mikayla Settles-Chambers
CMSC 111
Spring 2026
AI Used: GPT-5.3-based Chat GPT
Assignment 1: Handling Invalid User Input
"""
# Program to safely read a number from the user

# Ask the user for input
entry = input("Enter a number: ")

try:
    # Try converting the input into an integer
    value = int(entry)
except ValueError:
    # Handle any invalid input
    print("Invalid input. Please enter a number.")
else:
    # Runs only if conversion is successful
    print("You entered:", value)