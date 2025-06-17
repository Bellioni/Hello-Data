#Copy this code into Colag and execute it. Study the structure of the for loops here.

import numpy as np
#These line are examples of looping
#looping a 1d array
arr1 = np.array([1, 2, 3, 4])
#print the array
print(arr1)
#display the shape(dimensions) of the array
print( np.shape(arr1) )

#loop through the 1 dimensional array
for i in range(np.shape(arr1)[0]):
    print(arr1[i])

# This is an example of a two dimensional array
arr2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr2)
print( np.shape(arr2) )

#two nested loops to access all elements of
# the two dimensional array ar2
for ii in range(np.shape(arr2)[0]):
    for jj in range(np.shape(arr2)[1]):
        print(arr2[ii,jj])
        
