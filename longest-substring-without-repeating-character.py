class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dic = {}
        start = 0
        max_len = 0

        for i in range(len(s)):
            curr_char = s[i]
            if curr_char in dic and dic[curr_char] >= start:
                start = dic[curr_char] + 1
            dic[curr_char] = i
            max_len = max(max_len, i- start + 1)

        return max_len

