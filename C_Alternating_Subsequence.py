t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = [a[0]]
    
    for i in range(1, n):
        
        if b[-1] > 0 and a[i] > 0:
            if b[-1] < a[i]:
                b.pop()
                b.append(a[i])
        
        elif (b[-1] < 0 and a[i] > 0) or (b[-1] > 0 and a[i] < 0):
            b.append(a[i])
        
        else:
            if b[-1] < a[i]:
                b.pop()
                b.append(a[i])
    print(sum(b))
