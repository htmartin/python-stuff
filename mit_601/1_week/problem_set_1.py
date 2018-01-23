Problem 1
10.0 points possible (graded)
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained 
in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:

>>>Number of vowels: 5


s='strghaaaqvb'
vowels=['a','e','i','o','u']
count=0
for letter in s:
	if letter in vowels:
		count+=1
print('Number of vowels: ' + str(count))







Problem 2
10.0 points possible (graded)

Assume s is a string of lower case characters.

Write a program that prints the number of times the 
string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print:
>>>Number of times bob occurs is: 2

s = 'azcbobobegghakl'
#MY ANSWER
count=0
index = 0
while index < len(s):
    index = s.find('bob', index)
    if index == -1:
        break
    index+=1
    count+=1
print('Number times bob occurs is: ' + str(count))
#END MY ANSWER


s = 'azcbobobegghakl'
count=0
for number of times 'bob' in s:
	count+=1
print('Number times bob occurs is: ' + str(count))


#define the for loop
for each letter in s,
	start with that letter and go 2 letters out
		does that == bob?
			if yes, 
				count it

I want for index 0 to -1:
	text.find('bob', index)

for char in s[0:-1]:

s = 'azcbobobegghakl'
count=0
i = 0
while i < len(s): 
	for i in s[i:i+3]:
		count+=1
	print(count)

for char in s[i:i+3]:

for i in text:
	print(i)

for i in text:
	if str(text[i:i+3]) == "bob":
		print(bob)

>>> str(text[2:5])
'cbo'

>>> list(text)
['a', 'z', 'c', 'b', 'o', 'b', 'o', 'b', 'e', 'g', 'g', 'h', 'a', 'k', 'l']
>>> i=1
>>> text[i:i+3]
['z', 'c', 'b']
>>> 

text = 'azcbobobegghakl'
text = list(text)
i=0
for item in text:
	if text[i:i+3] == ['b','o','b']:
		print(item)


text = 'azcbobobegghakl'
count=0
i=0
for item in text:
	if str(text[i:i+3]) == 'bob':
		i+=1
		count+=1
print(count)


#mess
count=0
text = 'azcbobobegghakl'
index = 0
while index < len(text):
    index = text.find('bob', index)
    count+=1
    if index == -1:
        break
    print('bob found at', index)
    index += 1 # +2 because len('ll') == 2>>> 
print(count)
#this prints 3 because it is at 3rd index that bob is 1st found

#try again
count=0
text = 'azcbobobegghakl'
index = 0
while index < len(text):
	for i in text:
    	index = text.find('bob', index)
    	count+=1
    	if index == -1:
        	break
    	print('bob found at', index)
    	index += 1 # +2 because len('ll') == 2>>> 
print(count)



#their code:
s = 'azcbobobegghakl'
count=0
index = 0
while index < len(s):
    index = s.find('bob', index+1)
    if index == -1:
        break
    count+=1
print('Number times bob occurs is: ' + str(count))


for index in range([-1])


>>> text = 'Allowed Hello Hollow'
>>> index = 0
while index < len(text):
    index = text.find('ll', index)
    if index == -1:
        break
    print('ll found at', index)
    index += 2 # +2 because len('ll') == 2

#define the for loop
for any possible (forwards) combination of (3) letters:
	if it equals 'bob':
		count+=1

#possible solution: 
import itertools
s = 'gbobhvbob'
my_string='bob'
count=0
combinations = list("".join(string) for string in itertools.combinations(s,3)) 
for element in combinations:
	if element == 'bob':
		count+=1
count = int(count/2)
print('Number times bob occurs is: ' + str(count))
#combinations = list("".join(string) for string in itertools.combinations(s,3)) 
#perm = list(set(perm)) # permuted list without duplicates
#if you make into a set, there will be no duplicate elements and we want to count the duplicates, but not the number all possible combinations generates






for s[0:-1]:
	if my_string in s:
		count+=1
#this will check by letter, not groups of letters


for s[start:end:3]:
#this means every 4th letter, check by letter, I want to check by groups of letters







Warning: hard

