'''
A counter is a sub-class of the dictionary. It is used to keep the count of the elements in an iterable in the form of an unordered dictionary where the key represents the element in the iterable and value represents the count of that element in the iterable. A counter is a sub-class of the dictionary. 
'''

from collections import Counter, defaultdict, namedtuple

#counter with a list of items
print(Counter(['b','b','c', 'd','e','e','f','a','a']))

#counter with dict
count = Counter({'A':2, 'B':3, 'C':5})

count.update('A')
count.update(['A', 'D'])
print(count)

d = defaultdict(int)

L = [1,2,3,4,2,4,1,2]

for i in L:
    # The default value is 0
    # so there is no need to enter the key first
    d[i] += 1
    

print(d)

Student = namedtuple('Student', ['name', 'age', 'grade'])

student_one = Student('Joe', '190', 'Grade Four')
print(student_one.age)