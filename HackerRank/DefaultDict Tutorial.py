from collections import defaultdict

n, m = map(int, input().split())
group_a = defaultdict(list)

for i in range(1, n + 1):
    word = input().strip()
    group_a[word].append(i)

for _ in range(m):
    word = input().strip()
    if word in group_a:
        print(*group_a[word])
    else:
        print(-1)
        
