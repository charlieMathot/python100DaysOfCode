# The hangman game written in python
import WordList
import random

# Game initialisation
game_over = False
user_lives = 6
letter_list = []
choice_list = []
word = random.choice(WordList.words)
placeholder = ""

# Game loop
print("Welcome to the hangman game !\n")
print(f"user_lives = {user_lives}")
while game_over == False:
	display = ""
	letter = input("Choose a letter : ").lower()

	if letter in choice_list:
		print("\nYou already picked that letter")
		print(f"user_lives = {user_lives}")
		print(f"{display}\n")
		continue
	elif letter in word:
		letter_list.append(letter)
		choice_list.append(letter)
		print(f"\nRight guess, {letter} is in the word")
	else:
		print(f"\nWrong guess, {letter} is not in the word")
		choice_list.append(letter)
		user_lives -= 1
	
	for i in range(len(word)):
		if word[i] in letter_list:
			display += word[i]
		else:
			display += "_"
	
	print(f"{display}\n")
	print(f"user_lives = {user_lives}")
	
	if user_lives == 0:
		game_over = True
		print(f"You lost the game, the word was {word}")
	if "_" not in display:
		game_over = True
		print("You won the game")
