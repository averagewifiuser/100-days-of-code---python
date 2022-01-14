#continuation of linked lists
#deletion

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 


    #list traversal
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    
    #deletion of first occurence of the key in a list
    def delete_node(self, key):
        #store head node
        temp = self.head

        #if key is not present
        if temp == None:
            return

        #if the head node is the key to be deleted
        if temp is not None:
            self.head = temp.next
            temp = None
            return

        #search for the key
        while temp is not None:
            if temp.data == key:
                break

            prev = temp
            temp = temp.next
            
        prev.next = temp.next

        temp = None


llist = LinkedList() 
llist.push(7) 
llist.push(1) 
llist.push(3) 
llist.push(2) 

print ("Created Linked List: ")
llist.print_list() 
llist.delete_node(1) 
print ("\nLinked List after Deletion of 1:")
llist.print_list() 

