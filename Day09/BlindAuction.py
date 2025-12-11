# A small python program simuling secret auction
import os

finish = False
bidder_list = {}

print("Welcome to the secret auction program")

while finish == False:
	name = input("What is your name ? : ")
	bid = int(input("What is your bid ? : $"))
	if name in bidder_list:
		print(f"{name} is already taken, please take another one.")
		continue
	bidder_list[name] = bid
	
	other_bidder = input("Is there another bidder ? Type 'yes' or 'no'. : ").lower()
	if other_bidder == "no":
		finish = True
	os.system('clear')
	print("\n")

max_bid = 0
max_bidder = []
for key in bidder_list:
	if bidder_list[key] > max_bid:
		max_bid = bidder_list[key]
		max_bidder += key
	elif bidder_list[key] == max_bid:
		max_bidder += key
if len(max_bidder) > 1:
	print("There is a tie auction. Please run the program again")
else:
	print(f"{max_bidder} win the auction for {max_bid}$")