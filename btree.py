class Node:
	def __init__(self,data):
		self.value=data
		self.lchild=None
		self.rchild=None
	

class BTree:
	def __init__(self):
		self.root=None
	
	def insert(self,parent,value):
	
		if(self.root is None):
			self.root=Node(value)
			print("Inserted Root Element")
		else:
			print("Parent :"+str(parent.value)+" Child : "+str(value))		
			temp=parent
			if(temp.value)>value:
				if(temp.lchild is None):
					temp.lchild=Node(value)
				else :
					temp=temp.lchild
					self.insert(temp,value)
			else:
				if(temp.rchild is None):
					temp.rchild=Node(value)
				else :
					temp=temp.rchild
					self.insert(temp,value)
	
	def disp(self,root):
		temp=root
		if(temp is None):
			return
		self.disp(temp.lchild)
		print(temp.value)		
		self.disp(temp.rchild)

btree=BTree()
btree.insert(None,15)
root=btree.root
btree.insert(root,10)
btree.insert(root,7)
btree.insert(root,8)
btree.insert(root,20)
btree.insert(root,19)
btree.insert(root,17)
btree.insert(root,22)
print("Displaying Elements in order: ")
btree.disp(root)
