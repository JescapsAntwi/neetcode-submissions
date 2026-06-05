class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums.reverse()
        return nums[k-1]






'''
[1, 2, 3, 4, 5]

[5, 4, 3, 2, 1]
|
    |
    k 

[5, 5, 4, 3, 2, 1, 1]
|
    |
        |
        k

sort and reverse and return the k element (1 indexed)

time: nlogn + n = O(nlogn)
space: O(1)
'''