class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
brute force approach 
sort strings 
add sorted strings as key to dictionary 
values of dictionary will be anagrams as list 
return groups of anagrams

['act', 'cat', 'hat', 'aht', 'mat']

results = defaultdict(list)
        for s in strs:
            sorted_string = ''.join(sorted(s))
            results[sorted_string].append(s)
        return list(results.values())
        '''
        #optimal solution (using character count as keys in hashtable), then values will be anagrams as list
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26 #get count of each character 
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s)
        return list(result.values())
        
        