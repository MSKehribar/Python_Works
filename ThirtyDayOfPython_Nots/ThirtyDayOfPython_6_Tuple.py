"""
A tuple is a collection of different data types which is ordered and unchangeable (immutable). 
Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. 
We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). 
Methods related to tuples:

tuple(): to create an empty tuple
count(): to count the number of a specified item in a tuple
index(): to find the index of a specified item in a tuple
operator: to join two or more tuples and to create a new tuple
"""

tpl = ('item1', 'item2', 'item3','item4','item5')
len(tpl)
second_item = tpl[1]
last_item = tpl[-1]
sec_and_third_items = tpl[1:3]  # sec and third items in tpl

#We can change tuples to lists and lists to tuples. 
# Tuple is immutable if we want to modify a tuple we should change it to a list.
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')
print('lime' in fruits) # False 
print('apple' in fruits) # True


fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
del fruits
print(fruits)












