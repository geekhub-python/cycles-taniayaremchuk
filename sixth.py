#!/usr/bin/env python3

for a in range(1, 11):
	for b in range(1,11):
		if( ((a*b) - 10) >= 0):
			print(a*b, end = ' |')
		else:
 			print(a*b, end = '  |')
	print()
