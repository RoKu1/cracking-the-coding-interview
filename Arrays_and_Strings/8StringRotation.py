"""
1.9 String Rotation; Assume you have a method i s S u b s t r i n g which checks if one word is a substring
of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
call to i s S u b s t r i n g (e.g.,"waterbottle" is a rotation o f ' e r b o t t l e w a t " ) .

"""
s1 = input("First String")
s2 = input("First String")
if s2 in s1+s1:
    print("Yes")
else:
    print("No")