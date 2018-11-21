class Node:
	def __init__(self,data):
		self.value=data;
		self.next=None;
		print("Created Node with Value :"+ str(self.value))
		
class Linked :
	def __init__(self):
		self.root=None
		print("Root is none")

			
	def insert(self,value):
		if(self.root==None):
			self.root=Node(value)
			print("This is Root Element :"+ str(self.root.value))
		else:
			temp=self.root
			while(temp.next!=None):
				temp=temp.next
			temp.next=Node(value)
	
	def display(self):
		temp=self.root
		print("Root is :"+str(temp.value))
		while(temp.next!=None):
			temp=temp.next
			print(" -> "+str(temp.value))
			
	def delete(self,value):
		temp=self.root
		if(temp.value==value):
			print("Deleted Root element :"+str(self.root.value))
			self.root=temp.next
			
		else:
			try:
				while(temp.next.value!=value):
					temp=temp.next
				print("Deleted Element: "+str(temp.next.value))
				temp.next=temp.next.next
			except:
				if(temp.next==None):
					print("No Element Found")

ll=Linked()
ll.insert(2)
ll.insert(3)
ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.delete(10)
ll.display()
