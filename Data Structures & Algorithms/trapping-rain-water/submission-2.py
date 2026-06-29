class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        lmax, rmax = height[left], height[right]
        ans = 0
        while left < right:
            if lmax < rmax:
                left += 1
                lmax = max(lmax, height[left])
                ans += lmax - height[left]
            else:
                right -= 1
                rmax = max(rmax, height[right])
                ans += rmax - height[right]

        return ans