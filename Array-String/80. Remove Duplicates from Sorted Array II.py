class Solution:
    def removeDuplicates(self, nums):
        
        if len(nums) <= 2:
            return len(nums)
        
        k = 2
        for i in range(2, len(nums)):

            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        
        return k

obj1 = Solution()
result = obj1.removeDuplicates([0,0,1,1,1,1,2,3,3])
print(result)
