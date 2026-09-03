class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            cmp = target - num
            if cmp in seen:
                return [seen[cmp], i]
            
            seen[nums[i]] = i
        return []