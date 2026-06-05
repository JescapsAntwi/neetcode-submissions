import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False 
        #small_string = s.lower().isalpha()

        #if string reads the same forwards and backwards, return True else return False 
        #match any character that isn't alphanumeric 
        pattern = r'[^a-zA-Z0-9]'
        #replace all non-alphanumeric characters with an empty string
        alpha_string = re.sub(pattern, "", s.lower())
        #if string reads the same forwards and backwards, return True
        if alpha_string == alpha_string[::-1]:
            return True 
        else:
            return False 

    #time complexity: O(n)
    #space complexity: O(n)


        