# Programming with python
> Python for scientific computing, Scopatz (Effective computation in physics)

More in: [Scipy Lectures](scipy-lectures.org)

## Fundamentals

### Basic types
  1. Numerical types
  ```Python
    c = 4 #integers
    a = 1.5 + 0.5j #complex
    b = 3 > 4 #Boolean
    # To cast
    float(c)

    3.0 // 2.0 #integer division

    type() #which type
  ```

  To do division like python 3.7 in python 2.7 use `from __future__ import division`

  2. Containers

  **List**
  ```Python
  colors = ["red", "blue", "green", "black","white"]
  colors[2] # prints "green"
  colors[-1] #last value of list
  colors[:] #Slicing(?) all column
  colors[2:4] #In between
  colors[::2] #
  ```
  Everything in `Python ` is an object.

  3. Assignment operator

  `=` is actually **not** an assignment operator but a _"labeling"_ operator.

  `id()` is the operator to see the reference of the object.

  In `Python` the integer 1 is the same in memory, so every object equals to 1 whatsoever would return `== True`

  ```Python
  colors[0] = "yellow" #Assignment
  colors[2] = ["gray","purple"]
  #Replacing [2] and adding to the List
  colors[2:5] = ["yellow","orange"]
  #Replacing in between and adding new elements
  colors.append("pink") #adding element
  colors.pop()
  ```

  **Dictionaries**

  **Tuples**

  You can **not** modify it. The `,` operator is defining the tuple.
  ```Python
  t = (1, 2, 3, "Hello")

  ```
### Control Flow

1. `if/elif/else`

  ```Python

  ```

2. `for/range`

  ```Python

  ```

3. `while/break/continue`

  ```Python

  ```

4. Conditional Expressions

5. Advanced iteration

  ```python
  vowels = "aeiouy"

  for i in "powerful":
    if i in vowels:
      print(i)
  ```

Pythonic way to iterate a tuple whatsoever

```python
words = ("cool", "powerful", "readable")

for index, item in enumerate(words):
  print((index,item))
```

6. List Comprehensions

```python
[i**2 for i in range(4)]
# >> (0,1,4,9)
```
## Defining Functions

```python
def disk_area(radius):

  return 3.14 * (radius**2)

#Since Everything is an object:
area = disk_area
```

Another example:

```python
def add_to_dict(args={"a":1, "b":2}):
  for i in args.keys():
    args[i] += 1
    print(args)
#Mutable ,result is gonna change every time you run code
```

One more:

```python
def try_to_modify(x,y,z):

```

**Variable Number Parameters**

**Docstrings**

```python
def funcname(x):
  """ Info about Functions

  """
```
> Read more about the basics [**Scipy Lectures**](scipy-lectures.org)

# `Numpy`
Provides extension package to python for multi-dimensional arrays, closer to hardware, designed for scientific computation. More info
[Numpy reference documentation](https://docs.scipy.org/doc/)

- Looking for something ` np.lookfor('create array')`, `np.con*?` (search for attributes with _con_)

## Numpy arrays

```python
a = np.array([0, 1, 2, 3])
a = np.array([0, 1, 2, 3], dtype="float")
```
**Why is it useful?** Memory efficient container that provides fast numerical operations.
> Read [numpy](http://scipy-lectures.org/intro/numpy/array_object.html#id1)

#### Functions for creating arrays
```python
# Evenly spaced
a = np.arange(10) # 0 .. n-1  (!)
b = np.arange(1, 9, 2) # start, end (exclusive), step

#Number of points
c = np.linspace(0, 1, 6)   # start, end, num-points
d = np.linspace(0, 1, 5, endpoint=False)

# Common arrays
a = np.ones((3, 3))  # reminder: (3, 3) is a tuple
b = np.zeros((2, 2))
c = np.eye(3)
d = np.diag(np.array([1, 2, 3, 4]))

# Random numbers
a = np.random.rand(4)       # uniform in [0, 1]
b = np.random.randn(4)      # Gaussian
np.random.seed(1234)        # Setting the random seed

```
#### Indexing and slicing
_Indexing_
```python
# Reversing a sequence
a[::-1]

#For multidimensional arrays
a = np.diag(np.arange(3))
a[2, 1] = 10 # third line, second column
```

_Slicing_
```python
a[2:9:3] # [start:end:step]
a[:4] # All but position 4
a[::2] #All array but position 2
a[3:] #Start from position 3
a[:, 2] #all column of position 2
a[4:,4:] #From column 4 all and from row 4 all
a[2::2, ::2]
#from column 2 any other with step 2,all rows from
#selected columns with step 2

```

#### Copies and views
A slicing operation creates a **view** on the original array, meaning the original array is not copied in memory.
> Use `np.may_share_memory()` to check if arrays share same block of memory

```python
a = np.arange(10)
c = a[::2].copy() #Force a copy
```

#### Fancy Indexing
Numpy arrays can be indexed with slices but also with boolean or integer arrays (**masks**). This method is called _fancy indexing_. It creates _copies_ **not** views.

**1.Boolean masks**
```python
np.random.seed(3)
a = np.random.randint(0,21,15)
mask = (a % 3 == 0)
extract_from_a = a[mask] #a[a%3==0]

#indexing with a mask is useful to assign
#new value to subarray
a[a%3==0] = -1
#All values of a mult of 3, change to -1
```

**2. Indexing with an array of integers**
```python

```

## `Matplotlib`: plotting

for 2D-graphics. It provides both a quick way to visualize data from `python` and publication quality figures in many formats.

```python
from matplotlib import pyplot as plt
%matplotlib inline
#for interact there are several other ways

```

`pyplot` provides a procedural interface to the matplotlib object-oriented plotting library. It is modeled closely after _Matlab_ analogs with similar arguments. Important commands are explained with interactive examples.
