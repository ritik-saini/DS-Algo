#How much a thief stole in maximum k things
def stole(arr, n, k):
    if n ==0:
        return 0
    ans =0
    arr.sort(reverse = True)
    for i in range(k):
        ans+=arr[i]
    return ans
arr=[100, 500, 400, 300, 700]
n =len(arr)
k= 4
print(stole(arr, n, k))