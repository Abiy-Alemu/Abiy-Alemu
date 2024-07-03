t  = int(input())

for _ in range(t):
    n  = int(input())
    s = input()
    count = n 
    left =0
    right = n-1

    flag = True
    
    while left <= right:
        if s[left] == '0' and s[right] == '1':
            left += 1
            right -= 1
            count -= 2
        elif s[left] =='1' and s[right] == '0':
            left += 1
            right -= 1
            count -= 2
        else:
            flag = False
            break

    if flag == False:
        print(count)
    else:
        print(count)