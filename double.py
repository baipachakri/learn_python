class node:
    def __init__(self,x):
        self.data=x
        self.nxt=None
        self.prev=None
class link:
    def __init__(self):
        self.head=None
        self.tail=None
    def add_front(self,x):
        if self.head==None:
           self.head=node(x)
           self.tail=self.head
        else:
            temp=node(x)
            temp.nxt=self.head
            self.head.prev=temp
            self.head=temp
    def priint(self):
        if self.head == None:
            print("empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end="->")
                temp=temp.nxt
    def inpuut(self):
        for i in range (1,n+1):
            l1.add_front(int(input()))
            l1.priint()
        
l1=link()
n=int(input())
l1.inpuut()

                
            
    
        
        
