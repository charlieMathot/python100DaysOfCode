#A tresure hunt program with muliple choices

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a crossroad. Where to you want to go ?")
res = input("Type \"left\" or \"right\" : ")

if res == "right":
	print("Game over.")
else:
	print("You've come to a lake.\nDo you want to swim or wait ? ")
	res = input("Type \"swim\" or \"wait\" : ")
	if res == "swim":
		print("Game over.")
	else:
		print("A guy make you cross the lake, now there is 3 doors.\nDo you want to go to the red, the blue or the green one ? ")
		res = input("Type \"red\", \"blue\" or \"green\" : ")
		if res == "red":
			print("Game over.")
		elif res == "blue":
			print("Game over.")
		else:
			print("You found the treasure, GG.")

#Yeurks code, happy to see the functions in the next day