class Solution:
    def smallerNumbersThanCurrent(self,nums : List[int]) -> List[int]:
        sort_num  = sorted(nums)
        result = []
        for i in nums:
            result.append(sort_num.index(i))

        return result