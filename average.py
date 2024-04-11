# Author: Jovane Cano
# GitHub Username: jovanecano
# Date: 04/09/2024
# Description: This program asks the user for five numbers and then prints out the average of those numbers

# Asking user to input the five numbers
num1 = float(input("Please enter the first number:"))
num2 = float(input("Please enter the second number:"))
num3 = float(input("Please enter the third number:"))
num4 = float(input("Please enter the fourth number:"))
num5 = float(input("Please enter the fifth number:"))

# Adding all the numbers up and assigning value to the variable
sum_of_numbers = num1 + num2 + num3 + num4 +num5
average = sum_of_numbers / 5
print(f"The average of those numbers is: {average}")