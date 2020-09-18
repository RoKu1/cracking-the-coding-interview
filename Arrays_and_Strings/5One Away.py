"""
1.5 One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple - > true
pales, pale - > true
pale, bale - > true
pale, bake - > false
Hints: #23, #97, it 130
"""
"""
Solution -->
  There are three types of edits --> replace, insert and delete
  Here insert and delete will be done only if length do not match
  AND Replace will e done if length are same
  ALgorithm -->
   Check the lengths
   A) If difference in lengths is more than 1 return false
   B) Else -->
            C) If lengths are same go to replace function
            D) If length are different go to insert/delete function 
"""


def difflenstrs(shrtstr, lngstr):
    edits = 0
    ind1 = 0
    ind2 = 0
    while ind1 < len(shrtstr) and ind2 < len(lngstr):
        print("Edits Done-->" + str(edits))
        if shrtstr[ind1] == lngstr[ind2]:
            ind1 += 1
            ind2 += 1
        elif shrtstr[ind1] != lngstr[ind2]:
            edits += 1
            ind2 += 1
        if edits == 2:
            return False
    if ind2 == len(lngstr) - 2:
        edits += 1
    if edits < 2:
        return True
    else:
        return False


def checkoneaway(usrstr1, usrstr2):
    usrstr1 = str(usrstr1).strip()
    usrstr2 = str(usrstr2).strip()

    if abs(len(usrstr2) - len(usrstr1)) > 1:
        return False
    edits = 0
    if len(usrstr1) == len(usrstr2):
        print(edits)
        for i in range(0, len(usrstr2)):
            if usrstr1[i] != usrstr2[i] and edits < 2:
                edits += 1
            if edits == 2:
                return False
    # pales and pale --> delete 's' or insert 's'
    # pale and ple --> delete 'a' --> can not insert inside a string this has to be done at the end  only
    else:
        if len(usrstr1) > len(usrstr2):
            return difflenstrs(usrstr2, usrstr1)
        else:
            return difflenstrs(usrstr1, usrstr2)
    if edits <= 1:
        return True


if checkoneaway(input("String1"), input("String2")):
    print("Yes")
else:
    print("No")
