# class Solution:
#     def majorityElement(self, nums):
#         freq_count = {}
#         for i in nums:
#             if i not in freq_count:
#                 freq_count[i] = 1
#             else:
#                 freq_count[i]+=1
 
#         max_value = list(freq_count.values())[0]
#         max_key = list(freq_count.keys())[0]
        
#         for k,v in freq_count.items():
#             if v > max_value:
#                 max_value = v
#                 max_key = k
#         print(max_key)
#         return max_key
        
        
# obj1 = Solution()
# obj1.majorityElement([2,2,1,1,1,2,2])

# ===========  Boyer-Moore Voting Algorithm =========

class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        print(candidate)
        return candidate
        
        
obj1 = Solution()
obj1.majorityElement([2,2,1,1,1,2,2])