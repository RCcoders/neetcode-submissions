class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)

        low = 0
        high = x

        while low <= high:
            px = (low + high) // 2
            py = (x + y + 1) // 2 - px

            alx = float('-inf') if px == 0 else nums1[px - 1]
            ary = float('inf') if px == x else nums1[px]

            blx = float('-inf') if py == 0 else nums2[py - 1]
            bry = float('inf') if py == y else nums2[py]

            if alx <= bry and blx <= ary:
                if (x + y) % 2 != 0:
                    return max(alx, blx)

                else:
                    return (max(alx, blx) + min(bry, ary)) / 2

            elif alx > bry:
                high = px - 1

            else:
                low = px + 1