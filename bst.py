#!/usr/local/bin/python
#-*-coding:utf-8-*-

class BinaryTree(object):

	#define attr of BinaryTree
	def __init__(self,data):
		self.data = data
		self._left = None
		self._right = None
	
	@property
	def left(self):
		return self._left

	@left.setter
	def left(self,node):
		self._left = node
		
	@property
	def right(self):
		return self._right

	@right.setter
	def right(self,node):
		self._right = node

	def __str__(self):
		return '{}'.format(str(self.data))

	def insert(self,root,data):
		if not root:
			return BinaryTree(data)
		else:
			if data < root.data:
				if root.left:
					self.left = self.insert(root.left,data)
				else:
					root.left = BinaryTree(data)

			else:
				if root.right:
					self.right = self.insert(root.right,data)
				else:
					root.right = BinaryTree(data)
			return root
		
	def remove(self,root,data):
		if not root:
			print "Error, root does not exists"
			pass
		elif data == root.data:
			if not root.left or not root.right:
				root = root.left or root.right
			else:
				next = root.right

				while next.left:
					next = next.left
				
				root.data = next.data
				root.right = self.remove(root.right,next.data)

		elif data < root.data:
			self.remove(root.left,data)

		else:
			self.remove(root.right,data)

		return root
			
	def preorder(self,root):
		if root:
			yield root
			for l in self.preorder(root.left): yield l
			for r in self.preorder(root.right): yield r

	def inorder(self,root):
		if root:
			for l in self.inorder(root.left): yield l
			yield root
			for r in self.inorder(root.right): yield r

	def postorder(self,root):
		if root:
			for l in self.postorder(root.left): yield l
			for r in self.postorder(root.right): yield r
			yield root

def main():
	test = BinaryTree(4)
	for i in [2,7,1,3,6,9]: test.insert(test,i)
	for p in test.postorder(test): print p

if __name__ == '__main__':

	main()
	
