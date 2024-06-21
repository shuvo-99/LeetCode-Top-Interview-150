class Solution:
    def merge(self, nums1, m, nums2, n):
        for i in range(len(nums1)):
            if i>=m:
                nums1.pop()

        for i in range(len(nums2)):
            if i>=n:
                nums1.pop()

        for i in nums2:
            nums1.append(i)
        
        # Selection Sort
        for i in range(len(nums1)):
            minIdx = i

            for j in range(i+1, len(nums1)):
              if nums1[j] < nums1[minIdx]:
                minIdx = j
            
            temp = nums1[i]
            nums1[i] = nums1[minIdx]
            nums1[minIdx] = temp
                          
        print(nums1)
obj1 = Solution()
obj1.merge([0],  0,  [1], 1)