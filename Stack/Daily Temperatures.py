class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]
        for index, k in enumerate(temperatures):
            if not stack or k <= stack[-1][0]:
                stack.append([k, index])
            else:
                while stack and stack[-1][0] < k:
                    res[stack[-1][1]] = index - stack[-1][1]
                    stack.pop(-1)
                stack.append([k, index])

        return res