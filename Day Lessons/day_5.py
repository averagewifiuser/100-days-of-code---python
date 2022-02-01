#######Lesson 9: Dictionaries

this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors": ['red', 'black', 'blue']
}

#dicts don't allow duplicates

#
x = this_dict.get('model')
x = this_dict["model"]
print(x)

x = this_dict.keys()
print(x)

print(this_dict.values())
print(this_dict.items())