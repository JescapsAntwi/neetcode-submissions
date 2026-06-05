class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
brute force approach 
sort strings 
add sorted strings as key to dictionary 
values of dictionary will be anagrams as list 
return groups of anagrams

['act', 'cat', 'hat', 'aht', 'mat']
        '''
        results = defaultdict(list)
        for s in strs:
            sorted_string = ''.join(sorted(s))
            results[sorted_string].append(s)
        return list(results.values())
        