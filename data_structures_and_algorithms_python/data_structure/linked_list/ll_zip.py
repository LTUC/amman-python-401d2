from linked_list import LinkedList , Node

# def zipLists(ll1, ll2):
#     if not ll1.head:
#         return ll2.head
#     elif not ll2.head:
#         return ll1.head

#     current1, current2 = ll1.head, ll2.head

#     while current1 and current2:
#         next1, current1.next = current1.next, current2
#         if next1:
#             next2, current2.next = current2.next, next1
#         current1, current2 = next1, next2

#     return ll1.head
# if __name__ == "__main__":
#     ll1 = LinkedList()
#     ll2 = LinkedList()

#     ll1.append(1)
#     ll1.insert(2)
#     print(ll1)
#     ll2.append(2)
#     ll2.insert(4)
#     print(ll2)
#     zipLists(ll1, ll2)
#     print( ll1)
def zipLists(list1, list2):
    current_one = list1.head  
    current_two = list2.head
    if current_one == None:
        return print(list2)
    if current_two == None:
        return print(list1)
    new_list = LinkedList()
    while current_one or current_two:
        if current_one:
            if new_list.head == None:
                new_list.insert(current_one.value)
            else:
                new_list.append(current_one.value)
        if current_two:
            if new_list.head == None:
                new_list.insert(current_two.value)
            else:
                new_list.append(current_two.value)
        if current_one and current_one.next:
            current_one = current_one.next
        else:
            current_one= False
        if current_two and current_two.next:
            current_two = current_two.next
        else:
            current_two=False
    return new_list