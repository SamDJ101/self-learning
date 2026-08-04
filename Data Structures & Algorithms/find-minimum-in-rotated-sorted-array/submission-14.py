class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l<=r:
            if nums[l] <= nums[r]:
                return nums[l]
            m = (l+r)//2
            if nums[m] < nums[m-1] :
                return nums[m]
            elif nums[m] >=nums[l]:
                l = m+1
            elif nums[m] <= nums[r]:
                r = m-1

        
        