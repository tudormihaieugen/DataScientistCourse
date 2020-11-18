import numpy as np
import pandas as pd
import math
import timeit


# create arrays commands
print(np.ones(10))  # array with 10 elements equal to 1.0
print(np.random.random(10))  # array with 10 random elements between 0-1
print(np.random.rand(10, 3))  # matrix 10x3 with elements between 0-1
print(np.empty(5))  # an array with elements aprox 0, but not 0
print(np.full(3, 7))  # an array with 3 elements equals to 7
print(np.full((3, 3), 8))  # a 3x3 matrix with all elements equal to 8
print(np.zeros(8))  # an array with 8 elements equal to 0.0

a = np.linspace(1, 2)  # an array with 50 elements from 1 to 2
print(len(a))
a = np.linspace(1, 2, num=10)  # an array with 10 elements from 1 to 2
print(a)
a = np.linspace(1, 2, num=10, endpoint=False)  # an array with 10 elements from 1 to 2, but the last element < 2
print(a)
b = np.linspace(1, 2, num=9, endpoint=False, retstep=True)  # retstep shows the step at the end of the array
print(b)

print(np.arange(10))  # an array with elements from 0 to 9 ordered
print(np.arange(2, 29))  # an array with elements from 2 to 28 ordered
print(np.arange(10.0))  # float values

print(np.eye(2, dtype=int))  # identity matrix 2x2 integer
print(np.eye(3, k=2, dtype=float))  # identity matrix 3x3 but from 2 positions to right
print(np.identity(3))  # identity matrix 3x3 float

x = np.random.random(10)
print(np.exp(x))  # exponential
print(np.sqrt(x))  # root
print(np.cos(x))  # cosine
print(np.log(x))  # logarithm

c = 10
d = 20
print(np.dot(c, d))  # multiply c * d as numbers
c = np.array([1, 2, 0])
d = np.array([3, 0, 7])
print(np.dot(c, d))  # multiply c * d as arrays and than sum the numbers
# c and d must have the same length

example_array = np.array([1, 2, 3, 4.0, -3, 4, 8, 4, 9, 0])
print(example_array.sum())  # return the sum of the elements
print(example_array.min())  # return the min
print(example_array.cumsum())  # return the cumulative sum
print(example_array.mean())  # sum / number of numbers
print(np.median(example_array))  # the middle index value
print(np.corrcoef(example_array))  # correlation coefficient
print(np.std(example_array))  # standard deviation


# example
np.random.seed(0)
x1 = np.random.randint(10, size=6)  # 6 random values from 0 to 10 integers
print(x1)
x2 = np.random.randint(10, size=(3, 4))  # 3x4 matrix
print(x2)
x3 = np.random.randint(10, size=(3, 4, 5))  # 3x4x5 matrix
print("x3 ndim:", x3.ndim)  # print 3
print("x3 shape:", x3.shape)  # print 3, 4, 5
print("x3 size:", x3.size)  # print 60 (full size)
print("x3 dtype:", x3.dtype)  # int32
print("x3 itemsize:", x3.itemsize, "bytes")  # 4 bytes for one item
print("x3 nbytes:", x3.nbytes, "bytes")  # 240 bytes for all items

print(x1)
print(x1[1])
print(x1[-2])
x1[3] = 3.1415
print(x1)  # the element with index 3 will pe truncated


# big_array = np.random.rand(10000000)
# %timeit sum(big_array)
# %timeit np.sum(big_array)


# pandas example
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98]}
data1 = pd.DataFrame(dict)
print(data1)
