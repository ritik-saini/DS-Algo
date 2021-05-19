#find the trapped water between walls
def find_total_Water(arr, n):
    total_Water = 0

    for i in range(1, n - 1) :

        left = arr[i]
        for j in range(i) :
            left = max(left, arr[j])
         
        right = arr[i]
         
        for j in range(i + 1 , n) :
            right = max(right, arr[j])

        total_Water = total_Water+(min(left, right) - arr[i])
 
    return total_Water

arr= [3, 0, 2, 0, 4]
print(find_total_Water(arr, len(arr)))