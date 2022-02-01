'''
STACKS - INTRO

A stack is a linear data structure that 
stores items in a Last-In/First-Out (LIFO) 
or First-In/Last-Out (FILO) manner. In stack, 
a new element is added at one end and an element 
is removed from that end only. The insert and 
delete operations are often called push and pop.
'''

stack = []
#append() to push element in the stack
stack.append('g')
stack.append('f')
stack.append('h')

print('Initial stack')
print(stack)

#pop() function to pop element frrom stack in LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('Stack after elements are popped:')
print(stack)


'''
QUEUES
As a stack, the queue is a linear data structure 
that stores items in a First In First Out (FIFO) manner. 
With a queue, the least recently added item is removed first. 
A good example of the queue is any queue of consumers for a 
resource where the consumer that came first is served first.
'''

queue = []
print("Initial queue")
print(queue)

#adding elements to queue
queue.append('g')
queue.append('f')
queue.append('h')

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
 
print("\nQueue after removing elements")
print(queue)