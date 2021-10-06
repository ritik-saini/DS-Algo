#Rearrange an array so that arr[i] becomes arr[arr[i]] with O(1) extra space
def arrange(arr, N):
    for i in range(N):
        arr[i]+=(arr[arr[i]] % N) * N
    for i in range(0, N):
        arr[i] = int(arr[i] / N)
    return arr
arr= [1, 0]
print(arrange(arr, len(arr)))