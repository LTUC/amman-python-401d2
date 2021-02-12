# from data_structure.tree import Node , BinaryTree 
class Node:
    def __init__(self,value ):
        self.value  = value
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.root = None 

    def preorder(self):
        array_of_output = [] 
        def _walk(node):
            array_of_output.append(node.value)
            if node.left:
               _walk(node.left)
            if node.right:
               _walk(node.right)  
        _walk(self.root)  
 
        return array_of_output 



def FizzBuzzTree(k_ary):
    array_of_output = [] 
    def _walk(node):
        if  node.value % 5 == 0 and node.value %3 == 0:
            array_of_output.append('FizzBuzz')  
        elif node.value % 3 == 0:
           array_of_output.append('Fizz')
        elif node.value % 5 == 0:
           array_of_output.append('Buzz') 
        else:
            array_of_output.append(node.value) 

        if node.left:
            _walk(node.left)
        if node.right:
            _walk(node.right)  
    _walk(k_ary.root)  

    return array_of_output 




    
   





