# t  = no of test cases
t = int(input())

for _ in range(t):
    str = input()
    if str[:3].lower() == "yes":
        print("YES")
    else:
        print("NO")
    