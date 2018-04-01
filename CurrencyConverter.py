#Currency Converter.py
#Scripted by Brad Szalach
#Converts USD to Euro or other way around

#1 USD = .81 Euro
#1 USD = .71 GBP
#1 USD = 106.28 JPY
#1 Euro = 1.23 USD
#1 Euro = .88 GBP
#1 Euro = 131.02 JPY
#1 GBP = 1.40 USD
#1 GBP = 1.14 Euro
#1 GBP = 149.08 JPY
#1 JPY = .0094 USD
#1 JPY = .0076 Euro
#1 JPY = .0067 GBP

#Find out what user wants to convert  1) USD -> Euro or 2) Euro -> USD

def currencyconvert():
	userchoice = input("What do you want to convert? \n 1) USD -> Euro \n 2) USD -> GBP \n 3) USD -> JPY \n 4) Euro -> USD \n 5) Euro -> GBP \n 6) Euro -> JPY \n 7) GBP -> USD \n 8) GBP -> Euro \n 9) GBP -> JPY \n 10) JPY -> USD \n 11) JPY -> Euro \n 12) JPY -> GBP \n")
	
#User choice 1
	if(userchoice == '1'):
		userUSD = float(input("Enter the amount of USD you want to convert \n"))
		Euro = (userUSD * .81)
		print("$",userUSD,"=",Euro,"Euro")
		
#User Choice 2
	elif(userchoice == '2'):
		userUSD = float(input("Enter the amount of USD you want to convert \n"))
		GBP = (userUSD * .71)
		print("$",userUSD,"=",GBP,"GBP")
		
#User Choice 3
	elif(userchoice == '3'):
		userUSD = float(input("Enter the amount of USD you want to convert \n"))
		JPY = (userUSD * 106.28)
		print("$",userUSD,"=",JPY,"JPY")
		
#USer Choice 4
	elif(userchoice == '4'):
		userEuro = float(input("Enter the amount of Euro you want to convert \n"))
		USD = (userEuro * 1.23)
		print("$",userEuro,"=","$",USD)
		
#User Choice 5
	elif(userchoice == '5'):
		userEuro = float(input("Enter the amount of Euro you want to convert \n"))
		GBP = (userEuro * .88)
		print("$",userEuro,"=",GBP,"GBP")
		
#User Choice 6
	elif(userchoice == '6'):
		userEuro = float(input("Enter the amount of Euro you want to convert \n"))
		JPY = (userEuro * 131.02)
		print("$",userEuro,"=",JPY,"JPY")

#User Choice 7
	elif(userchoice == '7'):
		userGDP= float(input("Enter the amount of GBP you want to convert \n"))
		USD = (userGDP * 1.40)
		print("$",userEuro,"=","$",USD)

#User Choice 8
	elif(userchoice == '8'):
		userGDP= float(input("Enter the amount of GBP you want to convert \n"))
		Euro = (userGDP * 1.14)
		print("$",userEuro,"=",Euro,"Euro")

#User Choice 9
	elif(userchoice == '9'):
		userGDP= float(input("Enter the amount of GBP you want to convert \n"))
		JPY = (userGDP * 149.08)
		print("$",userEuro,"=",JPY,"JPY")

#User Choice 10
	elif(userchoice == '10'):
		userJPY = float(input("Enter the amount of JPY you want to convert \n"))
		USD = (userJPY * .0094)
		print("$",userJPY,"=","$",USD)

#User Choice 11
	elif(userchoice == '11'):
		userJPY = float(input("Enter the amount of JPY you want to convert \n"))
		Euro = (userJPY * .0076)
		print("$",userJPY,"=",Euro,"Euro")

#User Choice 12
	elif(userchoice == '12'):
		userJPY = float(input("Enter the amount of JPY you want to convert \n"))
		GBP = (userJPY * .0067)
		print("$",userJPY,"=",GBP,"GBP")
		
#User choice else
	else:
		print("Error")
		

	
	
currencyconvert()