class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        
        left,right = 0,n-1
        sum_a = []
        
        
        while left < right :
            
            sum_a.append(skill[left] + skill[right])
            left +=1
            right -=1

        summ = set(sum_a)
        if len(summ) == 1:
            total = 0
            left,right = 0,n-1
            while left < right:
                total += (skill[left]*skill[right])
                left +=1
                right -=1 
                

        else:
            return -1       

        return total

        
