import random
player1 = random.randrange(1000, 10000)

n = int(input("Guess the 4 digit number:"))
if(n == player1):
	print("You're a Mastermind!")
else:
	Turns = 0
	while(n != player1):
		Turns += 1

		count = 0
		n = str(n)
		player1 = str(player1)
		correct = []
		for i in range(0, 4):
			
			if(n[i] == player1[i]):
				count += 1
				correct.append(n[i])
			else:
				continue
		if (count < 4) and (count != 0):
			print("Not quite the number. But you did get ",
				count, " digit(s) correct!")
			print("Also these numbers in your input were correct.")

			for k in correct:
				print(k, end=' ')

			print('\n')
			print('\n')
			n = int(input("Enter your next choice of numbers: "))
		elif(count == 0):
			print("None of the numbers in your input match.")
			n = int(input("Enter your next choice of numbers: "))

	if n == player1:
		print("You've become a Mastermind!")
		print("It took you only", Turns, "tries.")
