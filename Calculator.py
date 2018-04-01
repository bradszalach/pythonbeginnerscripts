#Calculator.py
#Scripted by Brad Szalach
#Adds, Subtracts, Multiplies, and Divides



#Function add num1 and num2
def add(num1, num2):
	return num1 + num2

#Function subtracts num1 and num2
def sub(num1, num2):
	return num1 - num2

#Function multiplies num1 and num2
def mul(num1, num2):
	return num1 * num2

#Function divides num1 and num2
def div(num1, num2):
	return num1 / num2
	
def main():
	operation = input("What do you want to do? +,-,*,/ :")
	if(operation != '+' and operation != '-' and operation != '*' and operation != '/'):
		print("Invalid option")
	else:
		num1 = int(input("Enter First Number: "))
		num2 = int(input("Enter Second Number: "))
	if(operation == '+'):
		print(add(num1, num2))
	elif(operation == '-'):
		print(sub(num1, num2))
	elif(operation == '*'):
		print(mul(num1, num2))
	elif(operation == '/'):
		print(div(num1, num2))
		
		
main()		