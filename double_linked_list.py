class Node:
	def __init__(self,data):
		self.prev=None
		self.value=data
		self.next=None 
		print("Created node with value "+str(self.value))
		
class Double:
	def __init__(self):
		self.head=None
	
	def insert(self,value):
		if(self.head==None):
			self.head=Node(value)
			print("Inserted head with value"+str(self.head.value))
		else:
			temp=self.head
			while(temp.next!=None):
				temp=temp.next			
			temp.next=Node(value)			
			temp.next.prev=temp
			print(str(temp.next.prev.value)+" is the previous element of "+str(temp.next.value))
			
			
	def display(self):
		temp=self.head
		while(temp.next!=None):
			print("<-"+str(temp.value))
			temp=temp.next
		print("<-"+str(temp.value))
		
	
	def delete(self,value):
		if(self.head.value==value):
			self.head=self.head.next
			self.head.prev=None
		else:
			try:
				temp=self.head
				while(temp.next.value!=value):
					temp=temp.next
				temp.next=temp.next.next
				if(temp.next!=None):				
					temp.next.prev=temp
			except:
				if(temp.next==None):
					print("No Elemenet Found")
					
			
	def delete_index(self,index):
		temp=self.head
		if(index==0):
			print("deleted "+str(temp.value)+" at index "+str(index))
			self.head=temp.next
			temp.prev=None
			temp=None
			
			return
		for current_index in range(index) :
			if(temp):
				temp=temp.next
		if(temp is None):
			print("Index :"+str(index)+" is greater than length of list")
			return
		elif(temp.next is not None):
			
			temp.prev.next=temp.next
			temp.next.prev=temp.prev
		else:
			temp.prev.next=None
		print("deleted "+str(temp.value)+" at index :"+str(index))

		
	
d=Double()
d.insert(2)
d.insert(3)
d.insert(4)
d.insert(5)
d.insert(6)
d.insert(7)


print("Double linked list contains: ")
d.display()
d.delete(7)
d.delete(2)
d.delete(5)
print("Double linked list contains: ")
d.display()
d.insert(8)
d.insert(9)
print("Double linked list contains: ")
d.display()
d.delete(91)
print("Double linked list contains: ")
d.display()
d.delete_index(0)
d.delete_index(10)
d.delete_index(3)
d.display()
