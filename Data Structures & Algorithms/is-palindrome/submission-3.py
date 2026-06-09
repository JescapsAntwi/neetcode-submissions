class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = "".join(char for char in s if char.isalnum()).lower() # new
        return cleaned_string == cleaned_string[::-1]

        #stringg = "tab"
        #print(stringg[0])
        

'''
remove all non-alphanumeric characters (keep only small and upper case alphabets)
convert all to small letters 
use two pointers to compare i and j at each point, if they are the same at each point, return True, 
if different anywhere,return False. 

time:O(n)
space: O(n) # a copy of the string
'''