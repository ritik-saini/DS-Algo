#find nth term of the AP series
def arthimetic(arr, n, d):
    # d= arr[1]-arr[0]
    # ans = arr[0]+(n-1)*d
    ans = (n / 2) * (2 * arr + (n - 1) * d)
    return ans
arr = 6
print(arthimetic(arr, 4, 3))