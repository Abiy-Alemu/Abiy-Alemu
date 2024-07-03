class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right+1):
            is_covered = False
            for s, e in ranges:
                if s <= i <= e:
                    is_covered = True
                    break
            if not is_covered:
                return False
        return True