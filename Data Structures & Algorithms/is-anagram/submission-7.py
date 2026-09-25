class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use of hashmap 
        countS = {} # char: freq
        countT = {}
        
        for c in s:
            current_count = 1 + countS.get(c, 0)
            countS[c] = current_count  
        for ch in t:
            current_count = 1 + countT.get(ch, 0)
            countT[ch] = current_count 
        
        return countS == countT
            

'''
{r: 2, a:1}
{a: 1, r:2}
rar, arr


length of two strings need to be the same (first check) else false straightaway 
same number of individual characters in the two strings (order doesn't matter)

two approaches: sorting one string, then check for equality
use hashmap and keep count of individual characters

if len(s) != len(t):
            return False 
        
        # sort 
        return sorted(s) == sorted(t)
'''