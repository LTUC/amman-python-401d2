# from data_structures.stacks_and_queues.stacks_and_queues import Stack

def multi_bracket_validation(input):
    temp = Stack()
    brackets = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    
    for user_input in input:
        if user_input in brackets.values():
            temp.push(user_input)
            
        elif user_input in brackets.keys():
            
            try:
                if not brackets[user_input] == temp.pop():
                    return False
            except AttributeError as err:
                print(err)
                return False
    
    return temp.is_empty()
    # ____________________________________________________________________________________
    ## helper clasess
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None    
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):
        if self.top == None:
            raise AttributeError('Cannot be called an empty stack')
        else:
            remved_top = self.top.value
            self.top = self.top.next 
            return remved_top
         
    def peek(self):
        if self.top == None:
            raise AttributeError('There is no peek in empty stack')
        return self.top.value
        
    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False  