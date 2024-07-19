class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeros = 0 
        for i in range(n-1):
            if nums[i]== nums[i + 1]:
                nums[i] *= 2
                nums[i+1] = 0

        zeros = nums.count(0)
        non_zeros = [i for i in nums if i != 0]

        return non_zeros + [0]* zeros