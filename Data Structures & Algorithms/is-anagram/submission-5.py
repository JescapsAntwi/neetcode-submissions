class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        return count_s == count_t

      


'''
s = "racecar"
t = "carrace"
use a hashmap to store each character and their counts
check if the two hashmaps after iterating through both strings are the same
count_s = {r: 2, a: 2, c: 2, e: 1}
count_t = {c: 2, a: 2, r: 2, e: 1}
count_s[s[i]] = 1 + count_s.get(s[i], 0)
count_t[t[i]] = 1 + count_t.get(t[i], 0)

'''