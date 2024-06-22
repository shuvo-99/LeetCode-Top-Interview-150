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

# ================= Alternate ==============

class Solution:
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        
        print(nums)
        
obj1 = Solution()
obj1.removeElement([3,2,2,3], 3)

# ============ Better Approach ==========
class Solution:
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
        
obj1 = Solution()
obj1.removeElement([0,1,2,2,3,0,4,2], 2)