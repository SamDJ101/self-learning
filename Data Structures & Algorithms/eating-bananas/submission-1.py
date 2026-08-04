import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        best_rate = max(piles)
        current_hours = 0
        while l<=r:
            current_rate = (l+r)//2
            current_hours = 0
            for i in range(len(piles)):
                current_hours+= math.ceil(piles[i]/current_rate)
            print((current_rate,current_hours))
            if current_hours > h:
                l = current_rate+1
            else:
                r = current_rate-1
                best_rate = min(best_rate, current_rate)
        
        return best_rate
            
            
        
        