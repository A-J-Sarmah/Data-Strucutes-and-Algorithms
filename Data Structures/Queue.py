from LinkedList import LinkedList

class Queue:
    def __init__(self):
        self.storage = LinkedList()

    
    #enqueue method adds an element in end 
    def enqueue(self,data):
        self.storage.append_node(data)

    #dequeue method removes first element from 
    def dequeue(self):
        self.storage.remove_node(self.storage.head.data)

    #peek method gives 1st element from
    def peek(self):
        return self.storage.head.data

    #prints queue 
    def print_queue(self):
        current = self.storage.head
        while(current):
            print(current.data)
            current = current.next


queue = Queue()
queue.enqueue(12)
queue.enqueue(13)
queue.enqueue(14)
queue.dequeue()
queue.print_queue()