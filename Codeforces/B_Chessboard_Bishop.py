def max_bishop_attack_sum(test_cases):
    results = []
    for grid in test_cases:
        n, m = len(grid), len(grid[0])
        pds = {} # primary digonal sums
        sds = {} #secondary_diagonal_sums
        
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                pds[i - j] = pds.get(i - j, 0) + val
                sds[i + j] = sds.get(i + j, 0) + val
        
        max_sum = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                current_sum = pds[i - j] + sds[i + j] - val
                max_sum = max(max_sum, current_sum)
        
        results.append(max_sum)
    
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    test_cases.append(grid)

results = max_bishop_attack_sum(test_cases)
for result in results:
    print(result)