cannot say
s[0] = 'y' #for s = 'whateverstring', it's immutable

s = 'abcdefgh'
for index in range(len(s)):
	if s[index] == 'i' or s[index] == 'u':
		print('There is an i or a u.')

same as

for char in s:
	if char == 'i' or char == 'u':
		print('There is an i or a u.')





an_letters = ' aefhilmnorsxAEFHILMNORXS'

word = input("I will cheer for you! Enter a word: ")
times = int(input('Enthusiasm level (1-10): '))
i = 0

while i < len(word):
	char = word[i]
	if char in an_letters:
		print('Give me an ' + char + '!' + char)
	else:
		print('Give me a ' + char + '!' + char)
	i+=1
print('What does that spell?')
for i in range(times):
	print(word, '!!!')


#Approximate Solutions

cube = 27
epsilon = 0.01
guess 0.0
increment = 0.0001
num_guesses = 0
while abs(guess**3-cube) >=epsilon:
	guess +=increment
	num_guesses +=1
print('num_guesses =', num_guesses)
if abs(guess**3-cube)>=epsilon:
	print('Failed on cube root of', cube)
else:
	print(guess, 'is close to the cube root of',cube)

#That runs a bunch (30K) of times. So, make increment smaller (now can get inf loop or the 'failed' answer)

cube = 29
epsilon = 0.01
guess =0.0
increment = 0.01
num_guesses = 0
while abs(guess**3-cube) >=epsilon:
	guess +=increment
	num_guesses +=1
print('num_guesses =', num_guesses)
if abs(guess**3-cube)>=epsilon:
	print('Failed on cube root of', cube)
else:
	print(guess, 'is close to the cube root of',cube)

#That gives too big a step, so end up in inf loop

cube = 29
epsilon = 0.01
guess =0.0
increment = 0.01
num_guesses = 0
while abs(guess**3-cube) >=epsilon and guess <=cube:
	guess +=increment
	num_guesses +=1
print('num_guesses =', num_guesses)
if abs(guess**3-cube)>=epsilon:
	print('Failed on cube root of', cube)
else:
	print(guess, 'is close to the cube root of',cube)

#That fails but doesn't run forever


#Exercise after that video

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) < epsilon:
        break
    else:
        guess += step


if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))

If this code is executed, it will print succeeded: 4.9999999999998 (or succeeded: 5.0). (Remember floating point errors?)
Now suppose we try the following

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))

Select the answer that best describes what occurs when the above code is executed:

Script successfully completes, and prints out succeeded: 4.9999999999998 (or succeeded: 5.0)
Script successfully completes, but prints out failed
Script successfully completes, but prints out succeeded: followed by some number not really close to 5.0
*Script enters an infinite loop and never terminates



Next question:
Now try:

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))


Select the answer that best describes what occurs when the above code is executed:

*Script successfully completes, and prints out succeeded: 4.9999999999998 (or succeeded: 5.0)
Script successfully completes, but prints out failed
Script successfully completes, but prints out succeeded: followed by some number not really close to 5.0
Script enters an infinite loop and never terminates


Finally, let's use the same code as immediately above
but change the first line to x = 23. 
Note that the square root of 23 is roughly 4.7958.

Select the answer that best describes what occurs when the modified code is executed:


Script successfully completes, and prints out succeeded: 4.9999999999998 (or succeeded: 5.0)
*Script successfully completes, but prints out failed
Script successfully completes, but prints out succeeded: followed by some number not really close to 5.0
Script enters an infinite loop and never terminates



"Bisection Search"

x=25
epsilon=0.01
num_guesses=0
low=0.0
high=x
ans = (high+low)/2.0

while abs(ans**2 - x) >=epsilon:
	print('low = ' + str(low) + ' high = ' +str(high) + ' answer = ' +str(ans))
	num_guesses+=1
	if ans**2 < x:
		low = ans
	else:
		high = ans
	ans = (high+low)/2.0
print('num_guesses = ' + str(num_guesses))
print(str(ans) + ' is close to the square root of ' + str(x))


x=27
epsilon=0.01
num_guesses=0
low=0.0
high=x
ans = (high+low)/2.0

while abs(ans**3 - x) >=epsilon:
	print('low = ' + str(low) + ' high = ' +str(high) + ' answer = ' +str(ans))
	num_guesses+=1
	if ans**3 < x:
		low = ans
	else:
		high = ans
	ans = (high+low)/2.0
print('num_guesses = ' + str(num_guesses))
print(str(ans) + ' is close to the cube root of ' + str(x))


#bisection search works when value of function varies monotonically with input
#guess converges on log(sub2)N steps

#This only works for 0<n<1 - why?
#challenges
#1 modify to work with negative cubes
#2 modify to work with x < 1 (ie fractions)
#if x < 1 change the search space to look from  0 to -x

bisection search reduces computation time

Exercise: guess my number

In this problem, you'll create a program that guesses a secret number!

The program works as follows: 
you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). 
The computer makes guesses, and you give it input - is its guess too high or too low?
Using bisection search, the computer will guess the user's secret number!

Here is a transcript of an example session:

Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 75?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 87?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 81?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 84?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 82?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 83?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
Game over. Your secret number was: 83

I think this is part 2
Note: your program should use input to obtain the user's input! 
Be sure to handle the case when the user's input is not one of h, l, or c.

When the user enters something invalid, 
you should print out a message to the user explaining you did not understand their input. 
Then, you should re-ask the question, and prompt again for input. 

For example:

Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. y
Sorry, I did not understand your input.
Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c











