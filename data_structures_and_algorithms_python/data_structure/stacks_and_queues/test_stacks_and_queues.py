from stacks_and_queues import Stack, Queue
from queue_with_stacks import PseudoQueue
import pytest

@pytest.fixture
def prep_stack():
    elements = Stack()
    elements.push('The challenge')
    elements.push('has been')
    elements.push('solved')
    elements.push('successfully')
    return elements

def test_push_3_element(prep_stack):
    assert prep_stack.peek() == 'successfully'

def test_pop_element(prep_stack):
    assert prep_stack.pop() == 'successfully'
    assert prep_stack.peek() == 'solved'

def test_pop_empty():
    element = Stack()
    with pytest.raises(AttributeError):
        assert element.pop()

def test_peek():
    element = Stack()
    element.push(1)
    assert element.peek() == 1
   

def test_is_empty(prep_stack):
    prep_stack.pop() == 'solved'
    prep_stack.pop() == 'has been'
    prep_stack.pop() == 'The challenge'
    assert prep_stack.is_empty() == True

# ---------------------------------------------------------------------

@pytest.fixture
def prep_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2) 
    return queue  
    
def test_enqueue_3(prep_queue):
    assert prep_queue.peek() == 1

def test_dequeue_one_item(prep_queue):
    prep_queue.dequeue == 2

def test_is_empty(prep_queue):
    assert  prep_queue.is_empty() == False
# -------------------------------------------------------------------------

def test_PseudoQueue_enqueue():
    element = PseudoQueue()
    element.enqueue(1)
    element.enqueue(2)
    assert element.stack1.peek() == 2
     

def test_PseudoQueue_dequeue():
    element = PseudoQueue()
    element.enqueue(1)
    element.enqueue(2)
    element.dequeue()
    assert  element.stack2.peek() == 2
       



    



    




    