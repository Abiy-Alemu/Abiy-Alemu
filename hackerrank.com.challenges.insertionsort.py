def insertionSort1(n, arr):
    key = arr[n-1]
    for i in range(n-2, -1, -1):
        if arr[i] > key:
            arr[i+1] = arr[i]
            print(*arr)  
        else:
            arr[i+1] = key
            break
    else:  
        arr[0] = key
    print(*arr)  
n = int(input())
arr = list(map(int, input().split()))
insertionSort1(n, arr)