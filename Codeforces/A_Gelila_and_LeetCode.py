def longest_non_decreasing_subsegment(n, a):
    if n == 1:
        return 1

    max_l = 1 # max length
    cur_l = 1 # current length
    
    for i in range(1, n):
        if a[i] >= a[i - 1]:
            cur_l += 1
        else:
            if cur_l > max_l:
                max_l = cur_l
            cur_l = 1
    
    if cur_l > max_l:
        max_l = cur_l
    
    return max_l


n = int(input())
a = list(map(int, input().split()))
print(longest_non_decreasing_subsegment(n, a))

