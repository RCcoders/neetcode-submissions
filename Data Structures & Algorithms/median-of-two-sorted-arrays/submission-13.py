from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # We want to ensure nums1 is the smaller array to optimize the binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        
        while low <= high:
            partitionX = (low + high) // 2
            # Total elements on the left side should be (x + y + 1) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            
            # Edge cases: if partition is 0, nothing is on the left. Use -infinity.
            # If partition is at the end, nothing is on the right. Use +infinity.
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]
            
            # Check if we found the correct partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # If total number of elements is odd
                if (x + y) % 2 != 0:
                    return max(maxLeftX, maxLeftY)
                # If total number of elements is even
                else:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            
            # Adjust the binary search range
            elif maxLeftX > minRightY:
                # We are too far right in nums1, move left
                high = partitionX - 1
            else:
                # We are too far left in nums1, move right
                low = partitionX + 1