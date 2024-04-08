class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 ==0:
            return False
        org_x = x #orignal number
        num_rev = 0
        while x > 0:
            lastdigit = x%10
            num_rev *= 10 +lastdigit
            x = x//10
        return num_rev == org_x