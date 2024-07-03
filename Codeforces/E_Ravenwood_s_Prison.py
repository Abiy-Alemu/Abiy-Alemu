# def is_unique_mapping(n, a):
#     visited = set()
#     for i in range(n):
#         new_position = (i + a[i % n]) % n
#         if new_position < 0:
#             new_position += n
#         if new_position in visited:
#             return "NO"
#         visited.add(new_position)
#     return "YES"

# # Read input
# import sys
# input = sys.stdin.read
# data = input().split()

# t = int(data[0])
# index = 1
# results = []

# for _ in range(t):
#     n = int(data[index])
#     a = list(map(int, data[index + 1:index + 1 + n]))
#     index += 1 + n
#     results.append(is_unique_mapping(n, a))

# # Output results
# sys.stdout.write("\n".join(results) + "\n")
def is_unique_mapping(n, a):
    visited = set()
    for i, num in enumerate(a):
        new_position = (i + num) % n
        if new_position in visited:
            return "NO"
        visited.add(new_position)
    return "YES"

t = int(input())
results = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    results.append(is_unique_mapping(n, a))

print("\n".join(results))