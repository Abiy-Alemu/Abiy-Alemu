class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        rows = len(matrix)
        cols = len(matrix[0])
        res = []
        for _ in range(cols):
            res.append([0] * rows)

        for i in range(rows):
            for j in range(cols):
                res[j][i] = matrix[i][j]
        for r in res:
            print(r)

        return res
