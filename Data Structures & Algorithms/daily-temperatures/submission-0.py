class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for curr_idx in range(n):
            curr_temp = temperatures[curr_idx]
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                ans[prev_idx] = curr_idx - prev_idx
                

            stack.append(curr_idx)

        return ans