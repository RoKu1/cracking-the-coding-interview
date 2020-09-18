"""
1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
Solution ->
    First we have to ask for char set --> unicode/ascii  --> know your data
    Then we need to know the details  like....
        1. Is this Case Sensitive/Insensititve
        2. Does white sapce matters or is it to be ignored
"""
"""
Solution for
1->Case matters
2->White sapce matters --> "god  " not same as "dog"  // if allowed write line to strip strings of white spaces
"""

"""
Solution1 --> O(nlogn)
"""


def checkpermu(usr_str1, usr_str2):
    usr_str1 = sorted(usr_str1)
    usr_str2 = sorted(usr_str2)
    if len(usr_str1) != len(usr_str2):
        return False
    for i in range(0, len(usr_str1)):
        if usr_str2[i] != usr_str1[i]:
            return False
    return True


"""
Solution1 --> O(n)
"""


def checkpermu2(usr_str1, usr_str2):
    d1 = dict()
    d2 = dict()
    if len(usr_str1) != len(usr_str2):
        return False
    for char in usr_str1:
        if d1.get(char):
            d1[char] += 1
        else:
            d1[str(char)] = 1

    for char in usr_str2:
        if d2.get(char):
            d2[char] += 1
        else:
            d2[str(char)] = 1

    for char in usr_str1:
        if d1.get(char) != d2.get(char):
            return False
    return True


inp_str1 = input("Enter String1 \n")
inp_str2 = input("Enter String1 \n")

if checkpermu(inp_str1, inp_str2):
    print('Is Permutation')
else:
    print('Not Permutation')

if checkpermu2(inp_str1, inp_str2):
    print('Is Permutation')
else:
    print('Not Permutation')

