class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pointer = 0
        aset = {}
        c = 0
        maxc = 0
        for k in range(len(s)):
            if s[k] not in aset:
                aset[s[k]] = k
                c += 1

            elif s[k] in aset and s[k] == s[pointer]:
                pointer += 1
                aset[s[k]] = k

            else:
                maxc = max(c, maxc)
                pointer = aset[s[k]] + 1
                to_pop = []
                for i in aset:
                    if aset[i] < pointer:
                        to_pop.append(i)
                        c -= 1

                for l in to_pop:
                    aset.pop(l)

                aset[s[k]] = k
                c += 1

        return max(maxc, c)


print(Solution().lengthOfLongestSubstring('pwwkew'))



