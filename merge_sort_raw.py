#!/usr/bin/python

def merge(A, start, mid, end):
	# print 'merge({0}, {1}, {2}, {3})'.format(A, start, mid, end)
	left = A[start:mid + 1]
	right = A[mid + 1: end + 1]
	i = 0
	j = 0
	k = start
	# print 'left: {0}\nright: {1}\n'.format(left, right)
	while i < mid - start + 1 and j < end - mid:
		# print i, j
		if left[i] < right[j]:
			A[k] = left[i]
			i = i + 1
		else:
			A[k] = right[j]
			j = j + 1
		k = k + 1
		# print 'S1: ' + str(A)
	while i < mid - start + 1:
		A[k] = left[i]
		i = i + 1
		k = k + 1
	# print 'S2: ' + str(A)
	while j < end - mid:
		A[k] = right[j]
		j = j + 1
		k = k + 1
	# print 'S3: ' + str(A)

def merge_sort(A, start, end):
	'''
	Merge sort the array A with elements [start, end]
	'''
	# print 'merge_sort({0}, {1}, {2})'.format(A, start, end)
	if start < end:
		mid = (start + end) / 2
		merge_sort(A, start, mid)
		merge_sort(A, mid + 1, end)
		merge(A, start, mid, end)


#data = [1]
#merge_sort(data, 0, 0)
#print data

import random

for x in range(1000):
	old_data = range(1000)
	new_data = old_data[:]
	random.shuffle(new_data)
	merge_sort(new_data, 0, len(new_data) - 1)
	assert old_data == new_data, 'foo'
	print 'good'
