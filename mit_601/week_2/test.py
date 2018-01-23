x=54
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