class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        water = 0
        for i in range(n):
            left = 0
            right = 0
            for j in range(i + 1):
                left = max(left, height[j])

            for j in range(i , n):
                right = max(right, height[j])

            water += min(left, right) - height[i]
        return water