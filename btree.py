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
		return 
		
	def delete(self,root,value):
		if(value<(root.value)):
			root.lchild=self.delete(root.lchild,value)
		elif(value>(root.value)):
			root.rchild=self.delete(root.rchild,value)
		else:
			if(root.lchild is None):
				temp=root.rchild
				root=None
				return temp
			elif(root.rchild is None):
				temp=root.lchild
				root=None
				return temp
			else:
				temp=self.find_min(root.rchild)
				self.delete(root.rchild,temp.value)
				root.value=temp.value
				root.rchild=self.delete(root.rchild,temp.value)
				return root
	def find_min(self,root):
		temp=root
		if temp.lchild is None:
			return temp
		else:
			return self.find_min(temp.lchild)
		
	
	def find(self,root):
		temp=root
		print("Find temp: "+str(temp.value))
		print("Temp->Lchild: "+str(temp.lchild.value))
		print("Temp->Lchild->Lchild :"+str(temp.lchild.lchild.value))
		while(temp.lchild.lchild is not None):
			temp=temp.lchild
		if(temp.rchild is not None):
			k=Node(temp.rchild.value)
			temp.rchild=None
			return k
		else:
			k=Node(temp.value)
			temp=None
			return k
btree=BTree()
btree.insert(None,15)
root=btree.root

btree.insert(root,7)
btree.insert(root,8)
btree.insert(root,4)
btree.insert(root,3)
btree.insert(root,5)
btree.insert(root,9)
print("Displaying Elements in order: ")
btree.disp(root)
btree.delete(root,7)

print("Displaying Elements in order: ")
btree.disp(root)
