# Union of two sorted arrays with handling of duplication
def unionSort(a, b , n ,m):
    '''
    a= Sorted array 1
    n= Size of aaray 1 (a)
    b= Sorted array 2
    m=  Size of aaray 2 (b)
    '''
    c= list() #a list or array for storing the result
    i, j =0, 0
    while i<n and j<m :
        while i+1<n and a[i+1]==a[i]:
            i+=1
        while j+1<m and b[j+1]==b[j]:
            j+=1
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        elif a[i]>b[j]:
            c.append(b[j])
            j+=1
        else:
            c.append(b[j])
            i+=1
            j+=1
    while i<n:
        while i+1<n and a[i+1]==a[i]:
            i+=1
        c.append(a[i])
        i+=1
    while j<m:
        while j+1<m and b[j+1]==b[j]:
            j+=1
        c.append(b[j])
        j+=1
    return c

a= [6, 8, 8, 10]
n= 4
b= [1, 2, 7, 9, 10]
m= 5
print(unionSort(a, b, n, m))