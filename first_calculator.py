#calculator program

#this variable tells the loop whether it should loop or not.
# 1 means loop. anything else means don't loop.

loop = 99

#this variable holds the user's choice in the menu:


while loop == 99:
#print what options you have
	print (" ")
	print (" ")
	print ("Welcome to calculator.py")
	print ("your options are:")
	print (" ")
	print ("1) Addition")
	print ("2) Subtraction")
	print ("3) Multiplication")
	print ("4) Division")
	print ("5) Quit calculator.py")
	print (" ")

	choice = int(input("Choose your option: "))

	if choice == 1:
		add1 = float(input("Add this: "))
		add2 = float(input("to this: "))
		print (add1, "+", add2, "=", add1 + add2)
	elif choice == 2:
		sub2 = float(input("Subtract this: "))
		sub1 = float(input("from this: "))
		print (sub1, "-", sub2, "=", sub1 - sub2)
	elif choice == 3:
		mul1 = float(input("Multiply this: "))
		mul2 = float(input("with this: "))
		print (mul1, "*", mul2, "=", mul1 * mul2)
	elif choice == 4:
		div1 = float(input("Divide this: "))
		div2 = float(input("by this: "))
		print (div1, "/", div2, "=", div1 / div2)
	elif choice == 5:
		loop = 0
	
print ("Thank you for using calculator.py!")
