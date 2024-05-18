class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        n = len(height)
        right = n - 1
        max_area = 0
        
        while left < right:
            diff_index = right - left
            height_min = min(height[right], height[left])
            max_area = max(max_area, diff_index * height_min)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area







