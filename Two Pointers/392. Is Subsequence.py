class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = 0
        p2 = 0
        count = 0
        if len(s) == len(t) == 0: return True
        while p2 < len(t):
            if count == len(s):
                return True
            if len(s)>0 and t[p2] == s[p1]:
                count+=1
                p2+=1
                p1+=1
            
            else:
                p2+=1
        if count == len(s):
                return True
        return False
        
obj = Solution()
print(obj.isSubsequence("bcd", "ubcd"))