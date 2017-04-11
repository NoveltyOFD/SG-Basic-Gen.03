class Node:
	def __init__(self,val):
		self.info = val
		self.left = None
		self.right = None

	def insert(self,val):
		if (val<self.info):
			if self.left is None:
				self.left = Node(val)
			else:
				self.left.insert(val)
		elif (val>self.info):
			if self.right is None:
				self.right = Node(val)
			else:
				self.right.insert(val)

	def printinorder(self):
		if self.left :
			self.left.printinorder()
		print(self.info, end= " ")
		if self.right :
			self.right.printinorder()

	def printpreorder(self):
		print(self.info, end=" ")
		if self.left :
			self.left.printpreorder()
		if self.right :
			self.right.printpreorder()

	def printpostorder(self):
		if self.left :
			self.left.printpostorder()
		if self.right :
			self.right.printpostorder()
		print(self.info, end=" ")

	def search(self, val):
		if self.info < val:
			if self.right is None:
				return None
			else:
				self.right.search(val)
		elif self.info > val:
			if self.left is None:
				return None
			else:
				self.left.search(val)
		else:
			return True

	def countheigh (self):
		if self.left:
			a = self.left.countheigh() + 1
		elif self.right:
			b = self.right.countheigh() + 1
		if a>b:
			return a
		elif b>a:
			return b 

BT = Node(23)
BT.insert(10)
BT.insert(16)
BT.insert(19)
BT.insert(65)
BT.insert(45)
BT.insert(24)
BT.insert(50)
BT.insert(47)
BT.insert(30)
print("Inorder :")
BT.printinorder()
print()
print("Postorder : ")
BT.printpostorder()
print()
print("Preorder :")
BT.printpreorder()
print()
print(BT.search(23))
print("Heigh :", end= " ")
print(BT.countheigh())