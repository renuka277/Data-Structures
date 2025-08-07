from enum import nonmember
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def b_insert(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def display(self):
        if self.head is None:
            print("empty")
            return
        cur = self.head
        while cur:
            print(cur.data, end="->")
            cur=cur.next
    def e_insert(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        cur=self.head
        while cur.next:
            cur=cur.next
        cur.next=newnode
    def b_delete(self):
        if self.head is None:
            print("empty")
            return
        self.head=self.head.next
    def e_delete(self):
        if self.head is None:
            print("empty")
            return
        if self.head.next is None:
            self.head=None
            return
        cur=self.head
        while cur.next.next:
            cur=cur.next
        cur.next=None
    def fin_position(self,pos):
        cur=self.head
        for i in range(pos-1):
            if cur.next is None:
                return -1
            cur=cur.next
        return cur
    def insert_at(self,data,pos):
        newnode = Node(data)
        if pos==1:
            self.b_insert(data)
            return
        cur=self.fin_position(pos-1)
        if cur==-1:
            print("position is not found")
        else:
            newnode.next=cur.next
            cur.next=newnode







obj=linkedlist()
print("insertion at begin")
obj.b_insert(10)
obj.b_insert(20)
obj.b_insert(7)
obj.display()
obj.e_insert(40)
obj.e_insert(50)
obj.e_insert(1)
print()
print("after insertion at end")
obj.display()
obj.b_delete()
print()
print("after delete at begin")
obj.display()
obj.e_delete()
print()
print("delete at end")
obj.display()
obj.fin_position(2)
print()
obj.insert_at(12,2)
print()
obj.display()




