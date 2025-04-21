from pprint import pprint as show
import numpy as np

arr1 = np.zeros(3,dtype=int) # 3 columns
arr2 = np.zeros([3,4],dtype=int) # 3 rows, 4 columns
arr3 = np.zeros([3,4,5],dtype=int) # 3 planes, 4 rows, 5 columns
show(arr1)
show(arr2)
show(arr3)

arr4 = np.ones(3, dtype=int) # same as np.zeroes
show(arr4)

arr5 = np.empty(3)
show(arr5)

arr6 = np.eye(3,5, dtype=int) # it will create identity matrix (but we can give more dimesions as well)
show(arr6)

arr7 = np.diag([1,2,3,4,5])
show(arr7)

arr8 = np.arange(0,10)
# arr8 = np.arange(0,10,2) # in this output will be 0,2,4,6,8
show(arr8)

arr9 = np.linspace(0,10,num=5) # array between 0 and 10 with num as number of elements (an AP in short)
show(arr9)