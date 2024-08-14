class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        l,r = 0,n-1
        sum_a = []
        while l < r :
            sum_a.append(skill[l] + skill[r])
            l +=1
            r -=1

        summ = set(sum_a)
        if len(summ) == 1:
            total = 0
            l,r = 0,n-1
            while l< r:
                total += (skill[l]*skill[r])
                l+=1
                r -=1 
        else:
            return -1         
        
        return total

        