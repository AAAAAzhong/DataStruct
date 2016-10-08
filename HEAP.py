#1/usr/bin/python
#-*-coding:utf-8-*-
import sys
import math

class Heap(object):

	def __init__(self,inputlist):
		self.heaplist = inputlist
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
		self._normal_minheap(self.heaplist)

		return self.heaplist

	@property
	def maxheap(self):
		self._normal_maxheap(self.heaplist)

		return self.heaplist

	#@property
	def fast_minheap(self):
		n = len(self.heaplist)

		for i in xrange(n/2,-1,-1):
			self._sink_min(self.heaplist,i)

		return self.heaplist
		#return Heap(self.heaplist)

	#@property
	def fast_maxheap(self):
		n = len(self.heaplist)
	
		for i in xrange(n/2,-1,-1):
			self._sink_max(self.heaplist,i)

		return self.heaplist
		#return Heap(self.heaplist)
	
	def minheap_insert(self,data):
		self.heaplist.append(data)
	
		n = len(self.heaplist)
		
		k = n
		while k != 0:
			k = k/2
			self._sink_min(self.heaplist,k)

		

	def maxheap_insert(self,data):
		self.heaplist.append(data)

		n = len(self.heaplist)
		
		k = n
		while k!=0:
			k = k/2
			self._sink_max(self.heaplist,k)

	def _pop(self,inmode='max'):
	
		n = len(self.heaplist)
		if n > 1:
			temp = self.heaplist[0]
			self.heaplist[0] = self.heaplist.pop()
	
			
			if inmode == 'max':

				while n!=0:
					n = n/2
					self._sink_max(self.heaplist,n)

			else:
				
				while n!=0:
					n = n/2
					self._sink_min(self.heaplist,n)
		else:
			temp = self.heaplist.pop()
			
		return temp

	def pop(self,mode):
		return self._pop(inmode=mode)
		
		
		

def main():
	inlist = [i for i in xrange(1,10,1)]
	inlist2 = [i for i in xrange(1,11,1)]
	inlist3 = [2,3,1,4,6,2,7,1,4,8,92,45,26,73]
	#test = Heap(inlist)
	
	#print "minheap","."*30
	#for i in test.minheap:
	#	print i
	#
	#print "fastminheap","."*30
	#for i in test.fast_minheap:
	#	print i

	#print "maxheap","."*30
	#for i in test.maxheap:
	#	print i

	#print "fastmaxheap","."*30
	#for i in test.fast_maxheap:
	#	print i

	#test.minheap_insert(11)
	#print test.minheap

	#test.maxheap_insert(11)
	#print test.maxheap
	maxheap = Heap(inlist3)
	maxheap.fast_maxheap()
	while maxheap.heaplist:
		print maxheap.pop("max")

	#for i in xrange(5): print test.pop("max")

if __name__ == '__main__':

	main() 
