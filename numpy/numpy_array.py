import pprint

import numpy as np

arr1 = np.array((1,2,3,4,5))
"""
    we can give dimensions as well
"""
# arr1 = np.array((1,2,3,4,5), ndmin = 3)
arr2 = np.array([[1,3,5,7,9],[2,4,6,8,10]])
# arr3 = np.array([[[1,2],[3,4],[9,10]],[[5,6],[7,8]]]) # The shape should be consistent
arr3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
arr4 = np.array([1,2,3,4],ndmin=4)

print("Array1")
print("------")
pprint.pprint(arr1)

print("\nArray2")
print("------")
pprint.pprint(arr2)

print("\nArray3")
print("------")
pprint.pprint(arr3)

print("\nMore attributes:")
print("Array1 dimension:",arr1.ndim)
print("Shape of array3:",arr3.shape) # Shape gives, planes, rows and columns
print("Shape of aray4:",arr4.shape) # Shape gives cube, plane, rows, columns
print(f"Array1 datatype: {arr1.dtype}")
print(f"Array1 Item size: {arr1.itemsize}")

