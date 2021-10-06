#Program to find the minimum number of platforms to departure the train

def minPlatform(arr,dep, n):
    arr.sort()
    dep.sort()
    i, j=0,0
    maxTrain, platform=0, 0
    while(i<n and j<n):
        if arr[i]<=dep[j]:
            maxTrain+=1
            i+=1
        else:
            maxTrain-=1
            j+=1
        platform = max(platform, maxTrain)
    return platform

n= 6
arr= [900, 940, 950, 1100, 1500, 1800]
dep= [910, 1200, 1120, 1130, 1900, 2000]
print("Minimum",minPlatform(arr, dep, n),"platforms are required for the departure of all trains")