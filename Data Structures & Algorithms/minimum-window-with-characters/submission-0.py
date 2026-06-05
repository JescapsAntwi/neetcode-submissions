class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return 

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT) # we have 0 of the characters we need and need represents the number of unique characters in T

        # res is an array of pointers so we assign default values of 0 and 1. we are looking for the minimum substring so any value we find will be less than infinity
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # if c is a character in T and we have satisfied the haves and needs
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                # current length of our string/ window
                #update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                #pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1 # we have to shift by 1 if we are removing a character from the left of our window
        l, r = res 
        return s[l: r+ 1] if resLen != float("infinity") else ""



            



'''
brute force:
we want to make sure each substring in s has the counts of the individual characters in t 
(greater than or equal)

taking characters and adding them into our window map
checking if the condition has been met and updating the window accordingly 
if the result exists, it will be stored in our result variable 
time: O(n)
'''
