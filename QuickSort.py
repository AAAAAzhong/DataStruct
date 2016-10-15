#!/usr/local/bin/python
#-*-coding:utf-8-*-

def QuickSort(inlist):

	right = len(inlist)-1
	left = 0
	r = right
	l = left
	stack = []
	
	def partition(inlist,l,r):
		
		if l >= r:
			return inlist
		
		key = inlist [l]

		while l < r:
			
			while l < r and inlist[r] >= key:
				r -= 1
		
			inlist[l] = inlist[r]
		
			while l < r and inlist[l] <= key:
				l += 1
			
			inlist[r] = inlist[l]

		inlist[l] = key

		return l

	if l >= r:
		return inlist

	else:
		p = partition(inlist,l,r)

		if p-1 > l:
			stack.append(l)
			stack.append(p-1)

		if p+1 < r:
			stack.append(p+1)
			stack.append(r)

		while(stack):
			r = stack.pop()
			l = stack.pop()

			p = partition(inlist,l,r)

			if p-1 > l:
				stack.append(l)
				stack.append(p-1)

			if p+1 < r:
				stack.append(p+1)
				stack.append(r)

		return inlist

if __name__ == '__main__':

	inlist = [i for i in xrange(10,1,-1)]
	print QuickSort(inlist)











