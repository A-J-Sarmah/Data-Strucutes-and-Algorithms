class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 
    
    #insert Node at end
    def append_node(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current:
                if not current.next:
                    current.next = newNode
                    break
                current = current.next
        else:
            self.head = newNode

    #insert a node at random place
    def insert_node(self,data,position):
        new_element = Node(data)
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        elif position > 0:
            current = self.head
            counter = 1
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1

    #gets data at certain position
    def get_data_on_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current.data
            current = current.next
            counter += 1
        return None

    #delete node from linked list
    def remove_node(self,data):
        current = self.head
        previous = None
        while current.data != data and current.next:
            previous = current
            current = current.next
        if current.data == data:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    #print Node
    def print_linked_list(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

# linked_list = LinkedList()
# linked_list.append_node(12)
# linked_list.append_node(13)
# linked_list.append_node(14)
# linked_list.remove_node(13)
# linked_list.insert_node(15,3)
# linked_list.print_linked_list()
# print(linked_list.get_data_on_position(2))