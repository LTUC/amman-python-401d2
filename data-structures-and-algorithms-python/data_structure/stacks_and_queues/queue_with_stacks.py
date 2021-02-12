from stacks_and_queues import Node,Stack,Queue

class PseudoQueue:
        def __init__(self):
            self.stack1 = Stack()
            self.stack2 = Stack()
        
        def enqueue(self,data):
            self.stack1.push(data)
            # self.stack2.push(data)
                        
        def dequeue(self):
            if self.stack1.is_empty() and self.stack2.is_empty():
                raise AttributeError('The PseudoQueue is empty') 
            if self.stack2.is_empty():
                while self.stack1.top != None:
                      self.stack2.push(self.stack1.pop())
                return self.stack2.pop()
            else:
                return self.stack2.pop()    

if __name__ == "__main__":
    s = PseudoQueue()
    s.enqueue(1)
    s.enqueue(3)
    s.enqueue(4)
    print(s.stack2.is_empty())
    print(s.stack1.peek())
    s.dequeue()
    s.dequeue()
    print(s.stack2.peek())
     
    
   
 



                