"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr 3ohn Smith"
Output: "Mr%203ohn%20Smith"
"""


def urlify(usr_str):
    return str(usr_str).replace(' ', '%20')


# inp_str = input("Enter String \n")
print(urlify(input("Enter String \n")))
