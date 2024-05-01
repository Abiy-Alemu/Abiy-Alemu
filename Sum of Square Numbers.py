class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        self.c = c

        if 0 <= c <= 2**31-1:
            for a in range(int(c**0.5)+1):
                b = (c - a*a)**0.5
                if b == int(b):
                    return True
            return False
        else:
            return False
