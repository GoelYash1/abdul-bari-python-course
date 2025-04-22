import pprint
from pprint import pprint as show

import numpy as np

arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr1 = arr1.reshape(3,4)
show(arr1)
arr1 = arr1.reshape(3,2,2)
show(arr1)

# arr1 = arr1.flatten() Can be used to flatten a list
arr1 = arr1.reshape(12)
# arr1 = arr1.reshape(11) # This will show error
show(arr1)