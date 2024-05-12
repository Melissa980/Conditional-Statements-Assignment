# Question 2 Task 1
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

print("Entered numbers:", number1, ",", number2, ",", number3)

if number1 >= number2 and number1 >= number3:
    largest = number1
elif number2 >= number1 and number2 >= number3:
    largest = number2
else:
    largest = number3

print("The largest number is:", largest)

# Question 2 Task 2
if number1 <= number2 and number1 <= number3:
    smallest = number1
elif number2 <= number1 and number2 <= number3:
    smallest = number2
else:
    smallest = number3

print("The smallest number is:", smallest)

# Question 2 Task 3
if number1 == number2 == number3:
    print("All numbers are equal.")
elif number1 == number2:
    print("The first and second numbers are equal.")
elif number2 == number3:
    print("The second and third numbers are equal.")
elif number1 == number3:
    print("The first and third numbers are equal.")
else:
    print("No two numbers are equal.")