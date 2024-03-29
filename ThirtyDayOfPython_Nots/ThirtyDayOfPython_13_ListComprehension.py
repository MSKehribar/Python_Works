# List Comprehension
# List comprehension in Python is a compact way of creating a list from a sequence. It is a short way to create a new list. 
# List comprehension is considerably faster than processing a list using the for loop.
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']
























