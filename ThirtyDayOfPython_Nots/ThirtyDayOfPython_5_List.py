"""
help(list)
dir(list)

List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
Lists are written with []. We can change its values. 
"""

empty_list = list()     # this is an empty list, no item in the list
empty_list = []         # this is an empty list, no item in the list
print(len(empty_list))  # 0

lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types

first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
# first=1, second=2, third=3, rest=[4,5,6,7,8,9], tenth=10

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:]     # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3]  # it does not include the first index
orange_and_lemon = fruits[::2]  #It will take every 2cnd item - ['banana', 'mango']
orange_and_mango = fruits[-3:-1]    # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:]    # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1]   # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']
fruits[1] = 'apple'             #  ['avocado', 'apple', 'mango', 'lemon']
print('lime' in fruits)         # False
fruits.append('apple')          # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.insert(2, 'apple')       # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.remove('lemon')          # ['orange', 'mango', 'banana']
fruits.pop()                # ['banana', 'orange', 'mango']  remove last index
fruits.pop(0)               # ['orange', 'mango']            remove 0. index 
del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
fruits.clear()      #The clear() method empties the list:
del fruits          # to delete the list completely

#list2 = list1. 
# Now, list2 is a reference of list1, any changes we make in list2 will also modify the original, list1.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy() # Now, fruits_copy is different list from fruit
#Joining List
# There are several ways to join, or concatenate, two or more lists in Python.
two_fruit_list=fruits+fruits
#Joining using extend() method The extend() method allows to append list in a list.
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3.    The count() method returns the number of times an item appears in a list:
print(ages.index(24))           # 2, the first occurrence.  The index() method returns the index of an item in the list:
ages.reverse()              #The reverse() method reverses the order of a list.
print(ages)                 # [24, 25, 24, 26, 25, 24, 19, 22]
ages.sort()         #The sort() method reorders the list items in ascending order and modifies the original list.
print(ages)         #  [19, 22, 24, 24, 24, 25, 25, 26]

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True)    #sorted(): returns the ordered list without modifying the original list
print(fruits)     # ['orange', 'mango', 'lemon', 'banana']












