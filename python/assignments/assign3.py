'''
Q1) Return array of even rows and odd columns from the following -
    [02,04,06,08,06]
    [23,56,45,10,83]
    [98,12,34,78,78]
    [21,63,78,84,53]

'''

import numpy as np

a = np.array([[2,4,6,8,6],[23,56,45,10,83],[98,12,34,78,78],[21,63,78,84,53]])
result = a[np.arange(a.shape[0]) % 2 == 0, 1::2]
print(result)

'''
Q2) Create a 8*3 array for numbers from 10 to 34 and split the array into 4 parts.
'''

# Create an 8x3 array of numbers from 10 to 34
arr = np.arange(10, 34).reshape(8, 3)

# Split the array into 4 equal parts
part1, part2, part3, part4 = np.split(arr, 4)

print("Part 1:")
print(part1)
print("\nPart 2:")
print(part2)
print("\nPart 3:")
print(part3)
print("\nPart 4:")
print(part4)
