class Solution:
    def lengthOfLastWord(self, s):
        wordSplit = s.split(' ')
        print(wordSplit)
        for i in range(len(wordSplit)-1, -1,-1):
            if len(wordSplit[i]) >= 1:
                return len(wordSplit[i])
    
obj1 = Solution()
print(obj1.lengthOfLastWord("luffy"))