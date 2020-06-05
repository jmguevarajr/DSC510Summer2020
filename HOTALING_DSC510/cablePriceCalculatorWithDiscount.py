# Programming Assignment 3.1
# #Michael Hotaling
# This program will: 1) Welcome the user 2) Retrieve the company name
# from the user 3) Retrieve the number of feet of fiber optic cable to be installed from the user 4) Calculate the
# installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87. 5) Print a
# receipt for the user including The Company Name The Number of Feet of fiber optic cable to be installed The
# Calculated Cost The Total Cost


# Introduction
print('Hello! Welcome to the Fiber Optic Price Calculator!')

# Asking the user which company they are from
# Convert the company name to a string in case it is something like "101" Cable Company
company = input('Which company are you from?: ')
print("Okay! You are from " + str(company) + ". That's great to hear!")

# Asking the user how many feet of cable they will need for their job
# There is no error handling here, so if a string is passed, it will break the program
fiberLength = float(input('How many feet of fiber optic cable is required?: '))

# We will check for the price per length of cable here
# If the user requests more than a certain amount of cable, they will get a discount
if fiberLength > 500:
	fiberPrice = 0.50
elif fiberLength > 250:
	fiberPrice = 0.70
elif fiberLength > 100:
	fiberPrice = 0.80
else:
	fiberPrice = 0.87


if fiberPrice != 0.87:
	print("Good news! You're eligible for our bulk discount!")


# We will need to round the total price to prevent float issues
print('You will need ' + str(fiberLength) + " feet of fiber optic cable! That will cost you $" + str(round(fiberPrice * fiberLength, 2)))

# Some print statements to create some room between the chat and the receipt
print()
print()

# Printing the receipt
print("--" + company + " Cable Company--")
print("--Fiber Optic Receipt--")
print("-Feet of Cable: " + str(fiberLength) + "-")
print("-Price per Foot: $" + str(float(fiberPrice)) + "-")
print("-Total Cost: $" + str(round(fiberPrice * fiberLength, 2)) + "-")
