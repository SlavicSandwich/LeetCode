class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        maxc = 0
        hashtable = {}
        for i in nums:
            if i not in hashtable:
                hashtable[i] = 1
                maxc = max(maxc, hashtable[i])
            else:
                hashtable[i] += 1
                maxc = max(maxc, hashtable[i])


        new = [[] for j in range(maxc + 1)]
        for i in hashtable:
            new[hashtable[i]].append(i)

        i = 0
        j = len(new) - 1
        res = []
        while i != k:
            for l in new[j]:
                res.append(l)
                i += 1
                if i == k:
                    return res
            j -= 1

        return res

print(Solution().topKFrequent([0], 0))







