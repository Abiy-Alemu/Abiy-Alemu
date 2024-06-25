def find_runner_up_score(n, arr):
    A = set(arr)
    max_score = max(A)
    A.remove(max_score)
    runner_up_score = max(A) 
    return runner_up_score
if __name__ == "__main__":
    n = int(input().strip()) 
    arr = list(map(int, input().strip().split())) 
    result = find_runner_up_score(n, arr)
    print(result)