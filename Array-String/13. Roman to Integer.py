# === Brute Force ====

class Solution:
    def romanToInt(self, s):

      res = 0
      i = 0
      while i < len(s):

        if s[i] == 'C':
          if i != len(s)-1:
            if s[i+1] == 'D':
              res+=400
              i+=2
            elif s[i+1] == 'M':
              res+= 900
              i+=2
            else:
              res+= 100
              i+=1
          else:
            res+= 100
            i+=1
        
        elif s[i] == 'X':
          if i != len(s)-1:  
            if s[i+1] == 'L':
              res+=40
              i+=2
            elif s[i+1] == 'C':
              res+= 90
              i+=2
            else:
              res+= 10
              i+=1
          else:
            res+= 10
            i+=1
        
        elif s[i] == 'I':
          if i != len(s)-1:
            if s[i+1] == 'V':
              res+=4
              i+=2
            elif s[i+1] == 'X':
              res+= 9
              i+=2
            else:
              res+= 1
              i+=1
          else:
            res+= 1
            i+=1

        elif s[i] == 'D':
          res+= 500
          i+=1
        
        elif s[i] == 'M':
          res+= 1000
          i+=1
        
        elif s[i] == 'L':
          res+= 50
          i+=1
        
        elif s[i] == 'V':
          res+= 5
          i+=1
          
      print(res) 
      return res   

obj1 = Solution()
obj1.romanToInt('III')
obj1.romanToInt('LVIII')
obj1.romanToInt('MCMXCIV')