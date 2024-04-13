class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sort_nums = sorted(nums)
        res = []
        for num in nums:
            res.append(sort_nums.index(num))
        return res