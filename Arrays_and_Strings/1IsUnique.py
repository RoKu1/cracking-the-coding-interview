"""
1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
Solution ->
    First we need to consider the charcter set --> unicode OR ascii --> also how many chars are there like 128,256 etc
    first solve it using a datastructure --> simple...use map/dictionary
    Then solve it withoue using DS -> in this case we need to consider the Time Complexity of Algo we write
"""
'''
We are assuming that this string is a Unicode with 256 chars at max -> extended ascii
'''
'''
By using a additional DataStructure
'''


def checkunique(usr_str):
    my_dict = dict()
    for char in usr_str:
        if my_dict.get(char):
            return False
        my_dict[str(char)] = 1
    return True


'''
Without using a additional DataStructure
O(n^2) --> Time
O(1) --> Space
'''


def checkunique2(usr_str):
    for i in range(0, len(usr_str)):
        for j in range(0, len(usr_str)):
            if i != j and usr_str[i] == usr_str[j]:
                return False
    return True


'''
Without using a additional DataStructure
O(nlogn) --> Time
O(1) --> Space 
'''


def checkunique3(usr_str):
    usr_str = sorted(usr_str)
    for i in range(0, len(usr_str)):
        j = i + 1
        if j != len(usr_str):
            if usr_str[i] == usr_str[j]:
                return False
    return True


'''
Without using a additional DataStructure
Using a bit vector
O(n) --> Time
O(1) --> Space 
'''


def checkunique4(usr_str):
    currentstringinbits = 0  # saying we have 256 chars to represent it would be 8bits
    for char in usr_str:
        print(bin(currentstringinbits))
        if currentstringinbits & (1 << ord(char)) > 0:
            return False
        currentstringinbits = currentstringinbits | (1 << ord(char))
    return True


inp_str = input("Enter String \n")
if checkunique4(inp_str):
    print('Unique')
else:
    print('Not Unique')
