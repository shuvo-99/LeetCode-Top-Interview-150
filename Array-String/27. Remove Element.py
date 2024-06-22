class Solution:
    def removeElement(self, nums, val):
        i=0
        while i<len(nums):
            if nums[i] == val:
                nums.pop(i)
                
            else:
                i+=1
        print(nums)
        
obj1 = Solution()
obj1.removeElement([0,1,2,2,3,0,4,2], 2)