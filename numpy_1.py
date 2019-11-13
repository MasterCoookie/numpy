'''Learnin to use numpy.

Numpy is used to work on multi-dmientional array and is much faster than lists.
Its faster for a number of reasons like all the elements are the same type or each element
doesnt have properties like size or num of references. The numpy arrays also use
Contiguous memory (the pointers are tidly oredered one next to each other).

Note:
axis=0 -> y axis (up-down)
axis=1 -> x axis (left-right)'''
import numpy as np

# a cool example of what we can do with numpy
A = np.array([1, 3, 5])
B = np.array([1, 2, 3])

print(A * B)

#creating two-dimentional arrays
TWO_D = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(TWO_D)

# checking the num dimentions
print('Dimentions:', TWO_D.ndim)

# checking the shape (how many cols and rows)
print('Shape:', TWO_D.shape)

# getting a specific element - [row, col], negative notation work as well
print(TWO_D[1, 5])

# getting specific row/col
print(TWO_D[0, :], TWO_D[:, 1])

# 3-d arrays
THREE_D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(THREE_D)

# get specific element of 3-d (work outside in)
print(THREE_D[0, 1, 1])

# replacing sequence
THREE_D[:, 1, :] = [[9, 9], [8, 8]]
print(THREE_D)

# all 0s matrix, just cpecify shape
print(np.zeros((2, 3)))

# array of random floats
print(np.random.rand(4, 2))

# array of random ints
print(np.random.randint(10, size=(3, 3)))

# random exercise
EXC = np.zeros((5, 5))
EXC[0] = 1
EXC[-1] = 1
EXC[:, 0] = 1
EXC[:, -1] = 1
EXC[2, 2] = 9

print(EXC)

# be careful while copying! Those are NOT lists!
A = np.array([1, 2, 3])
B = A
B[0] = 100
print(A, B)
# use A.copy()

# u can do all the mathematics quite easy
maths = np.array([1, 2, 3, 4])
maths += 2 # works with - / *, powers etc
print(maths)

# works with other arrays too
maths_2 = np.array([2, 2, 0, 1])
maths -= maths_2
print(maths)

# the mins and max work same as usual
print(np.max(maths))

# summing the entire array
print(np.sum(maths_2))

# reorganizing
before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(before)

after = before.reshape((4, 2))
print(after)

# vertical stacking (just as it sounds, u stack one array on top of another)
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

# args: what on top of what
stacked = np.vstack([v1, v2])

print(stacked)

# horizontal is rather simmilar
h1 = np.ones((2, 4))
h2 = np.zeros((2, 2))

stacked = np.hstack([h1, h2])

print(stacked)

# some random stuff
# read from file
filedata = np.genfromtxt('data.txt', delimiter=',')
#change data type
filedata = filedata.astype('int32')

print(filedata)

# boolean masking
print(filedata > 50)

# a somewhat simmilar function
# any works like "OR", all works like "AND"
print(np.any(filedata > 50, axis=0))
print(np.all(filedata > 50, axis=0))

# now thats a cool thing: indexing by boolean
print(filedata[filedata > 50])

# a reason why this works is that u can index with lists in numpy
A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(A[[1, 2, -1]])

# quick exercise
arr = []
for index in range(1, 31):
    arr.append(index)

arr = np.array(arr).reshape(6, 5)

print(arr[2:4, 0:2])
print(arr[[0, 1, 2, 3], [1, 2, 3, 4]])
print(arr[[0, 4, 5], 3:5])
