""" Program to print the print numbers between 1-100"""
def Prime(n):
    if n>1:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                print(i)
prime_numbers = [num for num in range(1,101)if Prime(num)]
print(prime_numbers)