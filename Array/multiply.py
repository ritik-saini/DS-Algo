
arr=[1, 2, 3, 4]
res=[1]*len(arr)
left=[1]*len(arr)
right=[1]*len(arr)

for i in range(len(arr)):
    left[i]= arr[i-1]*left[i-1]

for i in range(len(arr)-2, -1, -1):
    right[i]= arr[i+1]*right[i+1]


for i in range(len(arr)):
    res[i]=(right[i]*left[i])//len(arr)

print (res)
