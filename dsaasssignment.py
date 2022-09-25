class Node:
    def __init__(self,name=None,age=None):
        self.name=name
        self.age=age
        self.prev=None
        self.next=None
class doublylinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        
#doubly linked list 
    def createdll(self,name,age):
        node1= Node(name,age)
        self.head=node1
        self.tail=node1      
    def display(self):
        if self.head is None:
            print("The list is empty")
        else:
            n=self.head
            while n is not None:
                print("Name is :",n.name,"Age is :",n.age,",",end=" ")
                n=n.next
                
                
DLL= doublylinkedlist()
DLL.createdll("FATHER",40)
DLL.display()
DLL.createdll("MOTHER",35)
DLL.display()
DLL.createdll("DAUGHTER",18)
DLL.display()
DLL.createdll("SON",10)
DLL.display()
