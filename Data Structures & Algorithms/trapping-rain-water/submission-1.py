class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        water = 0
        for i in range(n):
            left = 0
            right = 0
            for j in range(i + 1): # This scans from the very beginning of the array up to the current position i to find the tallest bar on the left side
                left = max(left, height[j])

            for j in range(i , n): # This scans from the current position i to the very end of the array to find the tallest bar on the right side 
                right = max(right, height[j])

            water += min(left, right) - height[i] # It takes the smaller of those two peaks subracts the current bar's height, and adds the result to the total water
        return water