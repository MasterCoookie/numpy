'''Learnin to use numpy.

Numpy is used to work on multi-dmientional array and is much faster than lists.
Its faster for a number of reasons like all the elements are the same type or each element
doesnt have properties like size or num of references. The numpy arrays also use
Contiguous memory (the pointers are tidly oredered one next to each other).'''
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
a = np.array([1, 2, 3])
b = a
b[0] = 100
print(a, b)
# use a.copy()
