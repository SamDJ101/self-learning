"""
[1,2,3,4]
[24,24,24,24]
[24,12,8,6]

[1,0,2,3]
[6,6,6,6]
[0,6,0,0]

[2,0,0,4]
[8,8,8,8]
[0,0,0,0]
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        z_count = 0
        for i in nums:
            if i!=0:
                prod = prod*i
            else:
                z_count += 1
        if z_count > 1:
            return [0]*len(nums)
        else: 
            result = [0] * len(nums)       
            for j in range(len(nums)):
                if nums[j]==0 and z_count:
                    result[j] = prod
                elif z_count ==0:
                    result[j] = int(prod/nums[j])
            return result





        
