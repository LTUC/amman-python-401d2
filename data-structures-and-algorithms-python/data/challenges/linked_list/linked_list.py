class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def includes(self, data):
        current = self.head
        while (current != None):
            if current.value == data:
                return True
            else:
                return False

    def __str__(self):
        if self.head == None:
            return ("NULL")
        else:
            list = ""
            current = self.head
            while (current != None):
                list += '{ %s } -> ' %current.value
                current = current.next
            list += 'NULL'
            return (f"{list}")

