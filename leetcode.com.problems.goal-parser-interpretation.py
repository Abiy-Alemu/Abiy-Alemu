class Solution:
    def interpret(self, command: str) -> str:
        interpretation = ""
        i = 0
        n = len(command)
        
        while i < n:
            if command[i] == 'G':
                interpretation += 'G'
                i += 1
            elif command[i] == '(':
                if command[i+1] == ')':
                    interpretation += 'o'
                    i += 2
                elif command[i+1:i+3] == 'al':
                    interpretation += 'al'
                    i += 3
            else:
                i += 1
        
        return interpretation