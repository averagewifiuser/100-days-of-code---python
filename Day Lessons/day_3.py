'''
Lesson 5 - Mutable and Immutable Data Types
Mutable - Lists, Dictionary, Sets
Immuntable - Tuples, Integers, Strings etc

Orderered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

Changeable (Mutable)


'''


# Lesson 6 - 

#Lists are ordered, mutable and allow duplicates

#create List
this_list = ["apple", "mango", "pear"]
print(this_list)

new_list = list(('apple', 1, 2, 'goat', 4, 'pear', 'lady', 9, 0))
print(new_list)

#accessing items in a list
print(this_list[0]) #index a list (first index is 0)
print(this_list[-1])#index last item

#range of indexes
print(new_list[2:5])#starts at index 2 ends at index 4
print(new_list[:4])#start at beginning and end before 4
print(new_list[3:])#start from 3 to the end

new_list.append(1) #adding to a new list
new_list.extend([1,2,3])
new_list.insert(1, "watermeling")

new_list.remove(1)#takes value
new_list.pop(1)#takes the index
del new_list[0] 
# new_list.clear() #list remains with no content
new_list.sort()#ascending
new_list.sort(reverse=True)#descending
new_list.reverse() #prints list in reverse order
