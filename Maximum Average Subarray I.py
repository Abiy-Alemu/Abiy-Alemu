class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        left = 0
        right = k - 1
        current_sum = sum(nums[left:right+1])
        max_average = current_sum / k
        
        while right < len(nums) - 1:
            current_sum -= nums[left]
            left += 1
            right += 1
            current_sum += nums[right]
            max_average = max(max_average, current_sum / k)
        
        return max_average

        