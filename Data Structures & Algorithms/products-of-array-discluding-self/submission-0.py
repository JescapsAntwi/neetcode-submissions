class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #[1, 2, 3]

        #output = [6, 3, 2]
        #brute force approach 
        n = len(nums)
        res = [0] * n 
        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue 
                prod *= nums[j]
            res[i] = prod 
        return res 