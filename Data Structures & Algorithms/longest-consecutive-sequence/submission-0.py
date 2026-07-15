[20,23,21,22,1,2,3,5,24]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        maximum = 0 
        hashset = set(nums)
        for i in nums:
            if (i-1) not in hashset:
                initial = i
                streak = 1
                while (initial + 1) in hashset:
                    streak +=1
                    initial +=1
                maximum = max(maximum, streak)
        return maximum
     
            


        
        