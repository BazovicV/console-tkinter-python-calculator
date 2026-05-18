# Prost kalkulator za sabiranje, oduzimanje, množenje i deljenje dva broja

import sys

def sab(x,y):
	return x + y
	
def odu(x,y):
	return x - y
	
def mno(x,y):
	return x * y
	
def delj(x, y):
	return x / y
	
def dvaBroja():
	
	while True:	
		
		try:
			x = int(input("Unesite prvi broj:"))
			y = int(input("Unesite drugi broj:"))
			break
			
		except ValueError:
			print("Unesite BROJ!")
			print()
			
	return x, y		
	
def opet():
	
	while True:
		print("Da li želite da računate opet?")
		print("1. Da")
		print("2. Ne")
		
		try:
			
			daNe = int(input(": "))
			
			if (daNe == 1):
				print("Ponovno računanje")
				print()
				break
				
			elif (daNe == 2):
				print("Program se gasi ...")
				sys.exit()
				
			else:
				print("Unesite broj 1 ili 2")
				print()
				
		except ValueError:
			print("Unesite BROJ!")
			print()

while True:
	print("Izaberite funkciju")
	print("1. Sabiranje")
	print("2. Oduzimanje")
	print("3. Množenje")
	print("4. Deljenje")
	print("0. Izlaz")
	
	try:
		n = int(input(": "))
	
	except ValueError:
		print("Greška! Morate upisati broj.")
		print()
		n = -1
	
	if (n == 0):
		print("Program se gasi ...")
		break
		
	print("Unesite brojeve nad kojim vršite operaciju")
		
	x,y = dvaBroja()
	
	if (n == 1):
		print(sab(x, y))
		
	elif (n == 2):	
		print(odu(x, y))
		
	elif (n == 3):
		print(mno(x, y))
		
	elif (n == 4):
		
		if (y == 0):
			print("Drugi broj ne može biti 0!")
			print()
		else:
			print(delj(x, y))
		
	else:
		print("Niste uneli vrednost od 0 do 4, pokušajte ponovo!")	
		print()
	
	opet()
	
