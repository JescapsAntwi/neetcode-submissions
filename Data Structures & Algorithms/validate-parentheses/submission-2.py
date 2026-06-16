class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', "")
            s = s.replace('{}', "")
            s = s.replace('[]', "")
        return s == ""

        


'''
replace matching pairs with empty spaces, if resulting string is empty, it is valid else false
stack to store just opening brackets 

'''