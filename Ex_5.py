# Exercise 5: Nested Lists
import numpy as np
# 1.Create a nested list representing a matrix and perform matrix addition.
array_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# array_2 = np.array([[6,5,4],[7,8,9],[3,2,1]])
# add_array = np.add(array_1,array_2)

# print(f"Add 2 matrix: \n {add_array} ")

# 2.Write a program to flatten a nested list.

# flatten_array = array_1.flatten()
# print(f"flatten array : {flatten_array} ")

# 3.Implement a function to find the transpose of a matrix.
trans = array_1.transpose()
print(f"array_1: \n {array_1}")
print(f"transposed array: \n {trans}")