# Simple calculator, it can add, subtract, multiply and divide two numbers.

import sys

def add(x,y):
	return x + y
	
def sub(x,y):
	return x - y
	
def mul(x,y):
	return x * y
	
def div(x, y):
	return x / y
	
def twoNums():
	
	while True:	
		
		try:
			x = int(input("Input the first number:"))
			y = int(input("Input the second number:"))
			break
			
		except ValueError:
			print("Please enter a valid number!")
			print()
			
	return x, y		
	
def again():
	
	while True:
		print("Do you want to calculate again?")
		print("1. Yes")
		print("2. No")
		
		try:
			
			yesNo = int(input(": "))
			
			if (yesNo == 1):
				print("Program restarting ...")
				print()
				break
				
			elif (yesNo == 2):
				print("Program exiting ...")
				sys.exit()
				
			else:
				print("Please enter 1 or 2")
				print()
				
		except ValueError:
			print("Please enter a valid number!")
			print()

def printInstructions():
	print("Input the numbers you want to perform the operation on")

while True:
	print("Choose a function:")
	print("1. Add")
	print("2. Subtract")
	print("3. Multiply")
	print("4. Divide")
	print("0. Exit")
	
	try:
		n = int(input(": "))
	
	except ValueError:
		print("Error! You must enter a number.")
		print()
		n = -1
	
	if (n == 0):
		print("Program exiting ...")
		break
			
	elif (n == 1):
		printInstructions()
		x,y = twoNums()
		print(add(x, y))
		
	elif (n == 2):	
		printInstructions()
		x,y = twoNums()
		print(sub(x, y))
		
	elif (n == 3):
		printInstructions()
		x,y = twoNums()
		print(mul(x, y))
		
	elif (n == 4):
		
		printInstructions()
		x,y = twoNums()
		if (y == 0):
			print("The second number cannot be 0!")
			print()
		else:
			print(div(x, y))
		
	else:
		print("You did not enter a value from 0 to 4, please try again!")
		print()
	
	again()
	
