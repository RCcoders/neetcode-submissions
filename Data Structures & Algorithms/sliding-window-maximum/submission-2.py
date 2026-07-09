class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []

        left = 0

        for right in range(len(nums)):

            if right - left + 1 == k:
                ans.append(max(nums[left:right + 1]))
                left += 1

        return ans
