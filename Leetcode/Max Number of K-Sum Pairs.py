class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        num_freq = {}
        operations = 0
        
        for num in nums:
            if k - num in num_freq and num_freq[k - num] > 0:
                operations += 1
                num_freq[k - num] -= 1
            else:
                num_freq[num] = num_freq.get(num, 0) + 1
        
        return operations
