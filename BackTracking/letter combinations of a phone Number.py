class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        bigits = {2:'abc',
                  3:'def',
                  4:'ghi',
                  5:'jkl',
                  6:'mno',
                  7:'pqrs',
                  8:'tuv',
                  9:'wxyz'}
        res = []

        def dfs(i:int, cur:list):
            if i == len(digits):
                if cur:
                    res.append(''.join(cur))
                return
            for k in bigits[int(digits[i])]:
                cur_rec = cur.copy()
                cur_rec.append(k)
                dfs(i + 1, cur_rec)

        dfs(0, [])
        return res


print(Solution().letterCombinations(''))




