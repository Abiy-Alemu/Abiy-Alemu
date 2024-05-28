class Solution:
    def partitionLabels(self, s: str) -> List[int]:      
        
        l_ocr = {} # last occurance of letter or character 
        res = [] # result partition
        sp = 0 # sp = start pointer 
        ep = 0  #ep = end pointer
        for index in range(len(s)):
            char = s[index]
            l_ocr[char] = index


        for index, char in enumerate(s):
            ep = max(ep, l_ocr[char])
            
            if index == ep:
                res.append(ep- sp + 1)
                sp = index + 1

        return res

