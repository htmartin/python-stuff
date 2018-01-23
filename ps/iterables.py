#!/usr/bin/env python

words='Why sometimes I have believed as many as six impossible things before breakfast!'.split()


lengths=[]
for word in words:
	lengths.append(len(word))




from math import factorial

#list comprehension
f=[len(str(factorial(x))) for x in range(20)]

#set comprehension
s={len(str(factorial(x))) for x in range(20)}

#dictionary comprehension
from pprint import pprint as pp

country_to_capital = {'United Kingdom': 'London',
                      'Brazil': 'Brazilia',
                      'Morocco':'Rabat',
                      'Sweden':'Stockholm',}

capital_to_country = {capital: country for country, capital in country_to_capital.items()}

words=['hi','hello','foxtrot','hotel']

{ x[0]:x for x in words }

#iterators
iterable = ['Spring', 'Summer','Fall','Winter']
iterator=iter(iterable)
next(iterator)

def first(iterable):
	iterator=iter(iterable)
	try:
		return next(iterator)
	except StopIteration:
		raise ValueError("iterable is empty")

first(['1st','2nd','3rd'])













