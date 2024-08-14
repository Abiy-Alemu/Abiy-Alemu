# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the input set
set_A = set(map(int, input().split()))
set_N = int(input())
is_superset = True
for _ in range(set_N):
    otherSets = set(map(int, input().split()))
    if not set_A.issuperset(otherSets):
        is_superset = False
        break
        
print(is_superset)