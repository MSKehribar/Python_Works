"""
help(dict)
dir(dict)

Dictionary: is a collection which is unordered, changeable(modifiable), paired (key: value) and indexed data type.
No duplicate members.

To create a dictionary we use curly brackets, {} or the dict() built-in function.
"""

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'    }
    }
print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
#Accessing an item by key name raises an error if the key does not exist. 
# To avoid this error first we have to check if a key exist or we can use the get method. 
# The get method returns None, which is a NoneType object data type, if the key does not exist.
print(person.get('country'))    # Finland
print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None
#We can add new key and value pairs to a dictionary
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
#We can modify items in a dictionary
person['first_name'] = 'Eyob'
#pop(key): removes the item with the specified key name:
#popitem(): removes the last item
#del: removes an item with specified key name
person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_married']        # Removes the is_married item
#The items() method changes dictionary to a list of tuples.
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
#The keys() method gives us all the keys of a a dictionary as a list.
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])
#The values method gives us all the values of a a dictionary as a list.
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])
#We can copy a dictionary using a copy() method. Using copy we can avoid mutation of the original dictionary.
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
#If we don't want the items in a dictionary we can clear them using clear() method
print(dct.clear()) # None
#If we do not use the dictionary we can delete it completely
del dct













