# Print numbers from 1 to 10

def numbers() :
    for i in range(1,11) :
        print(i)

print("The first 10 natural numbers: ")
numbers()

# Create a function to calculate the sum of first n natural no.'s

def sum(n) :
    return n*(n+1)//2

n  = int(input("enter any no."))

print("Sum: ", sum(n))

# Create a function to reverse a number

def reverse(n) :
    rev = 0
    while n>0 :
        digit = n%10
        rev = rev*10 + digit
        n //= 10
    return rev

n = int(input("enter any no.: "))
print("Reversed no.: ", reverse(n))

# Create a function to count the no. of digits in a number

def count(n) :
    count = 0
    if n==0 :
        return 1
    while n>0 :
        count += 1
        n //= 10
    return count

n = int(input("enter any no.: "))
print("No. of digits: ", count(n))

# Create a function to check palindrome no.

def check_palindrome(n) :
    original = n
    rev = 0
    while n>0: 
        digit = n%10
        rev = rev*10 + digit
        n //= 10
    if (rev==original) : return True
    else : return False
n = int(input("enter any no.: "))
if(check_palindrome(n)) :
    print("is palindrome")
else :
    print("Not a palindrome")

# Create a function to generate fibonacci series 

# 6. Function to generate Fibonacci series

def fibonacci(n):
    a, b = 0, 1

    print("Fibonacci Series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter number of terms: "))
fibonacci(n)

# calculator using functions 

# 7. Calculator Using Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b

print("\nCalculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result =", add(num1, num2))
elif choice == 2:
    print("Result =", subtract(num1, num2))
elif choice == 3:
    print("Result =", multiply(num1, num2))
elif choice == 4:
    print("Result =", divide(num1, num2))
else:
    print("Invalid Choice")

# Create a text file and store student details

name = input("Enter student name: ")
roll = input("Enter roll number: ")
marks = input("Enter marks: ")

file = open("student.txt", "w")

file.write("Name: " + name + "\n")
file.write("Roll No: " + roll + "\n")
file.write("Marks: " + marks + "\n")

file.close()

print("Student details saved successfully.")

# Read data from a file

file = open("student.txt", "r")

data = file.read()

print("File Contents:")
print(data)

file.close()

# Handle division by zero using exception handling

try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Please enter valid numbers.")

# Create a Student class with name and marks

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


name = input("Enter student name: ")
marks = float(input("Enter marks: "))

s1 = Student(name, marks)

print("\nStudent Details")
s1.display()

