#Problem to find the maximum occurence of a character in the string.
def max_occur(str):
    s = str.lower()
    occurences=[0 for i in range(256)]
    for char in s:
        occurences[ord(char)]+=1
    max_occurence=0
    character='~'
    for i in range(256):
        if (occurences[i]>max_occurence):
            character=chr(i)
            max_occurence=occurences[i]
    return character
print(max_occur('Entertainment'))