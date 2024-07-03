# tot_s  = totlal student team
#max_p_t = maximum possible teams
def max_teams(a, b):
    tot_s = a + b
    max_p_t = tot_s // 4
    
    if a < 1 or b < 1:
        return 0
    
    return min(a, b, max_p_t)

if __name__ == "__main__":
    t = int(input().strip())
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        results.append(max_teams(a, b))
    
    for result in results:
        print(result)
