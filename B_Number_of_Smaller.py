def count_element(arr1, arr2):
    arr_count = []
    for k in arr2:
        l, r = 0, len(arr1) - 1
        while l <= r:
            x = (l + r) // 2
            if arr1[x] < k:
                l = x + 1
            else:
                r = x - 1
        arr_count.append(l)
    return arr_count

n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = count_element(arr1, arr2)
print(*result)
