import sys
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    
    ans = a[0] - 1 if k == 0 else a[k - 1]
    
    cnt = sum(1 for num in a if num <= ans)
    
    if cnt != k or not (1 <= ans <= 1000 * 1000 * 1000):
        print(-1)
        return
    
    print(ans)

if __name__ == "__main__":
    main()
