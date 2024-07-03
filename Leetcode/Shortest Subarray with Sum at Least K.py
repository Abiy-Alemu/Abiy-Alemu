class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        prefix_sums = [0] * (n + 1)
        
        
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]
        
        
        deque_indices = deque()
        min_length = float('inf')
        
        for i in range(n + 1):
            
            while deque_indices and prefix_sums[i] - prefix_sums[deque_indices[0]] >= k:
                min_length = min(min_length, i - deque_indices.popleft())
            
            
            while deque_indices and prefix_sums[i] <= prefix_sums[deque_indices[-1]]:
                deque_indices.pop()
            
            deque_indices.append(i)
        
        if min_length == float('inf'):
            return -1
        else:
            return min_length

