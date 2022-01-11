'''
Deque - Doubly Ended Queue
optimized list for append and pop operation
from both sides of container.

implemented using doubly linked lists
'''

# from collections import deque

# de = deque([1,2,3,4,5])

# #append to right end
# de.append(4)

# print(de)

# #append to left end
# de.appendleft(0)

# print(de)

# #popleft
# de.popleft() #deletes first from the left

# de.pop() #deletes first from right
# print(de)


'''
Linked List - is a linear data structure,
in which the elements are not stored at 
contiguous memory locations. The elements in a linked 
list are linked using pointers
'''

# Node class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


    #this function prints the contents
    #of the linked list
    #starting from the head
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next



#empty list
linked_list = LinkedList()

linked_list.head = Node(1)
second = Node(2)
third = Node(3)

linked_list.head.next = second
second.next = third

linked_list.print_list()