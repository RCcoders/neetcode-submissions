class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(i, current):
            if i == len(nums):
                result.append(current.copy())
                return 
            
            backtrack(i + 1, current)

            # Take nums[i]
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

        backtrack(0, [])
        return result