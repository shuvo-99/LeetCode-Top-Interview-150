# === Brute Force ====
class Solution:
    def strStr(self, haystack, needle):
        if len(needle) > len(haystack):
            return -1
        flag = False
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if len(needle) > 1:
                    if len(haystack) - (i+1) < len(needle):
                        return -1
                    else:
                        for j in range(1,len(needle)):
                            if haystack[i+j] != needle[j]:
                                flag = False
                                break
                            else:
                                flag = True
                else:
                    flag = True 
            
            if flag == True:
                return i
        if flag == False:
            return -1
obj1 = Solution()
print(obj1.strStr("aaa", 'aaa'))


# === Alterantive (Better Approach) ===

class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i: i+len(needle)] == needle:
                return i
        return -1
obj1 = Solution()
print(obj1.strStr("baa", 'aaa'))