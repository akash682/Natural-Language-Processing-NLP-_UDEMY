import time

import numpy as np

print(np.arange(10))

print(np.arange(1,10))

print(np.arange(1,10,2))
print(np.arange(1,10,0.5))

print(np.arange(1,10,dtype='float64'))

arr = np.arange(1,10)
print(arr.ndim)

print(arr.shape)

print(arr.size)
print(arr.dtype)
print(arr.itemsize)


print(arr.itemsize * arr.size)


list1 = range(1,1000)
list2 = np.arange(1,1000)

#Important functions in numpy
# List to array
print(np.asarray(([1,2,3,4,5])))

list2d = [[1,2,3],[4,5,6]]
arr2d = np.asarray(list2d)
print(arr2d)


# Generate zeros
# zeros(shape, dtype=float, order ='C')

listzeros = np.zeros((3,4), dtype='int32')
print(listzeros)

print(np.linspace(1,4, num=4))
print(np.linspace(1,4, num=8))
print(np.linspace(1,4, num=8,endpoint=False))


rarr = np.random.random((3,4))
print(rarr)

print(np.max(rarr, axis = 0))
print(np.max(rarr, axis = 1))

print(np.min(rarr, axis = 0))
print(np.min(rarr, axis = 1))

print(np.median(rarr, axis = 0))
print(np.median(rarr, axis = 1))

new_arr = np.reshape(rarr, (12,))
print(new_arr)
print("END")
new_arr = np.reshape(rarr,(12,1))
print(new_arr)

# Slicing
rarr = np.random.random((4,5))

rarr[:,:]
rarr[1:3,:]

rarr[:,1:]
rarr[:,1:3]

rarr[1:3,1:3]

rarr[[0,3],:]
rarr[:,[0,3]]
rarr[:-1,:]
rarr[-1:,:]