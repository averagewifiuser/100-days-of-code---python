#########Lesson 7: Tuples

this_tuple = ("apple", "banana", "cherry")
one_item_tuple=("apple",) #requires the comma
#without comma it is a str type

#tuples are indexed like lists

#updating, removing from tuple value and adding new to tuple
#you'd need to change it to a list first because tuples are immutable

x = ("apples", "oranges")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

# you can add tuples to tuples
this_tuple += one_item_tuple

#delete a tuple
del one_item_tuple

#unpacking tuples
apple, banana, *cherry = this_tuple
print(cherry) #multiple will be added in al ist



######Lesson 8: Sets!
my_set = {"apple", "orange", "lola"}
this_set = {'mark', 'ruger'}
#sets are unchangeable but you can add or remove items
#no duplicates
#also unordered
#can't index or use keys to access items in a set

my_set.add("tangerine")
my_set.update(this_set)
my_set.remove("tangerine") #raises error if item not found
my_set.discard("tangerine") #no error raised

my_set.pop() #last item removed

my_set.union(this_set)#joins to sets
my_set.intersection_update(this_set)
#the above method keeps only the items present in both sets

#set_one.intersection(set_two) will return a new list with duplicate items in both sets

#set_one.symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

#more info on set methods
#https://www.w3schools.com/python/python_sets_methods.asp


