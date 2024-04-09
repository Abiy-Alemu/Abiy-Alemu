class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        def smallest_even_multiple(n):
            multiple = 2
            while multiple % n != 0:
                multiple += 2
            return multiple
        
        return smallest_even_multiple(n)
