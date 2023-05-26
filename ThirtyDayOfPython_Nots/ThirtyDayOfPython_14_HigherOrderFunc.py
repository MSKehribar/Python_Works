import os                           #Terminal temizlemek için
os.system('cls||clear')


#Higher Order Functions ---------------------------------------

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20



## Let us implement the example above with a decorator
'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON




def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')



#Bu bölümde ele aldığımız yerleşik yüksek dereceli işlevlerden bazıları map(), filter ve reduce'dur. 
#Lambda işlevi parametre olarak geçirilebilir ve lambda işlevlerinin en iyi kullanım durumu harita, 
# filtre ve azaltma gibi işlevlerdedir.


# map(function, iterable)       map() işlevi, bir işlevi alan ve parametre olarak yinelenebilen yerleşik bir işlevdir.
numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]


#  filter(function, iterable)       filter() işlevi, belirtilen yinelemeli (list) her öğe için boolean döndüren belirtilen işlevi çağırır. Filtreleme ölçütlerini karşılayan öğeleri filtreler.
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]


# reduce() fonksiyonu functools modülünde tanımlanmıştır ve bu modülden içe aktarmalıyız. 
# Harita ve filtre gibi, bir işlev ve bir yinelenebilir olmak üzere iki parametre alır. 
# Ancak, başka bir yinelenebilir döndürmez, bunun yerine tek bir değer döndürür.
from functools import reduce
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15



















