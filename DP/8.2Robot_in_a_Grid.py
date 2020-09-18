# 8.2 Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
# The robot can only move in two directions, right and down, but certain cells are "off limits" such that
# the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
# the bottom right.
# | R |   |   |
# |   | N |   |
# |   |   |   |
# |   |   | E |


# row = int(input("Number of rows\n"))
# col = int(input("Number of cols\n"))

"""
 off_limit -> list will determine the (row,col) position of all the positions that are not accessible
"""
off_limits = list()

# while True:
#     i, j = input("Enter (row col) that are off limits IF done enter 0,0 \n").split(',')
#     if i == '0' and j == '0':
#         break
#     off_limits.append([int(i), int(j)])

# print(off_limits)\

"""Now we need to implement a solution which is basically a reverse solve for this for the end to strt --> 
    NW(i,j) = NW(i-1,j) + NW(i,j-1) --> look for func count_ways1() it works but is not DP But it will just be a 
    reccurssive solution but we need to use memory to store soln's that we already have --> we will use map """


def count_ways1(i, j):
    if i == 0 and j == 0:
        # print('return 1')
        return 1
    if i < 0 or j < 0:
        return 0
    if [i, j] in off_limits:
        return 0
    else:
        return count_ways1(i - 1, j) + count_ways1(i, j - 1)


"""
Using the memory now--> we use a map to store soln's that could be used
"""

cords = list()
sols = list()

map()


def count_ways(i, j):
    if [i, j] in cords:
        print(sols[cords.index([i, j])])
        return sols[cords.index([i, j])]

    if i == 0 and j == 0:
        cords.append([i, j])
        sols.append(1)
        # print('return 1')
        return 1
    if i < 0 or j < 0:
        cords.append([i, j])
        sols.append(0)
        return 0
    if [i, j] in off_limits:
        cords.append([i, j])
        sols.append(0)
        return 0

    else:
        ans = count_ways(i - 1, j) + count_ways(i, j - 1)
        cords.append([i, j])
        sols.append(ans)
        return ans


# print(count_ways1(row-1,col-1))
off_limits.append([1, 1])
print(count_ways(10, 10))


print(count_ways1(10, 10))
