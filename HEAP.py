#1/usr/bin/python
#-*-coding:utf-8-*-
import sys
import math

class Heap(object):

	def __init__(self,inputlist):
		self._heaplist = inputlist
		self.c = 0
	
	def _normal_minheap(self,inlist):
		n = len(inlist)
		
		for i in range(int(math.log(n,2))):

			for j in range(0,n/2):
				k = j*2+2 if j*2+2 < n and inlist[j*2+2] < inlist[j*2+1] else j*2+1

				if inlist[j] > inlist[k]:
					inlist[j], inlist[k] = inlist[k], inlist[j]
				

	def _normal_maxheap(self,inlist):
		n = len(inlist)

		for i in range(int(math.log(n,2))):
	
			for j in range(0,n/2):
				k = j*2+2 if j*2+2 < n and inlist[j*2+2] > inlist[j*2+1] else j*2+1

				if inlist[j] < inlist[k]:
					inlist[j], inlist[k] = inlist[k], inlist[j]

	def _sink_min(self,inlist,root):
		n = len(inlist)
			

		if root*2+1 < n:
			k = root*2+2 if root*2+2 < n and inlist[root*2+2] < inlist[root*2+1] else root*2+1

			if inlist[root] > inlist[k]:
				inlist[root], inlist[k] = inlist[k], inlist[root]

				self._sink_min(inlist,k) 

	def _sink_max(self,inlist,root):
		n = len(inlist)

		if root*2+1 < n:
			k = root*2+2 if root*2+2 < n and inlist[root*2+2] > inlist[root*2+1] else root*2+1

			if inlist[root] < inlist[k]:
				inlist[root], inlist[k] = inlist[k], inlist[root]

				self._sink_max(inlist,k)	

	@property
	def minheap(self):
		self._normal_minheap(self._heaplist)

		return self._heaplist

	@property
	def maxheap(self):
		self._normal_maxheap(self._heaplist)

		return self._heaplist

	@property
	def fast_minheap(self):
		n = len(self._heaplist)

		for i in xrange(n/2,-1,-1):
			self._sink_min(self._heaplist,i)

		return self._heaplist

	@property
	def fast_maxheap(self):
		n = len(self._heaplist)
	
		for i in xrange(n/2,-1,-1):
			self._sink_max(self._heaplist,i)

		return self._heaplist

	def minheap_insert(self,data):
		self._heaplist.append(data)
	
		n = len(self._heaplist)
		
		k = n
		while k != 0:
			k = k/2
			self._sink_min(self._heaplist,k)

		

	def maxheap_insert(self,data):
		self._heaplist.append(data)

		n = len(self._heaplist)
		
		k = n
		while k!=0:
			k = k/2
			self._sink_max(self._heaplist,k)

def main():
	inlist = [i for i in xrange(10,1,-1)]
	test = Heap(inlist)
	
	print "minheap","."*30
	for i in test.minheap:
		print i
	
	print "fastminheap","."*30
	for i in test.fast_minheap:
		print i

	print "maxheap","."*30
	for i in test.maxheap:
		print i

	print "fastmaxheap","."*30
	for i in test.fast_maxheap:
		print i

	test.minheap_insert(11)
	print test.minheap

	test.maxheap_insert(11)
	print test.maxheap

if __name__ == '__main__':

	main() 
