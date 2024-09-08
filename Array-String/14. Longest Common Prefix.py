# === Brute Force ====

class Solution:
    def longestCommonPrefix(self, strs):
        p1 = 0
        res = ''
        while True:
          if len(strs[0]) == 0:
             return ''
          if p1 < len(strs[0]):
            curr= strs[0][p1]
            if len(strs) > 1: 
              for i in range(1, len(strs)):
                  if p1 < len(strs[i]):
                    if strs[i][p1] != curr:
                        if len(res) < 1:
                            return ''
                        else:
                            return res
                  else:
                    return res
                
              res += curr
              p1 += 1
            else: 
              return strs[0]
          else:  
            return strs[0]
              
obj1 = Solution()
print(obj1.longestCommonPrefix(["a"]))