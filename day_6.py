# ########Lesson 10: Functions

# #create function
# def my_function():
#     print("Hello Function")

# #call function
# my_function()

# #functions with arguments
# def new_function(fname):
#     print(fname + "'s function")

# new_function("Joseph")

# def name_combinator(fname, lname):
#     print(fname + " " + lname)

# name_combinator("joseph", "jones")

# #arbitrary arguments
# def arbitrary_args(*args):
#     print(f"the youngest child is {args[1]}")

# arbitrary_args("Emil", "Tobias")


# #keyword args
# def keyword_args(child3, child2, child1):
#     print("The youngest is " + child2)


# keyword_args(child1="Jane", child2="Joe", child3="Kate")

# #arbitrary keyword args
# def abs_keyword_args(**kwargs):
#     print(f"His last name is {kwargs['lname']}")
    

# abs_keyword_args(fname="Joe", lname="Doe")

# #default parameter
# def default_function(country="sweden"):
#     print("I am from "+country)


# default_function("india")

# #recursion
# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)

# #lambda
# #it is a small anon function
# #can take any number of args but have only one expression

x = lambda a: a + 10
print(x(5))

x = lambda a,b : a * b
print(x(5,6))

def my_function(n):
    return lambda a: a * n

my_doubler = my_function(2)

print(my_doubler(33))


#some popular functions

#convert to int
string_to_num = int('1')

x = "joseph".upper()

print(x)

#splitting a string into words
string_one = "Joseph is great"
print(string_one.split())

#into letters
print(list(string_one))
