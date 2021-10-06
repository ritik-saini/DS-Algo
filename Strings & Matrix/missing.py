# Problem in which we find the missing character from a sentence
def missing(str):
    arr = {}
    for i in range(0, 26):
        arr[i]=0
        
    for i in range(0, len(str)):
        if(ord(str[i])>=65 and ord(str[i])<=92):
            arr[ord(str[i])-ord('A')]=1
        else:
            arr[ord(str[i])-ord('a')]=1
    ans=""
    for i in range(0, 26):
        if(arr[i]!=1):
            ans += chr(i+ord('a'))

    if(ans==""):
        return "-1"
    return ans

print(missing('My name is Ritik Saini'))
