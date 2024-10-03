# === Brute Force ====

class Solution:
    def rotate(self, nums, k):
        
        if len(nums) > 1:
            if len(nums) > k:
                self.numsGreaterThanK(nums, k)
               
            elif len(nums) == k: # If k equal to length of array or multiple of length of array, then -
                pass             # the rotated array will be same as initial arr
            
            else:
                a=k//len(nums)  # Calculating to find value closest to k which is multiple of length of array,
                b=len(nums)*a   # since as 2nd condition, the rotated array will be same as initial array
                self.numsGreaterThanK(nums, k-b) # after finding closest value, we subtract it with k and send the
                                                 # difference to the method that is for 1st condition  
        print(nums)

    def numsGreaterThanK(self, nums, k):
        tempArr = []
        for i in range(len(nums)-k, len(nums), 1):
            tempArr.append(nums[i])
            nums[i] = ''
        for j in range(len(nums)-1-k, -1, -1):
            nums[j+k] = nums[j]
        for z in range(len(tempArr)-1, -1 , -1):
            nums[z] = tempArr[z]

obj1 = Solution()
obj1.rotate([1,2,3,4,5,6,7],3)
obj1.rotate([-1,-100,3,99],2)
obj1.rotate([1,2],2)
obj1.rotate([1,2],3)
obj1.rotate([1,2],5)