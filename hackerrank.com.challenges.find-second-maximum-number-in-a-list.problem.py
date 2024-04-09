def find_runner_up_score(n, arr):
    unique_scores = set(arr)
    max_score = max(unique_scores)
    unique_scores.remove(max_score)
    runner_up_score = max(unique_scores) 
    return runner_up_score
if __name__ == "__main__":
    n = int(input().strip()) 
    scores = list(map(int, input().strip().split())) 
    result = find_runner_up_score(n, scores)
    print(result)
