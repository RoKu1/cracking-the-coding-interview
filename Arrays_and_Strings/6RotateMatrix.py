"""
1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

"""
import numpy as np


def rotate(mat, n):
    mat = np.array(mat)
    layers = round(n / 2)
    for i in range(0, layers):
        firstel = i
        lastel = n - i - 1
        for j in range(firstel, lastel):
            top = mat[firstel][j]
            # left = mat[lastel - j - firstel][firstel]  # (3-0),(3-1),(3-2),(3-3)
            # bottom = mat[lastel][lastel - j - firstel]
            # right = mat[j][lastel]
            mat[firstel][j] = mat[lastel - j - firstel][firstel]  #left
            mat[lastel - j - firstel][firstel] = mat[lastel][lastel - j - firstel]  #bottom
            mat[lastel][lastel - j - firstel] = mat[j][lastel] #right
            mat[j][lastel] = top
    print(mat)


n = int(input("Enter N of NXN matrix "))
mat = list()
for i in range(0, n):
    row = input("Enter " + str(i) + "Row").split(' ')
    mat.append(row)
mat = np.array(mat)
rotate(mat, n)
