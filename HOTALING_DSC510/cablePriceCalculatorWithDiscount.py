# Programming Assignment 2.1 
# Michael Hotlaing
# This programm will:  
#	1) Welcome the user
#	2) Retrieve the company name from the user
#	3) Retrieve the number of feet of fiber optic cable to be installed from the user
#	4) Calculate the installation cost of fiber optic cable by multiplying
#	   the total cost as the number of feet times $0.87.
#	5) Print a receipt for the user including 
#	   The Company Name
#	   The Number of Feet of fiber optic cable to be installed
#	   The Calculated Cost
#	   The Total Cost

# We will create a definition here to check the price of the cable 
def bulkDiscount(feet):
	if feet > 500:
		return 0.50
	elif feet > 250:
		return 0.70
	elif feet > 100:
		return 0.80
	else:
		return 0.87

# Introdution
print("Hello! Welcome to the Fiber Optic Price Calculator!")

# Asking the user which company they are from
# Convert the company name to a string in case it is something like "101" Cable Oompany
company = input("Which company are you from?: ")
print("Okay! You are from " + str(company) +". That's great to hear!" )

# Asking the user how many feet of cable they will need for their job
# There is no error handling here, so if a string is passed, it will break the program
fiberLength = float(input("How many feet of fiber optic cable is required?: "))
if bulkDiscount(fiberLength) != 0.87:
	print("Good news! You are eligible for our bulk discount!")


# We will need to round the total price to prevent float issues
print("You will need " + str(fiberLength) + " feet of fiber optic cable! That will cost you $" + str(round(bulkDiscount(fiberLength) * fiberLength,2)))

# Some print statements to create some room between the chat and the receipt
print()
print()

# Printing the receipt
print("--" + company + " Cable Company--")
print("--Fiber Optic Receipt--")
print("-Feet of Cable: " + str(fiberLength) + "-")
print("-Price per Foot: $" + str(float(bulkDiscount(fiberLength))) + "-")
print("-Total Cost: $" + str(round(bulkDiscount(fiberLength) * fiberLength,2)) + "-")