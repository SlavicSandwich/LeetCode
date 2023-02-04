# def add_to_hashmap(hashmap, key):
#     if key not in hashmap:
#         hashmap[key] = 1
#
#     else:
#         hashmap[key] += 1


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        maxlen = 0
        hashmap = {}
        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)

            while (r - i + 1) - max(hashmap.values()) > k:
                hashmap[s[i]] -= 1
                if hashmap[s[i]] == 0:
                    hashmap.pop(s[i])
                i += 1

            maxlen = max(maxlen, r - i + 1)

        return maxlen


print(Solution().characterReplacement('AABABBA', 1))
