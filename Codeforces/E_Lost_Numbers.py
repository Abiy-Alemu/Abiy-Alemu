a = [0, 4, 8, 15, 16, 23, 42]  # given array
arr = [0] * 7  # array to store current permutation
vis = [False] * 7  # visited flags for elements in `a`

# Initialize variables for conditions
N, M, S, L = 0, 0, 0, 0
found = False  # flag to indicate if solution is found

def dfs(cnt):
    global found
    if found:
        return

    if cnt == 7:
        # Check if the current permutation satisfies the conditions
        if (arr[1] * arr[2] == N and 
            arr[2] * arr[3] == M and 
            arr[3] * arr[4] == S and 
            arr[4] * arr[5] == L):
            found = True
            print("! ", end="")
            for i in range(1, 7):
                print(arr[i], end=" \n"[i == 6])
        return
    
    for i in range(1, 7):
        if vis[i]:
            continue
        vis[i] = True
        arr[cnt] = a[i]
        dfs(cnt + 1)
        vis[i] = False

def main():
    global N, M, S, L
    print("? 1 2", flush=True)
    N = int(input().strip())
    print("? 2 3", flush=True)
    M = int(input().strip())
    print("? 3 4", flush=True)
    S = int(input().strip())
    print("? 4 5", flush=True)
    L = int(input().strip())

    dfs(1)

if __name__ == "__main__":
    main()
