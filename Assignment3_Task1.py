#Assignment 3 Task 1: Calculate Factorial Using a Function
number=int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"Factorial of {number} is:",factorial)