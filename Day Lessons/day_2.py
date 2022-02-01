##############Lesson 3 - operators

##3.1 - arithmetic operators
# print(10+3)
# print(10-4)
# print(9*9)   #multiplication
# print(20/3)  #division
# print(90%9)  #modulus
# print(2**8)  #exponent
# print(20//3) #floor division

##3.2 - assignment

# x = 5
# print(x)
# x += 3 # x= x + 3
# print(x)
# x **= 3 # x = x ** 3
# print(x)

##3.3 - comparison
# x, y = 4, 2

# print( x == y) #equals
# print(x != y)
# print(x > y)
# print( x >= y)

#python logical operators

'''
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
'''


#######Lesson 4 - Control Flow (if/else)
x = 5
y = 10
z = 10

if x == y:
    print("They're equal!")
else:
    print("They're not equal!")


if y > x:
    print(f'Your number is bigger than {x}')
else:
    print('Your number is smaller!')


if y > 10:
    print('Y is greater')
elif y < 10:
    print('Y is less')
else:
    print('they are equal')