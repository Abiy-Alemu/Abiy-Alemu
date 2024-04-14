import sys
def main():
    t = int(input())    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        find = True
        for i in range(1, n):
            if a[i] - a[i - 1] > 1:
                find = False
                break     
        if find:
            print("YES")
        else:
            print("NO")
if __name__ == "__main__":
    main()
