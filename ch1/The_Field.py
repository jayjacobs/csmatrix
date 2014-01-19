# version code ec40b5e32163+
# Please fill out this stencil and submit using the provided submission script.





## 1: Problem 1.7.1Python Comprehensions: Filtering
def myFilter(L, num): 
	'''
	Input:
	  -L: a list of numbers
	  -num: a number
	Output:
	  -a list of numbers not containing a multiple of num
	Examples:
	  >>> myFilter([1,2,4,5,7],2)
	  [1,5,7]
	  >>> myFilter([10,15,20,25],10)
	  [15,25]
	'''
	return [ x for x in L if x % num]



## 2: Problem 1.7.2Python Comprehensions: Lists of Lists

def my_lists(L):
    '''
    >>> my_lists([1,2,4])
    [[1], [1, 2], [1, 2, 3, 4]]
    >>> my_lists([0,3])
    [[], [1, 2, 3]]
    '''
    return [ list(range(1, x+1)) for x in L ]



## 3: Problem 1.7.3Python Comprehensions: Function Composition
def myFunctionComposition(f, g): 
	'''
	Input:
	  -f: a function represented as a dictionary such that g of f exists
	  -g: a function represented as a dictionary such that g of f exists
	Output:
	  -a dictionary that represents a function g of f
	Examples:
	  >>> f = {0:'a',1:'b'}
	  >>> g = {'a':'apple','b':'banana'}
	  >>> myFunctionComposition(f,g)
	  {0:'apple',1:'banana'}

	  >>> a = {'x':24,'y':25}
	  >>> b = {24:'twentyfour',25:'twentyfive'}
	  >>> myFunctionComposition(a,b)
	  {'x':'twentyfour','y':'twentyfive'}
	'''
	return { x[0]:g[x[1]] for x in f.items() }


## 4: Problem 1.7.4Summing numbers in a list
def mySum(L):
	'''
	Input: 
	  a list L of numbers
	Output:
	  sum of the numbers in L
    Be sure your procedure works for the empty list.
	Examples:
	  >>> mySum([1,2,3,4])
	  10
	  >>> mySum([3,5,10])
	  18
	'''
	current = 0
	for x in L:
		current = current + x
	return current



## 5: Problem 1.7.5Multiplying numbers in a list
def myProduct(L): 
	'''
	Input:
	  -L: a list of numbers
	Output:
	  -the product of the numbers in L
    Be sure your procedure works for the empty list.
	Examples:
	  >>> myProduct([1,3,5])
	  15
	  >>> myProduct([-3,2,4])
	  -24
	'''
	current = 1
	for x in L:
		current = current * x
	return current



## 6: Problem 1.7.6Minimum of a list
def myMin(L): 
	'''
	Input:
	  a list L of numbers
	Output:
	  the minimum number in L
    Be sure your procedure works for the empty list.
    Hint: The value of the Python expression float('infinity') is infinity.
	Examples:
	>>> myMin([1,-100,2,3])
	-100
	>>> myMin([0,3,5,-2,-5])
	-5
	'''
	current = L[0]
	for x in L:
		current = x if x < current else current
	return current



## 7: Problem 1.7.7Concatenation of a List
def myConcat(L): 
	'''
	Input:
	  -L:a list of strings
	Output:
	  -the concatenation of all the strings in L
    Be sure your procedure works for the empty list.
	Examples:
	>>> myConcat(['hello','world'])
	'helloworld'
	>>> myConcat(['what','is','up'])
	'whatisup'
	'''
        # return ''.join(L)
        # okay
	current = ''
	for x in L:
		current = current + x
	return current



## 8: Problem 1.7.8Union of Sets in a List
def myUnion(L): 
	'''
	Input:
	  -L:a list of sets
	Output:
	  -the union of all sets in L
    Be sure your procedure works for the empty list.
	Examples:
	>>> myUnion([{1,2},{2,3}])
	{1,2,3}
	>>> myUnion([{},{3,5},{3,5})
	{3,5}
	'''
	current = set()
	for x in L:
		current = current | x
	return current



## 9: Problem 1.7.10Complex Addition Practice
# Please only enter your numerical solution using Python

complex_addition_a = 5 + 3j
complex_addition_b = 1j
complex_addition_c = -1 + 0.001j
complex_addition_d = 0.001 + 9j



## 10: Problem 1.7.12Combining Complex Operations
#Write a procedure that evaluates ax+b for all elements in L

def transform(a, b, L): 
	'''
	Input:
	  -a: a number
	  -b: a number
	  -L: a list of numbers
	Output:
	  -a list of elements where each element is ax+b where x is an element in L
	Examples:
	>>>transform(3,2,[1,2,3])
	[5,8,11]
	'''
	return [ a*x + b for x in L ]

## 11: Problem 1.7.13GF(2) Arithmetic
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0
