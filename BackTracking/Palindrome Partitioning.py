class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []

        def check_palindrome(string:str):
            i = 0
            j = len(string) - 1
            while i < j:
                if string[i] != string[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfs(j, cur):
            if j == len(s):
                res.append(cur.copy())
                return
            string = ""
            for i in range(j, len(s)):
                string += s[i]
                if not check_palindrome(string):
                    continue

                newcur = cur.copy()
                newcur.append(string)
                dfs(i + 1, newcur)

        dfs(0, [])
        return res

print(Solution().partition('aab'))


