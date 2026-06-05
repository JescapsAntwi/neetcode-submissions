class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        "bcaabc"
        initial questions
        are all the strings made up of only lowercase letters (i think they are from the testcases but i will convert them to lowercase just to be sure)
        are the strings sorted or do i have to sort them (no they are not sorted but sorting will definitely help)
        are the strings made up of numbers, other characters that aren't letters (ASCII), hm i think they arem't 
        
           unique_string = sorted(set(s.lower()))
        return len(unique_string)
        '''
        #optimal approach using sliding window 
        charSet = set()
        l = 0 
        res = 0 #returns length of maximum substring w/o duplicate characters 
        for r in range(len(s)):
            while s[r] in charSet: #if we've seen a new duplicate character
                charSet.remove(s[l]) #we remove the old (second) duplicate
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res 

     
