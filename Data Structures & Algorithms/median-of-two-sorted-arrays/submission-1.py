class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        i = j = 0
        median1 = median2 = 0

        #loop till we reach middle of the two merged arrays 
        for count in range((len1 + len2) // 2 + 1):
            median2 = median1 
            #check if both pointers in the two arrays are in bounds 
            if i < len1 and j < len2:
                #check and select smaller element to simulate sorting merging
                if nums1[i] > nums2[j]:
                    median1 = nums2[j]
                    j += 1 #we have selected an element from one array so we increment the pointer in that array 
                else:
                    median1 = nums1[i]
                    i+= 1
            #right or second array is out of bounds 
            elif i < len1:
                median1 = nums1[i]
                i += 1
             #left or first array is out of bounds 
            else:
                median1 = nums2[j]
                j += 1
        if (len1 + len2) % 2 == 1:
            return float(median1)
        else:
            return (median1 + median2) / 2.0
            


  

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
     


