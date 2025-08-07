class Queue:
    def __init__(self,size):
        self.queue = []
    def enque(self,data):
        self.queue.append(data)

    def deque(self):
        if len(self.queue)==0:
            print("isempty")
            return
        self.queue.pop(0)

    def Front(self):
        if len(self.queue) == 0:
            print("isempty")
            return
        print(f"front : {self.queue[0]}")
    def display(self):
        if len(self.queue) == 0:
            print("isempty")
            return
        for i in self.queue:
            print(i,end=" ")

obj = Queue(15)
a = [9,3,4,12,0,34,2,22]
for i in a:
    obj.enque(i)
obj.display()