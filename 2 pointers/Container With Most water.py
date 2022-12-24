class Solution:
    def maxArea(self, height: list[int]) -> int:
        i1 = 0
        i2 = len(height) -1
        maxi = 0
        while i1 < i2:
            area = min(height[i1], height[i2]) * abs(i2 - i1)
            maxi = max(area, maxi)
            if height[i1] >= height[i2]:
                i2 -= 1

            elif height[i1] < height[i2]:
                i1 += 1

        return maxi

print(Solution().maxArea([1, 2, 1]))