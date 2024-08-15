class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n  = len(numbers)
        l,r = 0, n - 1
        while l < r:
            sum_two = numbers[l]+numbers[r]
            if sum_two > target:
                r -=1
            elif sum_two < target:
                l +=1

            else:
                return [l+1,r+1]