class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        def dfs(canditates:list, itero:list, i:int,total:int,  target:int):
            if i == len(canditates):
                return

            if total == target:
                res.append(itero.copy())
                return

            if total > target:
                return

            itero_rec = itero.copy()
            dfs(canditates, itero_rec, i + 1,total, target)
            itero_rec.append(canditates[i])
            dfs(canditates, itero_rec, i, total + canditates[i],target)

        dfs(candidates, [], 0,0, target)
        return res

print(Solution().combinationSum([2,3,6,7], 7))