# Author: Jovane Cano
# GitHub Username: jovanecano
# Date: 04/09/2024
# Description: This program allows the user to input Celsius temperature then it to Fahrenheit temperatures.

cel_temp = float(input("Please enter Celsius temperature. ")) # Asking user to input Celsius temperature

# Conversion Formula: F = (9/5)C + 32, where F is Fahrenheit and C is Celsius
fahrenheit_temp = (9/5)*cel_temp + 32

# Printing the Fahrenheit temperature
print(f"The equivalent Fahrenheit temperature is:\n {fahrenheit_temp}")
