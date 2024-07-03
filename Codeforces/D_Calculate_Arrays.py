def calculate_array(n, b):
    a = []
    x = 0
    
    for i in range(n):
        ai = b[i] + x
        a.append(ai)
        x = max(x, ai)
    
    return a

n = int(input())
b = list(map(int, input().split()))
result = calculate_array(n, b)
print(" ".join(map(str, result)))
