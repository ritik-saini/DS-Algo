#check whether the string is anagram of another method 1 complexity O(nlogn)
def checkAna(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
 
    if n1 != n2:
        return False
 
    str1 = sorted(str1)
    str2 = sorted(str2)
 
    for i in range(0, n1):
        if str1[i] != str2[i]:
            return False
    return True

str1 = 'integral'
str2 = 'triangle'
print (checkAna(str1, str2))