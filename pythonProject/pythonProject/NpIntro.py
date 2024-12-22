import numpy as np

#1d array
arr1 = np.array([1, 2, 3, 3, 4])
print(arr1)
print(np.__version__)
print(type(arr1))
#2d arrays
arr2 = np.array([[1, 2, 3], [4, 5, 6],[11,22,33]])
print(arr2)
#3d array
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr3)
#checking dimensions of array
print(f"dimension of arr1 is : {arr1.ndim}")
print(f"dimension of arr2 is : {arr2.ndim}")
print(f"dimension of arr3 is : {arr3.ndim}")
print("Accessig elements from array:\n")
print(arr1[2])
print(f"2nd element of 1st row : {arr2[0,1]}")
print(arr3[0,1,2])
print(np.zeros((3,4)))
arr4=np.full((3,4),5)
print(arr4)
print(np.empty((4,5)))
a=range(1,10)
print(a[6])