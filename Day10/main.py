def add(n1, n2):
	return n1 + n2

def sub(n1, n2):
	return n1 - n2

def multiply(n1, n2):
	return n1 * n2

def divide(n1, n2):
	return n1 / n2

operations = {
	"+": add,
	"-": sub,
	"*": multiply,
	"/": divide,
}

def main():
	res = float("-inf")
	finish = False
	
	while finish == False:
		
		if res == float("-inf"):
			res = first_operation()
			print(res)
		else:
			res = operation(res)
			print(res)

		finish = ask_for_termination(res)

def first_operation():
	n1 = input("What's the first number : ")
	n1 = float(n1)
	
	print("+\n-\n*\n/")
	sign = " "
	while sign not in "+-/*" or len(sign) != 1:
		sign = input("Pick an operation : ")
	
	n2 = input("What's the next number : ")
	n2 = float(n2)

	print(f"{n1} {sign} {n2} = ", end="")
	return operations[sign](n1, n2)

def operation(n1):
	print("+\n-\n*\n/")
	sign = " "
	while sign not in "+-/*" or len(sign) != 1:
		sign = input("Pick an operation : ")
	
	n2 = input("What's the next number : ")
	n2 = float(n2)

	print(f"{n1} {sign} {n2} = ", end="")
	return operations[sign](n1, n2)

def ask_for_termination(n):
	res = " "
	
	while res != "y" and res != "n":
		res = input(f"Type \'y\' to continue calculating with {n}, or type \'n\' to end the program : ").lower()
	
	return res == "n"




if __name__ == "__main__":
	main()