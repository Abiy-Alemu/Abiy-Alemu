#from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 2:
            return list(set(words[0]) & set(words[1]))
        
        first_word_chars = set(words[0])
        common_letters = []



