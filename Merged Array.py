from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        first, second = m - 1, n - 1
        current = m + n - 1

        for _ in range(m + n):
            if first >= 0 and (second < 0 or nums1[first] > nums2[second]):
                nums1[current] = nums1[first]
                first -= 1
            else:
                nums1[current] = nums2[second]
                second -= 1
            current -= 1
