"""
is: Returns true if both variables are the same object(x is y)
is not: Returns true if both variables are not the same object(x is not y)
in: Returns True if the queried list contains a certain item(x in y)
not in: Returns True if the queried list doesn't have a certain item(x in y)    

Bu seçeneklerin yerine eşitlik ifadelerinin kullanilmasi tavsiye edilir."""
print('1 is 1', 1 is 1)                   # True - because the data values are the same ==
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2 !=
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string 
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type
# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b
print(total) 
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)