"""
1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True ( permutations : " t a c o c a t " , " a t c o e t a " , e t c . )
"""


def checkpallindrome(usr_str):
    usr_str = str(usr_str).lower().replace(' ', "")
    d = dict()
    for chara in usr_str:
        if d.get(chara):
            d[chara] += 1
        else:
            d[str(chara)] = 1
    flag = 0
    for chara in usr_str:
        # print(str(chara) + " ->" + str(d[chara]))
        if d[chara] % 2 == 1:
            flag += 1
            if flag == 2:
                print("Not a Pallindrome Permutation")
                return
    print("A Pallindrome Permutation")


checkpallindrome(input("Enter String \n"))
