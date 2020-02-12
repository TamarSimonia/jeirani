"""1. Rock, Paper, Scissors Game:
შექმენით Rock, Paper, Scissors ( ჯეირანი ) თამაში. თამაში სულ გაქვთ სამი ასარჩევი ვარიანტი [ Rock, Paper, Scissors ]. 
მომხმარებელს კონსოლიდან შემოაქვს რომელიმე და კომპიუტერი შემთხვევითობით ( Random ) პასუხობს პასუხს. 
ყურადღება მიაქციეთ მნიშვენოლებების მინიჭებას რომ მაგალითად მაკრატელი ქაღალდს ჭრის და ამ შემთხვევაში მაკრატელი იგებს"""

import random

while True: 
	print("choice:")
	choice = str(input())
	choice = choice.lower()

	print("My choice is", choice)

	choices = ["rock", "paper", "scissors"]

	computer_choice = random.choice(choices)

	print("Computer choice is", computer_choice)
	if choice in choices:
		if choice == computer_choice:
			print("it is a tie")
		if choice == "rock":
			if computer_choice == "paper":
				print("you lose!, sorry ")
			elif computer_choice == "scissors":
				print("You win! congrats :D ")
		if choice == "paper":
			if computer_choice == "scissors":
				print("you lose!, sorry ")
			elif computer_choice == "rock":
				print("You win! congrats :D ")
		if choice == "scissors":
			if computer_choice == "rock":
				print("you lose!, sorry ")
			elif computer_choice == "paper":
				print("You win! congrats :D ")
	else:
		print("invalid choice, try again")

	print()

