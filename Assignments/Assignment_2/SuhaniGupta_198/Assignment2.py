# Find sum of first 10 natural numbers

sum = 0
for i in range(1,11) :
    sum += i

print("Sum: ", sum)

# Find factorial of a number

n = int(input("Enter a number: "))
fact = 1
for i in range(1,n+1) :
    fact*= i
print("Factorial: ", fact)

# Print fibonacci series 

n = int(input("Enter any number: ")) 
a = 0
b =1
for i in range(n) :
    print(a, end=" ")
    a,b = b, a+b

# Largest among three numbers

a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))

if a >=b and a >= c:
    largest = a
elif b >= a and b >= c :
    largest = c
else :
    largest = c

print(largest)

# Create student result system

name = input("enter student's name: ")
sci = int(input("enter science marks: "))
maths = int(input("enter maths marks: "))
hindi = int(input("enter hindi marks: "))

max_marks = 300
total_marks = sci+maths+ hindi
percentage = (total_marks/max_marks)*100
print("Percentage: ", percentage)

if(total_marks >=90)  :
    grade = 'A'
elif(total_marks>=80) :
    grade = 'B'
elif(total_marks >= 70) :
    grade = 'C'
else :
    grade = 'D'

print("Grade: ", grade)
