"""
1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
Hints: #17, #74, #102
"""
import numpy as np


def zeromatrix(mat, n, m):
    mat = np.array(mat)
    zerorows = list()
    zerocols = list()
    for i in range(0, n):
        for j in range(0, m):
            if mat[i][j] == '0':
                if i not in zerorows:
                    zerorows.append(i)
                if j not in zerocols:
                    zerocols.append(j)
    for row in zerorows:
        mat[row][:] = '0'
    for i in range(0, n):
        for j in range(0, m):
            if j in zerocols:
                mat[i][j] = '0'
    print(mat)


n, m = input("Enter N and M of NXM matrix ").split(' ')
n = int(n)
m = int(m)
mat = list()
for i in range(0, n):
    row = input("Enter " + str(i) + "Row").split(' ')
    mat.append(row)
mat = np.array(mat)

zeromatrix(mat, n, m)
