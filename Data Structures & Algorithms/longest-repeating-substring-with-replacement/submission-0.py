class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #brute force approach 
        res = 0 
        for i in range(len(s)):
            count, maxf = {}, 0 #count of each character (character : frequency), most frequent character 
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                maxf = max(maxf, count[s[j]])
                # current window size and number of most appearing characters
                if (j - i + 1) - maxf <= k:
                    res = max(res, j - i + 1)
        return res 
