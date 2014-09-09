#!/usr/bin/python

def max_subarray_kadane(A):
	'''
	Use Kadane algorithm to find the max possible sum of subarray of A.
	'''
	if A == None or len(A) == 0: return 0
	max_best = max_here = A[0]
	for x in A[1:]:
		max_here = max(x, max_here + x)		# status i
		max_best = max(max_best, max_here)	# decision i
		print 'max_here = {0}\tmax_best = {1}'.format(max_here, max_best)
	return max_best	

print max_subarray_kadane([-1, -3, -5, -7, -9, 9, -1, 2])
