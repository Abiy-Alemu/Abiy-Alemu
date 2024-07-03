from collections import defaultdict

graph = defaultdict(list)
height = defaultdict(int)

def dfs(ver, par=""):
    for child in graph[ver]:
        if child == par:
            continue
        dfs(child, ver)
        height[ver] = max(height[ver], height[child] + 1)

def main():
    n = int(input())
    
    for _ in range(n):
        s1, x, s2 = input().split()
        s1 = s1.lower()
        s2 = s2.lower()
        graph[s1].append(s2)
        graph[s2].append(s1)
    
    dfs("polycarp")
    print(height["polycarp"] + 1)

if __name__ == "__main__":
    main()
