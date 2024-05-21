class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        left, right = [None] * n, [None] * n 
        s1, s2 = [], [] 
        
        
        for i in range(n): 
            cnt = 1
            while s1 and arr[s1[-1]] > arr[i]:
                cnt += left[s1.pop()]
            left[i] = cnt
            s1.append(i)
        
        
        for i in range(n - 1, -1, -1): 
            cnt = 1
            while s2 and arr[s2[-1]] >= arr[i]:
                cnt += right[s2.pop()]
            right[i] = cnt
            s2.append(i)
        
        result = 0
        
        
        for i in range(n): 
            result = (result + arr[i] * left[i] * right[i]) % MOD

        return result
