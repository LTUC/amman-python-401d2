from linked_list import LinkedList , Node

def zipLists(ll1, ll2):
    if not ll1.head:
        return ll2.head
    elif not ll2.head:
        return ll1.head

    current1, current2 = ll1.head, ll2.head

    while current1 and current2:
        next1, current1.next = current1.next, current2
        if next1:
            next2, current2.next = current2.next, next1
        current1, current2 = next1, next2

    return ll1.head
if __name__ == "__main__":
    ll1 = LinkedList()
    ll2 = LinkedList()

    ll1.append(1)
    ll1.insert(2)
    print(ll1)
    ll2.append(2)
    ll2.insert(4)
    print(ll2)
    zipLists(ll1, ll2)
    print( ll1)
