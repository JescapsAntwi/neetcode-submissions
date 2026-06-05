import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False 
        #using reversed string 
        new_string = ""
        for c in s:
            if c.isalnum():
                new_string += c.lower()
        return new_string == new_string[::-1]

    #time complexity: O(n)
    #space complexity: O(n)


        