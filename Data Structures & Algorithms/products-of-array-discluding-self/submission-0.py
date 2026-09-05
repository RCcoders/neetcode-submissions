class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) # nums = [1,2,4,6] n = 4
        res = [1] * n # res = [1,1,1,1]

        prefix = 1
        for i in range(n): # from index 0 to 3 
            res[i] = prefix # res[0] = 1
            prefix *= nums[i] 
        # after this loop the res becomes [1, 2, 4, 8]
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix # now we will move backward
            suffix *= nums[i]

        return res