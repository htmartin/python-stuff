
x = 12

if x%2==0:
	print('')
	print('even')
else: 
	print('')
	print('odd')

print('Done with condiditonal')

#While Loops
#while this condition is true, do each of the things in the loop in order until the condition isn't true any longer

n = input('You are in the Lost Forest. Go Left or Right? ')
while n == 'right':
	n = input('You are in the Lost Forest. Go Left or Right? ')
print ('You got out of the Lost Forest!')


n = 0

while (n<5):
	print(n)
	n = n+1

n=2
while (n < 11):
	print(n)
	n = n+2
else:
	print('Goodbye!')

print("Hello!")
n=10
while (n > 0):
	print(n)
	n = n-2
	


#This has issues: if you forget to increment, it goes on forever etc
#so instead use for loop, a shortcut

for n in range(5): #this means 0,1,2,3,4
	print(n)

mysum = 0

for i in range(7,10):#this range is 7,8,9
	mysum +=i #+= is add to
print(mysum)

for i in range(5,11,2):
	mysum += i

print(mysum)


mysum = 0

for i in range(5,11,2):
	mysum +=i 
	if mysum == 5:
		break
print(mysum)





#so that loop stops at 5, so this evaluates to 5

#Write a piece of Python code that prints out the string 'hello world' 
#if the value of an integer variable, happy, is strictly greater than 2.


3. Write a while loop that sums the values 1 through end, 
inclusive. end is a variable that we define for you. 
So, for example, if we define end to be 6, your code should print out the result:
21
which is 1 + 2 + 3 + 4 + 5 + 6.

For problems such as these, do not include input statements or 
define variables we will provide for you. 
Our automating testing will provide values so write your code 
in the following box assuming these variables are already defined.

end = 4

result = 0
i = 1
while i <= end:
	result += i
	i += 1
print(result)

1. Convert the following code into code that uses a for loop.

n=2
while (n < 11):
	print(n)
	n = n+2
else:
	print('Goodbye!')

mysum=0
for i in range(2,11,2):
	print(i)
	mysum +=i
print('Goodbye!')


2. Convert the following code into code that uses a for loop.

print("Hello!")
n=10
while (n > 0):
	print(n)
	n = n-2

print("Hello!")
mylist=[10,8,6,4,2]
for i in mylist:
	print(i)

3. Convert the following code into code that uses a for loop.
Write a for loop that sums the values 1 through end, 
inclusive. end is a variable that we define for you. 
So, for example, if we define end to be 6, your code should print out the result:
21
which is 1 + 2 + 3 + 4 + 5 + 6.

end = 4

result = 0
i = 1
while i <= end:
	result += i
	i += 1
print(result)

end = 4
mysum = 0
for i in range(1,end+1):
	mysum +=i 
print(mysum)

x = int(input('Enter an integer: '))
ans=0
while ans**3<x:
	ans = ans +1
if ans**3 !=x:
	print(str(x) + ' is not a perfect cube')
else:
	print('Cube root of ' + str(x) + ' is ' + str(ans))

in for loop version

cube=8
for guess in range(cube+1):
	if guess**3==cube:
		print('Cube root of ', cube , ' is ' , guess)
	else:
		print('Cube root of ' + str(cube) + ' is ' + str(guess))



