#!/usr/bin/python

def binary_search(min, max, exp):
	while True:
		avg = (min + max) / 2.0
		print "{0}, {1}, {2}".format(min, max, avg)
		if avg > exp:
			max = avg
		else:
			min = avg
		if abs(max - min) < 0.25:
			return int(round(min))

for x in range(1, 100):
	exp = binary_search(1, 100, x)
	print "binary_search(1, 100, {0}) = {1}".format(x, exp)
	assert exp == x
