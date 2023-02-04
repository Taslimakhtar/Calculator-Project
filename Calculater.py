#Calculater.py
import sys

print("=========Mini Calculator========")
while(True):
	try:
		print("\n")
		print("-"*60)
		num1=float(input("Enter First Number Here: "))
		num2=float(input("Enter Second Number Here: "))
		print("\n")
		print("*"*60)
		print("Press 1 for Addition (+) \nPress 2 for Subtraction (-) \nPress 3 for Division (/) \nPress 4 for Multiplication (*)")
		print("*"*60)
		ch=int(input("Enter your choice here: "))
		if ch==1:
			print("-"*60)
			print("You have choosen for Addition")
			print("\t{}".format(num1+num2))
			print("-"*60)
		elif ch==2:
			print("-"*60)
			print("You have chossen for Subtraction")
			print("\t{}".format(num1-num2))
			print("-"*60)
		elif ch==3:
			print("-"*60)
			print("You have choosen for Division")
			print("\t{}".format(num1/num2))
			print("-"*60)
		elif ch==4:
			print("-"*60)
			print("you have choosen for Multiplication")
			print("\t{}".format(num1*num2))
			print("-"*60)
		else:
			print("\n")
			print("-"*60)
			print("Please enter the correct option !!!")
			print("-"*60)
		nu=input("\nDo you want to Calculate more:YES/NO ")
		if(nu.lower()=="no"):
			print("\nThanx for using \U0001F60A")
			sys.exit()
	except ValueError:
		print("\nPlease don't enter Alphanumrical or Special symbol,\nPlease try again!!!")