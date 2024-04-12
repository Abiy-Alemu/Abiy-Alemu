class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        M = len(grid)
        N = len(grid[0])
        answer = [[0] * (N-2) for _ in range(M-2)]
        for i in range(M-2):
            for j in range(N-2):
                window_max = max(max(row[j:j+3]) for row in grid[i:i+3])
                answer[i][j] = window_max        
        return answer
