#How maximum Number of items purchased in K rupees
def purchase(arr, n, k):
    if n==0 or k==0 :
        return 0
    ans =0
    arr.sort()
    i = 0
    while(i<n and k>arr[i]):
        ans+=1
        k=k-arr[i]
        i+=1
    return ans
k= 50
arr=[12, 80, 26, 42, 34]
print(purchase(arr, len(arr), k))