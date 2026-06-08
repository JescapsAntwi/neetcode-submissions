class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        if s_sorted == t_sorted:
            return True 
        else:
            return False


'''
two str should have same length 
count of individual characters in both strings should be the same
sort both strings and check for equality

s = "racecar"
t = "carrace"
s = "aaccer"
t = "aaccer"

s == t (true)

s= "jar"
t = "jam"
s = "ajr"
t = "ajm"

s!=t (false)
time: O(n)
space: O(1)
'''