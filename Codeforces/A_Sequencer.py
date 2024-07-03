t = int(input())
result = []

for i in range(t):
    length = int(input())
    arr = list(map(int, input().split()))
    left = 0
    right = length - 1
    sequence = []

    while left <= right:
        if left != right:
            sequence.append(arr[left])
            sequence.append(arr[right])
        else:
            sequence.append(arr[left])
        left += 1
        right -= 1

    result.append(' '.join(map(str, sequence)))

print('\n'.join(result))