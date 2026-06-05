class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        len1 = len(nums1)
        len2 = len(nums2)
        merged = nums1 + nums2 
        merged.sort()

        totalLen = len(merged)
        if totalLen % 2 == 0:
            return (merged[totalLen // 2 - 1] + merged[ totalLen // 2 ]) / 2.0
        else:
            return merged[totalLen // 2]  

    '''
we want the left partition to be roughly half of the length
we want all the elements in our left partition to be less than or equal to the elements in 
our right half 

brute force
add two arrays and sort them 
get the total length 
check if length is even, if even return average of values
at middle and before middle value 
else 
return number at middle (length is odd)
      ''' 
     


