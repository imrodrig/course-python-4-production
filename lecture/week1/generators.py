"""
Generators - https://wiki.python.org/moin/Generators
"""

## Build a list and return it: 
## not a generators - it uses return, not yield
def first_n(n):
    '''Build and return a list'''
    num, nums = 0, []
    while num < n:
        nums.append(num)  # note it builds the full list in memory.
        num += 1
    return nums

sum_of_first_n = sum(first_n(100))
print ("Result from list:", sum_of_first_n)


## Now using a generator (function) that yields items instead of returning a list

def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1   # note the counter is being incremented

## when the functio firstn is invoked, it returns each element of 
## the list per iteration, without having to build the entire 
## list in memory.
sum_of_first_n = sum(firstn(10000000))
print ("Result from generator:", sum_of_first_n)

# gen the first n fibonnaci numbers
for _ in range(10):
    print(next(sum_of_first_n))

## Generators with the next keyworkd
def even_numbers():
    num = 0 
    while True:
        yield num
        num += 2

## we create a generator object by calling the generator function
## and name it even_gen
even_gen = even_numbers()
print (even_gen)
# Get the first 5 numbers
for _ in range(5):
    print(next(even_gen))

print("now restart printing:")
## Must recreate the object?
even_gen = even_numbers()
for _ in range(10):
    print(next(even_gen))

# =============================================================================
# Using next with default value
# =============================================================================
def limited_alphabet(limit):
    for i in range(65, 65 + limit):
        yield chr(i)

alphabet_gen = limited_alphabet(5)

print(next(alphabet_gen, "End of sequence"))
print(next(alphabet_gen, "End of sequence"))
print(next(alphabet_gen, "End of sequence"))
print(next(alphabet_gen, "End of sequence"))
print(next(alphabet_gen, "End of sequence"))





# Comprehensions: concise way to create lists, dictionaries, and sets
# using a single line of code

# 4 types of comprehensions: 
### - List comprehensions
### - Dictionary comprehensions
### - Set comprehensions
### - Generator comprehensions

## list comprehension
doubles = [2 * n for n in range(5)]  
print(doubles)

# same as the list comprehension above
doubles = list(2 * n for n in range(5))
print (doubles )
sum_of_doubles = sum(doubles)
print(sum_of_doubles)

## Cannot do this. doubles is a list, no iterator.
doubles = [2 * n for n in range(5)]  
for _ in range(5):
    print(next(doubles))

## creating other LIST comprehensions
numbers = [1, 2, 3, 4, 5]
numbers = [n for n in range(5)]
squares = [x * x for x in numbers if x % 2 == 0 ]
print(squares)

# list comprehensions with multiple for loops: 
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print (type(matrix), matrix)
flattened = [num for row in matrix for num in row ]
flattened2 = [n for r in matrix for n in r ]
print(type(flattened), flattened)
print(type(flattened), flattened2)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_element = [10, 11, 12]
print (type(matrix), matrix)
matrix.append(new_element)
print (type(matrix), matrix)

## Print list elements
n = 0
while n < len(matrix):
    print(matrix[n])
    n += 1

## loop through a list with for
for x in matrix:
    print(x)

## loop through a list with index number
for i in range(len(matrix)):
    print(matrix[i])

## Looping with list comprehension
print("Now using comprehension:")
[print(x) for x in matrix]


# Printing only some rows
print("Now printing only rows with the number 1")
newmatrix = [x for x in matrix if 1 in x]
print(newmatrix)

# Dictionary comprehensions
words = ['apple', 'banana', 'orange']
word_lengths = {word: len(word) for word in words)}
print(word_lengths)


# =============================================================================
# Set Comprehensions
# =============================================================================
input_list = ['LARGE WHITE HEART OF WICKER', 
              'MEDIUM CERAMIC TOP STORAGE JAR', 
              'POLKADOT JAR', 
              'RED T-SHIRT', 
              'Red T-shirt'
              ]
output_set = {word.lower() 
              for sentence in input_list 
              for word in sentence.split()
              }
print(output_set)  
# Output: {'large', 'white', 'heart', 'of', 'wicker', 'medium', 'ceramic', 
# 'top', 'storage', 'jar', 'polkadot', 'red', 't-shirt'}


## Generator comprehensions - 
## Better than list if dataset is very large
## When using list comprehension the entire list must be able to 
## fit in memory
numbers = [1,2,3,4,5]
squares_generator = (x * x for x in numbers if x % 2 == 0)

for square in squares_generator:
    print(square)



### Higher-Order functions
# -- Storiing a function in a variable
def greet(name):
    return f"hello, {name}!"

greet_func = greet
print(greet_func("John"))

### Higher-Order functions
# -- pass a function as a parameter to another function
def apply_operation(numbers, operation):
    return [operation(num) for num in numbers]

def square(x):
    return x**2

def cube(x):
    return x**3

numbers = [1,2,3,4,5]
print(apply_operation(numbers, square))
print(apply_operation(numbers, cube))


### Higher-Order functions
# Important concept in functional programming
# -- lambda functions: functions without a name
#  these are throwaway functions
# Sort a list of strings by length
strings = ["apple","banana", "cherry","grape",'fig', "date"]
sorted_strings = sorted(strings, key=lambda x: len(x))
print(sorted_strings)

# -- Lambda is powerful when used inside another function
# function below takes one arg, which will be multiplied by an unknown number. 
def myfunc(n):
    return lambda a: a * n 

mydoubler = myfunc(2)
print(mydoubler(11))

a = [[1,6],[2,5],[3,4]]
# sort the list by the first element of each list
as1 = sorted(a, key=lambda y:y[0])
print("Sorted by the first element:", as1)
# now sort by the second element of each list
as2 = sorted(a, key=lambda y:y[-1])
print("Sorted by the last element:", as2)

## Higher-Order functions
## Three common: Map, Filter and Reduce

## MAP function: 
# Convert a LIST of temperatures from Celsius to Fahrenheit
def celsius_to_farenheit(temp):
    return (9/5) * temp + 32

temperature_celsius = [0, 20, 37, 100]
temperature_fahrenheit = list(
    map(celsius_to_farenheit, temperature_celsius)
    )
# to print unformatted float numbers:
print(temperature_fahrenheit)
# to print float numbers with a single decimal
print(["{0:0.1f}".format(i) for i in temperature_fahrenheit])

## FILTER function: 
# Find prime numbers in a list of integers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

numbers = [1,2,3,4,5,6,7,8,9,10]
primes = list(filter(is_prime, numbers))
print(primes)

b = [1,2,3,4]
# function to return TRUE if x is even 
def f(x):
    return x % 2 == 0

# applies the function to all elements in the list and returns
# each result
print(list(map(f,b)))

# applies the function to all elements in the list
# but FILTER the results and returns only the elements for 
# which the function returned True.
def f1(x):
    return x % 2 == 0

print(list(filter(f1, b)))