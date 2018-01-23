Problem 3
15.0 points possible (graded)
Assume s is a string of lower case characters.

Write a program that prints the longest substring 
of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print
>>>Longest substring in alphabetical order is: beggh


In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print
>>>Longest substring in alphabetical order is: abc

***he did make a big point of guess and check algorithms, with math, but could that help?
like look for first sub in alphabetical_order
(lexicographic order - search this to see if can help)

s = 'azcbobobegghakl'

longest = []
get substring
	if in alphabetical order:
		if len(next_substring) > last_substring_in_longest:
			replace last_substring_in_list with next_substring


so, could break into 2 loops:
find substrings
check if alpha order and check len, replace in list 

what I do not know:
#how to replace in a list
-need to figure out a way around list[0] for list =[] is an index out of range error
	could start with longest = ['a'] just to have something in there because alpha order substring means substring >1
-do the chars in that substring follow the order of string.ascii_lowercase (regardless of missing values in string constant)?
	some loop where 
	for i in next_substring:
		for i in ascii_lowercase:
			skip over any ascii_lowercase not in next_substring, but check if all next_substring
	*Crap - this is a mess :)



***find next_substring
start with first char in s
check all possible substrings that start with that char
do the chars in that substring follow the order of string.ascii_lowercase (regardless of missing values in string constant)?

***replace last_substring_in_list with next_substring
if len(next_substring) > len(longest[0]):#what if longest is empty? will it check length of empty set?
	del longest[0]
	longest.insert(0, next_substring)
	