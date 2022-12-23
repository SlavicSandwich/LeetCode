class Solution:
    def longestConsecutive(self, nums: list[int]):
        bruh = {}
        maxseq = 0
        curseq = 0
        for k in nums:
            bruh[k] = False

        for k in bruh:
            if k -1 in bruh:
                bruh[k] = k - 1

        for k in bruh:
            if bruh[k] is False:
                i = k
                curseq = 0
                while i in bruh:
                    curseq += 1
                    i += 1

                maxseq = max(curseq, maxseq)


        return maxseq