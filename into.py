# Python practice

import itertools

letters = ['a', 'b', 'c']
result = itertools.combinations(letters, 2)

for res in result:
	print(res)
