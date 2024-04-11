# Author: Jovane Cano
# GitHub Username: jovanecano
# Date: 04/09/2024
# Description: This program asks the user for number (int) of cents, from 0 - 99, and outputs how many of each type of coin would represent that amount wiht the fewest number of coins

# Asking the user to input an integer from 0-99
cents = int(input("Please enter an amount of cents less than a dollar. "))

# Creating the values for each of the coins worth less than 100 cents
HD = cents % 50
Q = cents % 25
D = cents % 10
N = cents % 5
P = cents % 1

print(f"Your change will be: \n{HD} \n{Q} \n{D} \n{N} \n{P}")
