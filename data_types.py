# datatypes: int, float, str, list, dict, tup, set, bool

# basic math operations

2+2
2-1
2*2
3/2

# mod modulo

7 % 4
50 % 5
23 % 2

# powers

2**3

# order of ops

2 + 10 * 10 + 3


# variables

a = 5
a = 10
a + a
a = a + a
type(a)
a = 30.1
type(a)
my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate


# strings

'hello'
"hello"
'this is also a string'
"I'm going for a run"
print('hello')
"Hello world one"
'hello world two'
print('hello world one')
print('hello world two')
print('hello \nworld')
print('hello \tworld')
len('hello')
len('I am')


# string indexing and slicing

mystring = 'hello world'
mystring[0]
mystring[8]
mystring[9]
mystring[-2]

mystring = 'abcdefghijk'
mystring[2:]
mystring[:3]
mystring[3:6]
mystring[1:3]

mystring[::2]
mystring[2:7:2]
mystring[::-1]

# strings are immutable

name = 'Sam'
# name[0] = 'P'  nie da sie
last_letters = name[1:]
'P' + last_letters
# string concatenation
x = 'hello world'
x + ' it is beautiful day'
letter = 'z'
letter * 10

2+3
"2" + "3"

# str methods
x = 'hello world'
x.upper()
x.isdigit()  # etc
x.split()
x = 'hi this is a sctring'
x.split('i')


# print formatting

print('this is a string {}'.format('inserted'))
print('the {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('the {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

result = 100/777
print('Result was: {r:10.3f}'.format(r=result))

name = 'Jose'
print(f'hello his name is {name}')
name = 'Sam'
age = 3
print(f'{name} is {age} years old')


# lists

my_list = [1, 2, 3]
my_list = ['string', 100, 23.2]
len(my_list)
mylist = ['one', 'two', 'three']
mylist[0]
mylist[1:]
another_list = ['four', 'five']
new_list = mylist + another_list
new_list[0] = 'ONE ALL CAPS'
new_list.append('six')
new_list.pop()
new_list.pop(0)
new_list = ['a', 'b', 'x', 'c', 'd']
num_list = [1, 4, 3, 7]
new_list.sort()
num_list.sort()
num_list.reverse()


# dictionaries

my_dict = {'key1': 'value1', 'key2': 'value2'}
my_dict['key1']
prices_lookup = {'apple': 2, 'oranges': 3, 'milk': 5.50}
prices_lookup['apple']
d = {'k1': 123, 'k2': ['a', 'b', 'c'], 'k3': {'insideKey': 100}}
d['k2']
d['k3']['insideKey']
d['k2'][2]

mylist = ['k2']
letter = mylist[2]
letter.upper()

d['k2'][2].upper()

d['k4'] = 300
d['k1'] = 'new value'

d.keys()
d.values()
d.items()


# tuples

t = (1, 2, 3)
mylist = [1, 2, 3]
len(t)
t = {'one', 2, 3.0}
t[0]
t[-1]
t = ('a', 'a', 'b')
t.count(a)
t.index(a) # first time it appears in tuple

mylist[0] = 'new'
# t[0] = 'mew' # cant do that


# sets

myset = set()
myset.add(1)
myset.add(2)
myset.add(2) # only unique values
mylist = [1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]
set(mylist)


# boolean (bool)

True
False
type(False)
1 > 2
1 == 1
b = None


# files, input, output

myfile = open('myfile.txt')
myfile.read()
myfile.seek(0) # resets cursor
myfile.read()
contents = myfile.read()

myfile.readlines()

myfile = open("C:\\users\\myfile.txt")
myfile = open("/Users/myfile.txt")

pwd

myfile.close()

myfile = open('myfile.txt')

with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()

#  r-read, w-write, a-append, r+-reading and writing, w+-writing and reading

with open('myfile.txt', mode='r') as myfile:
    contents = myfile.read()

with open('myfile.txt', mode='w') as myfile:
    contents = myfile.read()

with open('myfile.txt', mode='a') as myfile:
    contents = myfile.read()

with open('my_new_file.txt', mode='r') as f:
    print(f.read())

with open('my_new_file.txt', mode='a') as f:
    f.write("\nfour")

with open("newfile.txt", mode='w') as f:
    f.write("I made this")

with open('newfile.txt', mode='r') as f:
    print(f.read())
    # I made this


#