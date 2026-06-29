class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0

        for i in range(n):
            for j in range(i+1, n):
                width = j - i
                h = min(heights[i], heights[j])
                ans = max(ans, width * h)

        return ans