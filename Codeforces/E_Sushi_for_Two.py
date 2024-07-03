# t_1  = sushi with tuna anna choice
# t_2  = sushi with eel Arkdady choice
n = int(input())
t = list(map(int, input().split()))

max_l = 0
t_1 = 1
t_2 = 1

for i in range(1, n):
    if t[i] == t[i-1]:
        t_1 += 1
    else:
        max_l = max(max_l, min(t_2, t_1))
        t_2 = t_1
        t_1 = 1

print(max(max_l, min(t_2, t_1)) * 2)