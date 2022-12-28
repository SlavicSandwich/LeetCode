def ceil(val:float):
    if int(val) < val < int(val) + 1:
        return int(val + 1)
    if int(val) == val:
        return int(val)

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        begin = 1
        end = max(piles) + 1
        possible_k = []
        while begin < end:
            mid = (begin + end) // 2
            hours = 0
            for i in piles:
                hours += ceil(i / mid)

            if hours <= h:
                possible_k.append(mid)
                end = mid

            else:
                begin = mid + 1

        return min(possible_k)

print(Solution().minEatingSpeed([30,11,23,4,20], 6))