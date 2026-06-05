class Solution:

    def encode(self, strs: List[str]) -> str:

        '''
['a', 'b', 'c']
['abc']
joined_strings = ''.join(strs)
        return joined_strings

         sep_strings = list(s)
        return sep_strings 
        '''
        results = ""
        for s in strs:
            results += str(len(s)) + "#" + s
        return results

    def decode(self, s: str) -> List[str]:
        # ['a', 'b', 'c']
        results = []
        i = 0

        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length    
            results.append(s[i:j])
            i=j
        return results   
