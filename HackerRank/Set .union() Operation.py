# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
E = set(list(map(str, input().split())))
m = int(input())
F = set(list(map(str, input().split())))
print(len(E.union(F)))