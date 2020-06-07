# Assignment 6.1
# Michael Hotaling

def temp_recorder():
	print()
	print("Welcome to the temperature recorder!")
	print("Input a numeric value below.")
	print("Type 'quit' to exit the program")
	temp = []
	while True:
		user_input = input("Please input a temperature: ")
		if user_input.lower() == "quit":
			break
		elif user_input == '':
			print("No input detected!")
			return
		temp.append(float(user_input))
	print()
	print("The maximum temperature is " + str(max(temp)))
	print("The minimum temperature is " + str(min(temp)))
	print("The number of measurement inputs is " + str(len(temp)))
	
def main():
	temp_recorder()

if __name__ == "__main__":
	main()