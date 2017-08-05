def f_to_c(x):
	return (x - 32) * (5/9)

def c_to_f(x):
	return (x * (9/5)) + 32

looper = 0
while looper == 0:
	print("Welcome to Temperature Converter.\n\n")

	x = input("Do you want to convert to celsius or farenheit (C or F)?: ")
	y = int(input("What is the temperature?: "))
	print(" ")

	if x == 'f':
		print(y, "degrees celsius is equal to ",c_to_f(y), " degrees farenheit\n\n\n\n")
	else:
		print(y, "degrees farenheit is equal to ",f_to_c(y), " degrees celsius\n\n\n\n")