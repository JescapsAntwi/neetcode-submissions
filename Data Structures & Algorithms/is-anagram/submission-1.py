class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            #return sorted(s) == sorted(t)
            return self.quick_sort(s) == self.quick_sort(t)
    
    def quick_sort(self, word):
        if len(word) <=1:
            return word 
        split_word = list(word)
        pivot = split_word[len(split_word) // 2]
        left_half = [x for x in split_word if x < pivot]
        mid = [x for x in split_word if x == pivot]
        right_half = [x for x in split_word if x > pivot]

        return self.quick_sort(left_half) + mid + self.quick_sort(right_half)



    '''
brute force solution 
sort two strings, then compare their equality
    '''