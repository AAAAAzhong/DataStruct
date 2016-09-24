#!/usr/local/bin/python
#-*-coding:utf-8-*-

class AvlNode(object):

	def __init__(self,data):
		self.data = data
		self._left = None
		self._right = None
		self._height = 0
		self._factor = 0

	@property
	def height(self):
		return self._height

	@property
	def factor(self):
		return self._factor

	@property
	def left(self):
		return self._left

	@left.setter
	def left(self,node):
		self._left = node
		
		self._update()

	@property
	def right(self):
		return self._right

	@right.setter
	def right(self,node):
		self._right = node

		self._update()

	def _update(self):
		l = self.left._height if self.left else -1
		r = self.right._height if self.right else -1

		self._height = 1 + max(l,r)
		self._factor = r-l

	def __str__(self):
		return '{}({},{})'.format(str(self.data),self.height,self.factor)

class AvlTree(object):

	def __init__(self,data=None):
		self.root = None
		
		if data:
			self.insert(data)

	def _insert(self,root,data):
		if not root:
			return AvlNode(data)

		if data < root.data:
			root.left = self._insert(root.left,data)

		else:
			root.right = self._insert(root.right,data)

		return self._balance(root)

	def insert(self,data):
		if type(data) == type([]):
			for d in data:
				self.insert(d)
		
		else:
			self.root = self._insert(self.root,data)
			
	def _remove(self,root,data):
		if root:
			if data == root.data:
				if not root.left or root.right:
					root = root.left or root.right
					
				else:
					next = root.right
					
					while next.left:
						next = next.left

					root.data = next.data
					root.right = self._remove(root.right,next.data)

			elif data < root.data:
				root.left = root._remove(root.left,data)

			else:
				root.right = root._remove(root.right,data)

		return self._balance(root)

	def remove(self,data):
		if type(data) == type([]):
			for d in data:
				self.remove(d)

		else:
			self.root = self._remove(self.root,data)

	def _ll_rotation(self,root):
		next = root.left
		root.left = next.right
		next.right = root

		return next

	def _rr_rotation(self,root):
		next = root.right
		root.right = next.left
		next.left = root

		return next

	def _lr_rotation(self,root):
		root.left = self._rr_rotation(root.left)
		
		return self._ll_rotation(root)

	def _rl_rotation(self,root):
		root.right = self._ll_rotation(root.right)

		return self._rr_rotation(root)

	def _balance(self,root):
		if root:
			if root.factor > 1:
				root = self._rr_rotation(root) if root.right.factor >= 0 else self._rl_rotation(root)

			elif root.factor < -1:
				root = self._ll_rotation(root) if root.left.factor <= 0 else self._lr_rotation(root)

			assert root.factor in [-1,0,1]

		return root

	def _preorder(self,root):
		if root:
			yield root
			for l in self._preorder(root.left): yield l
			for r in self._preorder(root.right): yield r

	def preorder(self):
		return self._preorder(self.root)

	def _inorder(self,root):
		if root:
			for l in self._inorder(root.left): yield l
			yield root
			for r in self._inorder(root,right): yield r

	def inorder(self):
		return self._inorder(self.root)

	def _posorder(self,root):
		if root:
			for l in self._posorder(root.left): yield l
			for r in self._posorder(root.right): yield r
			yield root

	def posorder(self):
		return self._posorder(self.root)

def main():
	test = AvlTree([i for i in xrange(1,100)])
	for i in test.preorder(): print i

if __name__ == '__main__':
	
	main()
	
				

			

