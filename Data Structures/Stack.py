from LinkedList import LinkedList

class Stack:
    def __init__(self):
        self.list = LinkedList()

    #adds a new value to start 
    def push(self,data):
        self.list.insert_node(data,1)

    #pops out latest value
    def pop(self):
        self.list.remove_node(self.list.head.data)

    #prints stack
    def print_stack(self):
        current = self.list.head
        while(current):
            print(current.data)
            current = current.next


# stack = Stack()
# stack.push(12)
# stack.push(13)
# stack.push(14)
# stack.pop()
# stack.print_stack()