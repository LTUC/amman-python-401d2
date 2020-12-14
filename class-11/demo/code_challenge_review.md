S1
S2
queue.enqueue(i)
    S1.push(i)
queue.dequeue()
    exceptions
    push all elements from S1 to S2
    returned_val = S2.pop() # 3
    push the elements back to S1
    return returned_val

3 - 6 - 9 - 5 - 2


S1: 3 -> 6 -> 9
S2:

dequeue()
S1:
S2: 9 -> 6 -> 3
S2: 9 -> 6
S1: 6 -> 9
S2:

enqueue
S1: 6 -> 9 -> 5 -> 2
S2:

dequeue
S1:
S2: 2 -> 5 -> 9 -> 6
S2: 2 -> 5 -> 9
S1: 9 -> 5 -> 2
S2:
