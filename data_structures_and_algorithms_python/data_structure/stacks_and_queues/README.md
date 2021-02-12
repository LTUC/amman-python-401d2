# Stacks and Queues
<!-- Short summary or background information -->
## A stack
 is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.
## PseudoQueue:
 PseudoQueue class will implement our standard queue interface (the two methods listed below), but will internally only utilize 2 Stack objects. 
### The class with the following methods:

* enqueue(value) which inserts value into the PseudoQueue, using a first-in, first-out approach.
* dequeue() which extracts a value from the PseudoQueue, using a first-in, first-out approach.

## Mehtods that implemented in stack class:

* Push - Nodes or items that are put into the stack are pushed
* Pop - Nodes or items that are removed from the stack are popped. When you attempt to pop an empty stack an exception will be raised.
* Peek - When you peek you will view the value of the top Node in the stack. When you attempt to peek an empty stack an exception will be raised.
* IsEmpty - returns true when stack is empty otherwise returns false.

## Mehtods that implemented in stack class:

* Enqueue - Nodes or items that are added to the queue.
* Dequeue - Nodes or items that are removed from the queue. If called when the queue is empty an exception will be raised.
* Peek - When you peek you will view the value of the front Node in the queue. If called when the queue is empty an exception will be raised.
* IsEmpty - returns true when queue is empty otherwise returns false

## Challenge
<!-- Description of the challenge -->
Write methods for Stack and Queue classes and testing them

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The big O is used (O(1) operation. )


## API (Stack)
<!-- Description of each method publicly available to your Stack and Queue-->
**ALOGORITHM push(value)**

// INPUT <-- value to add, wrapped in Node internally

// OUTPUT <-- none

   node = new Node(value)
   node.next <-- Top
   top <-- Node
__________________
**ALGORITHM pop()**
// INPUT <-- No input

// OUTPUT <-- value of top Node in stack

// EXCEPTION if stack is empty

   Node temp <-- top
   top <-- top.next
   temp.next <-- null
   return temp.value
   ___________ 
**ALGORITHM peek()**

// INPUT <-- none

// OUTPUT <-- value of top Node in stack
// EXCEPTION if stack is empty

   return top.value
   __________
   **ALGORITHM isEmpty()**

// INPUT <-- none

// OUTPUT <-- boolean

return top = NULL
__________
## API (Queue)
**ALGORITHM enqueue(value)**

// INPUT <-- value to add to queue (will be wrapped in Node internally)

// OUTPUT <-- none

   node = new Node(value)
   rear.next <-- node
   rear <-- node
__________________
**ALGORITHM dequeue()**

// INPUT <-- none

// OUTPUT <-- value of the removed Node
// EXCEPTION if queue is empty

   Node temp <-- front
   front <-- front.next
   temp.next <-- null

   return temp.value
   ___________ 
**ALGORITHM peek()**

// INPUT <-- none

// OUTPUT <-- value of the front Node in Queue
// EXCEPTION if Queue is empty

   return front.value
   __________
**ALGORITHM isEmpty()**

// INPUT <-- none

// OUTPUT <-- boolean

return front = NULL
