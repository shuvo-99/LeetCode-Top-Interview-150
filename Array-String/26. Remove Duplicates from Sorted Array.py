class Solution:
    def removeDuplicates(self, nums):
       
      if len(nums) > 1:
          p1 = 0
          p2 = p1+1
          count = 1
          while p2<= len(nums)-1:
              if nums[p1] == nums [p2]:
                  p2+=1
                      
              else:
                  nums[p1+1] = nums[p2] 
                  p1+=1
                  p2+=1
                  count+=1
                  
          return count
      else:
           return 1

obj1 = Solution()
obj1.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
# obj1.removeDuplicates([1,1,2])

# ============ Better Approach ==========

class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        
        p1 = 0
        
        for p2 in range(1, len(nums)):
            if nums[p1] != nums[p2]:
                p1 += 1
                nums[p1] = nums[p2]
        
        return p1 + 1

obj1 = Solution()
result = obj1.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(result)
