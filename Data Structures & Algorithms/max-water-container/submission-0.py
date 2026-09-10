class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0 
        r = n - 1
        ans = 0

        while l < r:
            width = r - l
            current = width * min(heights[r], heights[l])
            ans = max(ans, current)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return ans