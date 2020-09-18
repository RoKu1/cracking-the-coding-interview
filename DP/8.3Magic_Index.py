"""
8.3 Magic Index: A magic index in an array A [ 0 . . . n - 1 ] is defined to be an
index such that A [ i ] = i. Given a sorted array of distinct integers, write a method
to find a magic index, if one exists, in array A.
FOLLOW UP
What if the values are not distinct?
"""

arr = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12]


# -->for distinct
def Magic_Index(strt, end, arr):
    mid = (strt + end) // 2
    # print(strt, end=' ')
    # print(end)
    if strt > end:
        return -1
    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        return Magic_Index(mid + 1, end, arr)
    elif arr[mid] > mid:
        return Magic_Index(strt, mid - 1, arr)


print(Magic_Index(0, len(arr) - 1, arr))



arr1 = [-10 ,-1, 2, 2, 2, 3, 4, 7, 9, 12, 13]
# for non-distinct -->

'''
Here we check the left side as well ...but we can be sure that the min(current_Mid,Mid_Index) 
would be the end for the left array,,,as it is the value that can not be beat in index matching 
'''
def Magic_Index1(strt,end,arr):
    # print(strt, end=' ')
    # print(end)
    if strt > end:
        return -1

    midindex = (strt + end) // 2
    midvalue = arr[midindex]

    if midvalue == midindex:
        return midindex

    # left search
    leftind = min(midvalue,midindex-1)
    leftsol =  Magic_Index(strt, leftind, arr)
    if leftsol >= 0:
        return leftsol

    # right search
    rightind = max(midindex+1,midvalue)
    rightsol =  Magic_Index(rightind, end, arr)
    return  rightsol

print(Magic_Index1(0, len(arr1) - 1, arr1))
