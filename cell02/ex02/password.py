#!/usr/bin/env python3

# Variable containing the password
password = "Python is awesome"

# Prompt user for password
user_input = input("Enter password: ")

# Check if the entered password is correct
if user_input == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
