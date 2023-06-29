class node:
    def __init__(self,u):
        self.data=u;
        self.nxt=None
class linked:
    def __init__(self):
        self.head=None
        self.tail=None
    def create(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            self.tail.nxt=node(x)
            self.tail=self.tail.nxt
    def add_front(self,x):
        temp=node(x)
        temp.nxt=self.head
        self.head=temp
    def add_middle(self,x,y):
        temp=self.head
        while temp!=None:
            if x==temp.data:
                break
            temp=temp.nxt
        if temp==None:
            print("empty")
        else:
            temp1=node(y)
            temp1.nxt=temp.nxt
            temp.nxt=temp1
    def pr(self):
        if self.head==None:
            print("EMPTY")
        else:
            temp=self.head
            while(temp!=None):
                print(temp.data,end="->")
                temp=temp.nxt
    def ip(self):
        for i in range(1,n+1):
            l1.create(int(input()))
            l1.pr()
    def del_back(self):
        if(self.head==None):
            print("empty")
        else:
            temp=self.head
            t=temp.nxt
            while(t.nxt!=None):
                temp=temp.nxt
                t=t.nxt
            temp.nxt=None
    def del_front(self):
        if(self.head==None):
            print("empty")
        else:
            temp=self.head.nxt
            self.head=None
            self.head=temp
    def del_btw(self,x):
        if self.head==None:
            print("empty")
        else:
            temp=self.head
            temp1=temp.nxt
        
l1=linked()
n= int(input())
l1.ip()
print()
l1.add_front(5)
l1.pr()
print()
#l1.del_back()
#l1.pr()
#print()
l1.add_middle(20,25)
l1.pr()
print()
#l1.del_front()
#l1.pr()
        
