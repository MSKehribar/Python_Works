#### Unpacking characters 
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P ...
print(f) # n

# Accessing characters in strings by index
first_letter = language[0]
last_letter = language[len(language) - 1]
last_letter = language[-1]

# Slicing
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
last_three = language[3:6]  # hon
last_three = language[-3:]  # hon
last_three = language[3:]   # hon

# Skipping character while splitting Python strings
language = 'Python'
pto = language[0:6:2]  #=="pto" (0'dan 6'ya 2'ser aralıkla seç)
print(pto) # 

"""
\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")
"""

## format()	formats string into nicer output  ***************************************************************  
first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result) # The area of circle with 10 is 314.0


## String Methods
challenge = 'thirty days of python'# capitalize(): Converts the first character the string to Capital Letter
print(challenge.capitalize()) # 'Thirty days of python'

challenge = 'thirty days of python'# title(): Returns a Title Cased String
print(challenge.title()) # Thirty Days Of Python
  
challenge = 'Thirty Days Of Python'# swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

challenge = 'thirty days of python'# count(): returns occurrences of substring in string, count(substring, start=.., end=..)
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th')) # 2`

challenge = 'thirty days of python'# startswith(): Checks if String Starts with the Specified String
print(challenge.startswith('thirty')) # True
challenge = '30 days of python'
print(challenge.startswith('thirty')) # False

challenge = 'thirty days of python'# endswith(): Checks if a string ends with a specified ending
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

challenge = 'thirty\tdays\tof\tpython'# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

challenge = 'thirty days of python'# find(): Returns the index of first occurrence of substring, if not found returns -1
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

challenge = 'thirty days of python'#rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
print(challenge.rfind('y'))  # 5
print(challenge.rfind('th')) # 1

challenge = 'thirty days of python'#index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.
sub_string = 'da'
print(challenge.index(sub_string))  # 7
#print(challenge.index(sub_string, 9)) # error

challenge = 'thirty days of python'#rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
sub_string = 'da'
print(challenge.rindex(sub_string))  # 8
#print(challenge.rindex(sub_string, 9)) # error

challenge = 'ThirtyDaysPython'# isalnum(): Checks alphanumeric character
print(challenge.isalnum()) # True
challenge = '30DaysPython'
print(challenge.isalnum()) # True
challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character
challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

challenge = 'thirty days of python'# isalpha(): Checks if all characters are alphabets(a-z and A-Z)
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

challenge = 'Thirty'# isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True

num = '10'# isdecimal():Checks decimal characters(0-9)
print(num.isdecimal()) # True
num = '10.5'
print(num.isdecimal()) # False

challenge = '30DaysOfPython'# isidentifier():Checks for valid identifier means it check if a string is a valid variable name
print(challenge.isidentifier()) # False, because it starts with a number

challenge = 'thirty days of python'# islower():Checks if all alphabets in a string are lowercase
print(challenge.islower()) # True

challenge = 'thirty days of python'# isupper(): returns if all characters are uppercase characters
print(challenge.isupper()) #  False

num = '10'# isnumeric():Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
print(num.isnumeric())      # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
print('ten'.isnumeric())    # False

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']# join(): Returns a concatenated string
result = '#, '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

challenge = ' thirty days of python '# strip(): Removes both leading and trailing characters
print(challenge.strip('y')) # 5

challenge = 'thirty days of python'# replace(): Replaces substring inside
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

challenge = 'thirty days of python'# split():Splits String from Left
print(challenge.split()) # ['thirty', 'days', 'of', 'python']



