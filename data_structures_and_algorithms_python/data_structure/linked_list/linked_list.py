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
        while current != None:
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
            while current != None:
                list += '{ %s } -> ' %current.value
                current = current.next
            list += 'NULL'
            return (f"{list}")

    def append(self,data):
        node = Node(data)
        if self.head == None:
           self.head = node
        else:
            current = self.head
            while current.next != None:
                  current = current.next
            current.next= node
    
    def insertBefore(self,value,newVal):
        node = Node(newVal)
        if self.head.value == value:
            return(self.insert(newVal))
        current = self.head
        while current.next.value != value:
            current = current.next
        node.next = current.next
        current.next = node

    def insertAfter(self,value,newVal):
        node = Node(newVal)
        current = self.head
        while current.value != value:
              current = current.next
        node.next = current.next
        current.next = node

    def  startFromLast(self,k):
        current = self.head
        length = 0
        while current: 
              current = current.next
              length += 1
          
        if k > length: 
            print('The number is greater than the length of LinkedList') 
            return
        else:
            current = self.head 
            for i in range(0, length - k-1): 
                current = current.next
 
if __name__ == "__main__":
    llist = LinkedList() 
    llist.append(3)
    llist.append(4) 
    print(llist.startFromLast(9))       





