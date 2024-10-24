name="this is yash\n"
age ='he is 23 right "now", but in the next year he will be 24\n'
relationship ='''he is single from last one year\n'''

print(name)
print(age)
print(relationship)

for character in name:
    print(character)


for letter in age:
    print(letter)

#important : fstring

value="yash"
age=25

val=f"my name is {value} and my age is {age}" 
print(val)

# docstrings in python

def NumTwoDigit(n):
    ''' take 2 numbers and multiply of it'''  #docstring is not a comments
    return (n*5)

print(NumTwoDigit(5))
print(NumTwoDigit.__doc__)


# strings method or different type of function

a="yash is lonely !!!!"
print(a)
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("lonely","not lonely anymore"))

#  split() it convert your string into list
print(a.split(" "))

# to convert a string into heading
print(a.capitalize())

# to make space between yor string or you can say put your into center
str="this is a string"
print(len(str))
print(str.center(50))
#count => this method returns number of times the given value has occured
str1="this is not good for this is what happens"
print(str1.count("this"))

# endswitch method check if the string end with a given value
print(str.endswith("string"))
print(str.find("a"))
print(str.index("string"))
# string contain only A-Z,a-z,0-9
print(str.isalnum())
# string contain only A-Z,a-z
print(str.isalpha())