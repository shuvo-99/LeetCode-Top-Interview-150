# === Brute Force ====

class Solution:
    def rotate(self, nums, k):
        
        if len(nums) > 1:
            if len(nums) > k:
                self.numsGreaterThanK(nums, k)
               
            elif len(nums) == k: # If k is equal to length of array or multiple of length of array, then -
                pass             # the rotated array will be same as initial arr

            else:
                # Calculating to find value closest to k which is multiple of length of array,
                # since as 2nd condition, the rotated array will be same as initial array
                # Here after mod operation, the remainder is the difference between k and closest value to k which is multiple of length of array
                # And send ot to the method that is for 1st condition 
                self.numsGreaterThanK(nums, k%len(nums))
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