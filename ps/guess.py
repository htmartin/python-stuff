import random

print('Hello, what is your favorite number?')
number = input()

print('Your favorite number is ' + number)

min_number = 1
max_number = 100
magic_number = random.randint(min_number, max_number)

message = "The magic number is between {0} and {1}."
print(message.format(min_number, max_number))

found = False

while not found:
	print("Guess what it is?")
	guess = input()
	if int(guess) == magic_number:
		found = True
	elif int(guess) > magic_number:
		print("Too high.")
	elif int(guess) < magic_number:
		print("Too low.")
print("You got it.")

