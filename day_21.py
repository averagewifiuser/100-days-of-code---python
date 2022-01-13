#continuation of linked lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    #list traversal
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    #inserting a new head (complexity O(1))
    def push(self, new_data):
        #make a new node
        new_node = Node(new_data)
        
        #allocate the current head as the next for this node
        new_node.next = self.head

        #now make the new_node the head
        self.head = new_node

    #insert a node inbetween the list(complexity O(1))
    def insert_after(self, prev_node, new_data):
        #check if the previous node exists
        if prev_node is None:
            print("The given previous node does not exist")
            return

        #create the new node with data
        new_node = Node(new_data)

        #make next of new node as next of prev_node
        new_node.next = prev_node.next
        #make next of prev_node the new node
        prev_node.next = new_node

    
    #insert a node at the last(complexity O(n))
    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        #traverse through the linked list to find the last
        #the last would have their next = None
        last = self.head
        while last.next:
            last = last.next

        #append the new node
        last.next = new_node

        '''
        the append can be be optimised to be O(1) by having a pointer that points to the 
        last node in the linked list
        '''

#empty list
linked_list = LinkedList() #list is emptu
linked_list.append(1) # 1 -> None

linked_list.push(0) # 0 -> 1 -> None

linked_list.append(3) # 0 -> 1 -> 3 -> None

linked_list.insert_after(linked_list.head.next, 9) # 0->1->9->3->None

#print list
linked_list.print_list()
