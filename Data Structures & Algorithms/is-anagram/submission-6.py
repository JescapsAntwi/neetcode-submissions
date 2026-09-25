class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        # sort 
        return sorted(s) == sorted(t)

'''
length of two strings need to be the same (first check) else false straightaway 
same number of individual characters in the two strings (order doesn't matter)

two approaches: sorting one string, then check for equality
use hashmap and keep count of individual characters

'''