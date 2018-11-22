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
	
	def delete_index(self,index):
		current_index=0;
		temp=self.root
		if(index==0):
			print("Deleted Root Element "+str(temp.value))
			self.root=temp.next
			print("New root element is : "+str(self.root.value))
			return
		while(current_index+1!= index and temp.next is not None):
			temp=temp.next
			current_index+=1
		if(temp.next is None):
			print("Index: "+str(index)+" is greater than linked list length")
			return
		print("Deleted Element at Index: "+str(index)+" Node: "+str(temp.next.value))
		temp.next=temp.next.next
		

ll=Linked()
ll.insert(2)
ll.insert(3)
ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.delete(10)
ll.display()
ll.delete_index(2)
ll.delete_index(10)
ll.display()
