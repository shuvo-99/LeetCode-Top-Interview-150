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



# if len(nums) == 0:
        #     return 0
        # count= 1
        # p1 = 0
        # for p2 in range(1, len(nums)):
        #     # if p1+1 != len(nums): 
        #         if nums[p1] != nums[p2]:
        #             if nums[p1] == nums[p1+1]:
        #                 p1 += 2
        #                 nums[p1] =  nums[p2]
        #             else:
        #                 p1 += 1
        #                 nums[p1] =  nums[p2]

        #         else:
        #             nums[p1+1] =  nums[p2]
        #             p1 += 1
            
        # print(nums, p1+1)
        # return p1 + 1

# for p2 in range(1, len(nums)):
        #     if nums[p2] >= nums[p2-1]:
        #       if nums[p1] == nums[p2] and nums[p1] != nums[p2+1]:
        #           nums[p1+2] = nums[p2+1]
        #           p1 += 1
                  
        #       elif nums[p1] != nums[p2]:
        #           p1 += 1
        #       count+=1
        #         # nums[p1] = nums[p2]
        # if nums[p1] == nums[p1+1] and nums[p1] == nums[p1+2]:
        #     nums[p1+2] = nums[p1+3]
        #     nums[p1+3] = "_"
        #     count+=1
        #     p1+=1
        
        # if nums[p1] == nums[p1+1]:
        #     nums[p1+1] = "_"