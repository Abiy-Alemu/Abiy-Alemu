def countingSort(arr):
    frequency = [0] * 100  
    for num in arr:
        frequency[num] += 1 
    return frequency
n = int(input())
arr = list(map(int, input().split()))
result = countingSort(arr)
print(*result)