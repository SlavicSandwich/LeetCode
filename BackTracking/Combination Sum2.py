class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def backtrack(itero: list, pos: int, total: int):
            if total == 0:
                res.append(itero.copy())
                return

            if total < 0:
                return
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                itero.append(candidates[i])
                backtrack(itero, i + 1, total - candidates[i])
                itero.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res

#Just Copied It, Not sure that I understand this completely


print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
