#!/usr/local/bin/python
#-*-coding:utf-8-*-

class Heapnode(object):
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def __str__(self):
		return '{}'.format(self.data)

class Heap(object):

	def __init__(self):
		self._heaplist = [float("inf")]
		self._heapnum = 0
		#self._parentidx = 0
		#self._parentlist = [float("inf")]

	@property
	def heaplist(self):
		return self._heaplist

	@heaplist.setter
	def heaplist(self,data):
		self._heaplist.append(data)
		self._heapnum += 1

	def _update(self):
		
		r = self._heapnum
		
		while r > 1:
			parent = self._heapnum/2
			
			parentvalue = self._heaplist[parent]
			childvalue = self._heaplist[r]

			if parentvalue < childvalue:
				self._heaplist[parent] = childvalue
				self._heaplist[r] = parentvalue	 

			r -= 1	
		
	def create_heap(self):
		self._queue = []

		for heapdata in self.heaplist:
			if not self._queue:
				self.root = Heapnode(heapdata)
				self._queue.append(self.root.left)
				self._queue.append(self.root.right)
			
			if self._queue:
				rootchild = self._queue.pop(0)
				rootchild = Heapnode(heapdata)
				self._queue.append(rootchild.left)
				self._queue.append(rootchild.right)
		
	def _insert(self,data):
		self.heaplist = data

	def insert(self,data):

		if type(data) == type([]):
			for i in data:
				self._insert(i)

		else:
			self._insert(data)

		self._update()

		self.create_heap()

	def _preorder(self,root):
		if root:
			yield root
			for l in self._preorder(root.left): yield l
			for r in self._preorder(root.right): yield r

	def preorder(self):
		return self._preorder(self.root)
	
def main():
	test = Heap()
	test.insert([i for i in range(1,10)])	
	print test.heaplist
	for i in test.preorder(): print i

if __name__ == '__main__':

	main()
		
			

