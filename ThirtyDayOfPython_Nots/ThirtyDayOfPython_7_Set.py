"""
help(set)
dir(set)

Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. 
Duplicate members are not allowed.

Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson. 
The Mathematics definition of a set can be applied also in Python. 
Set is a collection of unordered and un-indexed distinct elements. 
In Python set is used to store unique items, 
and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.

We use curly brackets, {} to create a set or the set() built-in function.
"""

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.add('lime')          #Add one item using add()
fruits.update(vegetables)   #Add multiple items using update() The update() allows to add multiple items to a set. The update() takes a list argument.
#We can remove an item from a set using remove() method. If the item is not found remove() method will raise errors
#However, discard() method doesn't raise any errors.
fruits.remove('lime')  
removed_item =fruits.pop()  # removes a random item from the set
fruits.clear()
del fruits

lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st4 = {'item2', 'item3'}
st3 = st1.union(st2)    #Union This method returns a new set
st1.update(st2)         #st2 contents are added to st1

print(st2.issubset(st1)) # True
print(st1.issuperset(st2)) # True
print("st1",st1)
print("st3",st3)
print("st3\st4",st3.difference(st4)) # {'item4', 'item7', 'item6', 'item8', 'item1', 'item5'} => st3\st4
print("(A\B)∪(B\A)",st3.symmetric_difference(st4))  #{'item4', 'item7', 'item6', 'item8', 'item1', 'item5'}

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print("isdisjoint",st2.isdisjoint(st1)) # False




















