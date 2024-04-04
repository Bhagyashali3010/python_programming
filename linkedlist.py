class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def createlist(self, newnode):
        if self.head is None:
            self.head=newnode
        else:
            lastnode=self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode=lastnode.next
            lastnode.next=newnode

    def printlist(self):
        if self.head is None:
            print("LIST IS EMPTY")
        currentnode=self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode=currentnode.next
    
aa=node("asd")
bb=node("df")
cc=node("wert")
llst=linkedlist()
llst.createlist(aa)
llst.createlist(bb)
llst.createlist(cc)
llst.printlist()

            
            
