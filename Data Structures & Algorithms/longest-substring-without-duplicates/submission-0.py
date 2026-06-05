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
        #brute force approach
        res = 0 
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            res = max(res, len(charSet))
        return res 
     
