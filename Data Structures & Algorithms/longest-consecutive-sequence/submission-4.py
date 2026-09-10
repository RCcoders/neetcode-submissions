class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in numSet:
                current = num
                ln = 1

                while current + 1 in numSet:
                    current += 1
                    ln += 1

                longest = max(longest, ln)

        return longest