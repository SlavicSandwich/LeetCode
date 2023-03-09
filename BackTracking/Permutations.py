class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        def dfs(nums:list, se:set,cur:list, res:list):
            if len(se) == len(nums):
                res.append(cur)
                return

            for i in nums:
                if i not in se:
                    cur_rec = cur.copy()
                    se_rec = se.copy()
                    se_rec.add(i)
                    cur_rec.append(i)
                    dfs(nums, se_rec, cur_rec, res)

        dfs(nums, set(), [], res)
        return res

print(Solution().permute([1, 0]))