
import random

def get_random_word():
	words = ['pizza', 'cheese', 'apples']
	word = words[random.randint(0, len(words)-1)]
	return word

def show_word(word):
	for character in word:
		print(character, '', end = '')
	print('')

def get_guess():
	print('Enter a letter: ')
	return input()

def process_letter(letter,secret_word,blanked_word):
	result = False

	for i in range(0,len(secret_word)):
		if secret_word[i]==letter:
			result = True
			blanked_word[i] = letter
	return result

def print_strikes(number_of_strikes):
	for i in range(0, number_of_strikes):
		print('X', end='')
	print('')

def play_word_game():
	strikes = 0
	max_strikes = 3
	playing = True
	
	word = get_random_word()
	blanked_word = list('_'*len(word))



	while playing:
		show_word(blanked_word)
		letter = get_guess()
		found=process_letter(letter,word,blanked_word)

		if not found:
			strikes +=1
			print_strikes(strikes)

		if strikes >=max_strikes:
			playing=False

		if not "_" in blanked_word:
			playing = False

	if strikes >= max_strikes:
		print('Loser')
	else:
		print('Winner')

print('Game started')
play_word_game()
print('Game over')

#top down design - name a function that achieves your abstraction


#randomly pick a word from a word list
#separate the letters
#count the letters
#some sort of [0,1,2,3] representation of the letters
#dict? e.g., and goes to {a:[0], n[1],d:[2]}
#kep track of the number of letters in the word
#print the number of spaces as _ with spaces between that are in the word

#print('Enter a letter:')
#guess = input()

#if guess is in the word
#	where is guess positionally 