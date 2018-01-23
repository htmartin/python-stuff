million_squares=(x*x for x in range(1,10))

from itertools import islice, count
import math


thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
thousand_primes
list(thousand_primes)

any([False, False, True])

all([False, False, True])

any(name == name.title() for name in ['london','New York','sydney'])

all(name == name.title() for name in ['London','New York','Sydney'])

sunday=[12,14,17]
monday=[13,15,16]

for item in zip(sunday,monday):
	print(item)

for sun, mon in zip(sunday,monday):
	print('Average = ', (sun + mon)/2)