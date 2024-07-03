class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        set_nums2 = set(nums2)
        common_elements = [num for num in nums1 if num in set_nums2]
        
        if common_elements:
            return min(common_elements)
        else:
            return -1