# Program to check string2 is the rotation of string1 or not.
def areRotation(string1, string2):
    size1=len(string1)
    size2=len(string2)

    if(size1!=size2):
        return 0
    temp = string1+string2
        # if str2 is a substring of temp
        # string.count returns the number of occurrences of
        # the second string in temp
    if(temp.count(string2)>0):
        return 1
    else:
         return 0
        
print(areRotation("draw", "ward"))