#check whether the string is anagram of another method 2 complexity O(n)

NO_OFCHARS = 256
def checkAna(str1,str2):   
    count=[0 for i in range(NO_OFCHARS)]
    i=0
     
    for i in range(len(str1)):
        count[ord(str1[i]) - ord('a')] += 1
        count[ord(str2[i]) - ord('a')] -= 1
      
    if(len(str1) != len(str2)):
        return False
    
    for i in range(NO_OFCHARS):
        if (count[i] != 0):
            return False    
    return True

print(checkAna('listen', 'silent'))