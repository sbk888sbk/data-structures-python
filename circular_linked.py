class Node:
    def __init__(self,data):
        self.value=data
        self.next=None

class Circular:
    def __init__(self):
        self.head=None

    def insert(self,value):
        temp=self.head
        if(temp is None):
            self.head=Node(value)
            self.head.next=self.head
        else:
            while(temp.next is not self.head):
                temp=temp.next
            temp.next=Node(value)
            temp=temp.next
            temp.next=self.head


    def disp(self,head):
        temp=head
        print("Head Element")
        while(temp.next is not self.head):
            print(str(temp.value) + " -> ")
            temp = temp.next
        print("Last Element : "+str(temp.value) + " -> ")
        print("Reached Head Element :"+str(temp.next.value))
       # return 0

    def delete(self,value):
        temp=self.head
        while(temp.next.value!=value and temp.next!=head):
            temp=temp.next
        if(temp.next==self.head):
            self.head=self.head.next
            temp.next=self.head
           # return 0
            print("Head Element Deleted, New Head Element is : "+str(self.head.value))
        elif (temp.next.value == value):
            temp.next = temp.next.next
            print("Element Found and Deleted")
           # return 0
        else:
            print("No Element Found")
           # return 0


cl=Circular()
cl.insert(4)
head=cl.head
cl.insert(5)
cl.insert(6)
cl.insert(7)
cl.delete(4)
cl.disp(cl.head)
cl.insert(10)
cl.delete(4)
cl.disp(cl.head)
