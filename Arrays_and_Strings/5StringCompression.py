"""
1.6 String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3, If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
Hints: #92, if 110
"""


def stringcompressor(usr_str):
    usr_str = str(usr_str).strip()
    res = str()
    if len(usr_str) <= 2:
        return usr_str
    occurances = 1
    for i in range(1, len(usr_str)):
        if usr_str[i] == usr_str[i - 1]:
            occurances += 1
        if usr_str[i] != usr_str[i - 1]:
            res = res + str(occurances) + usr_str[i - 1]
            occurances = 1
    res = res + usr_str[-1] + str(occurances)
    if len(res) >= len(usr_str):
        return usr_str
    return res


print(stringcompressor(input("String ")))

