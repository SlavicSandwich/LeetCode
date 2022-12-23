class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firsthash = {}
        for k in s:
            if k not in firsthash:
                firsthash[k] = 1

            else:
                firsthash[k] += 1

        secondhash = {}
        for k in t:
            if k not in secondhash:
                secondhash[k] = 1

            else:
                secondhash[k] += 1
        if len(firsthash) == len(secondhash):
            for k in secondhash:
                if k not in firsthash or firsthash[k] != secondhash[k]:
                    return False

            return True

        else:
            return False



print(Solution().isAnagram('a', 'ab'))