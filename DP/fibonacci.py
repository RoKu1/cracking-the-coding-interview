# # # Think about how to do it for 1 case that is F(2) --> to F(n)
# # N = int(input("Enter N "))
# # a = 0
# # b = 1
# # for i in range(1,N-1):
# #     c = a + b
# #     a = b
# #     b = c
# #
# # print(c)
# # # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
#
# # testcases = int(input())
# k1 = [[4, 3]]
# l1 = [[3, 2], [3, 3], [3, 4], [4, 2], [4, 4], [5, 2], [5, 3], [5, 4]]
# l2 = [[2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [3, 1], [3, 5], [4, 1], [4, 5], [5, 1], [5, 5], [6, 1], [6, 2], [6, 3],
#       [6, 4], [6, 5]]
# l3 = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 0], [2, 6], [4, 0], [4, 6], [3, 0], [3, 6], [5, 0],
#       [5, 6], [6, 0], [6, 6],
#       [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6]]
# l4 = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7],
#       [7, 7], ]
#
#
# # off_limits = list()
#
#
# def blocker(arr1, arr2, dif):
#     global off_limits
#     if dif == 0:
#         off_limits = off_limits + arr1
#         return
#     else:
#         off_limits = off_limits + arr1
#         for i in range(dif):
#             off_limits = off_limits + [[arr2[i][0], arr2[i][1]]]
#
# def print_board():
#     # global off_limits, k1
#     # print(off_limits)
#     for i in range(8):
#         for j in range(8):
#             if [i, j] in k1:
#                 print('O', end='')
#             elif [i, j] in off_limits:
#                 print('X', end='')
#             else:
#                 print('.', end='')
#         print('')
#
#
# for case in range(1, 9):
#     k = case
#     global off_limits
#     off_limits = list()
#     if k == 1:
#         blocker(l1, [], 0)
#     elif k <= 8:
#         if k == 8:
#             blocker(l2, l1, 1)
#         else:
#             dif = 8 - k + 1
#             blocker(l2, l1, dif)
#
#     elif k <= 24:
#         if k == 24:
#             blocker(l3, l2, 1)
#         else:
#             dif = (8 + 16) - k + 1
#             blocker(l3, l2, dif)
#
#     elif k <= 48:
#         if k == 48:
#             blocker(l4, l3, 1)
#         else:
#             dif = (8 + 16 + 24) - k + 1
#             blocker(l4, l3, dif)
#     else:
#         dif = 64 - k
#         blocker([], l4, dif)
#
#     print_board()
#     print('\n')
#     del off_limits

testcases = int(input())
for case in range(testcases):
    n,noc = input().split()
    n = int(n)
    noc = int(noc)
    print(n+1)
    l = list(map(int, input().split(' ')))
    l.sort(reverse=True)
    print(l)
    days = 0
    while n>0:
        days += 1
        if noc in l:
            n -= 1
            l.remove(noc)
            noc = noc * 2
        else:
            if l[0] > noc:
                noc *= 2
            elif any(l) < noc:
                noc = 2 * l[any(l) < noc]
                n -= 1
                l.remove(l[any(l) < noc])
            else:
                noc = l[0]*2
        print(noc)
    print(days)