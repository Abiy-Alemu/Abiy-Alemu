class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_dict = {"(": ")", "{": "}", "[": "]"}
        
        for char in s:
            if char in my_dict:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if my_dict[top] != char:
                    return False
        
        return len(stack) == 0


