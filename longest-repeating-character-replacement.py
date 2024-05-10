class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_l = 0
        max_count = 0
        char_count = [0] * 26
        start = 0
        
        for i in range(len(s)):
            char_count[ord(s[i]) - ord('A')] += 1
            max_count = max(max_count, char_count[ord(s[i]) - ord('A')])
            if (i - start + 1 - max_count) > k:
                char_count[ord(s[start]) - ord('A')] -= 1
                start += 1
            max_l= max(max_l, i - start + 1)
        
        return max_l