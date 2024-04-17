class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
    
        n = len(arr)
        res = []

        for k in range(n, 0, -1):
            max_idx = arr.index(k)
            arr[:max_idx + 1] = arr[max_idx::-1]
            res.append(max_idx + 1)
            arr[:k] = arr[k - 1::-1]
            res.append(k)

        return res
