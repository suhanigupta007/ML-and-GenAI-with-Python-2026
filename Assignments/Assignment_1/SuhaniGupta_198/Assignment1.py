#Find the area of the rectangle

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

area = length*breadth

print("Area:", area)

# Find simple interest

P = 1000
R=2
T=2
si = P*R*T/100

print("Simle interest: ", si)

# Convert Temperature from Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(celsius, "C =", fahrenheit, "F")

#Calculate Average of 3 Numbers

num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
 
average = (num1 + num2 + num3) / 3
print("Average: ", average)

#Find Square and Cube of a Number

number = float(input("\nEnter a number: "))
 
square = number ** 2
cube   = number ** 3
 
print("Square: ", square)
print("Cube: ", cube)

#Swap Two Numbers Without a Third Variable

a = float(input("\nEnter first number (a): "))
b = float(input("Enter second number (b): "))

print("Before swap: a =", a, "b = ", b)

a,b = b,a
print("After swap: a =", a, "b = ", b)

#Student Report Program

student_name   = input("Enter student name: ")
roll_number    = input("Enter roll number : ")

marks_english  = float(input("Enter marks in English  (out of 100): "))
marks_math     = float(input("Enter marks in Maths    (out of 100): "))
marks_science  = float(input("Enter marks in Science  (out of 100): "))
marks_hindi    = float(input("Enter marks in Hindi    (out of 100): "))
marks_computer = float(input("Enter marks in Computer (out of 100): "))

total_marks     = marks_english + marks_math + marks_science + marks_hindi + marks_computer
maximum_marks   = 500 # 5 subjects × 100
percentage      = (total_marks / maximum_marks) * 100

print(total_marks, percentage)


                       

