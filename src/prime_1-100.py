""" Program to print the print numbers between 1-100"""
"""Checks if a number is prime.A prime number must be greater than 1."""
def is_prime(num):
    if num <= 1:
        return False
    # Check for factors from 2 up to the square root of the number.

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False # If divisible, it's not prime
    return True # If no divisors are found, it is prime

print("Prime numbers from 1 to 100 are:")
# Loop through numbers in the specified range
for number in range(1, 101):
    if is_prime(number):
        print(number, end=" ")
