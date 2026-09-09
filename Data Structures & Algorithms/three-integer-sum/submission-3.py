class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        for i in range(len(nums)):
            seen = set()

            for j in range(i + 1, len(nums)):
                comp = -(nums[i] + nums[j])

                if comp in seen:
                    triplet = tuple(sorted([nums[i], nums[j], comp]))

                    res.add(triplet)

                seen.add(nums[j])
        return [list(triplet) for triplet in res]