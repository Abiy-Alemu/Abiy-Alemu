class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))

        def compare(a, b):
            return int(b + a) - int(a + b)
        nums_str = sorted(nums_str, key=cmp_to_key(compare))

        
        result = ''.join(nums_str)

        if result[0] != '0':
            return result
        else:
            return '0'

