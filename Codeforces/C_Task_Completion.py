def find_task_duration(n, s, f):
    d = [0] * n
    d[0] = f[0] - s[0]

    for i in range(1, n):
        if s[i] > f[i-1]:
            d[i] = f[i] - s[i]
        else:
            d[i] = f[i] - f[i-1]

    for i in range(n):
        print(d[i], end=" ")
    print()

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    f = list(map(int, input().split()))

    find_task_duration(n, s, f)
#f = first
#s = second
#d = duration
# t = test case