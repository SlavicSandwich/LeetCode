class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        time_to_buy = -1
        time_to_sell = -1
        buy_price = -1
        sell_price = -1
        profit = [0]
        for k in range(len(prices)):
            if buy_price<0 or prices[k] < buy_price and k < len(prices) - 1:
                buy_price = prices[k]
                time_to_buy = k

            if buy_price >= 0 and prices[k] > buy_price:
                sell_price = prices[k]
                time_to_sell = k
                profit.append(sell_price - buy_price)

        return max(profit)


print(Solution().maxProfit([3,3,5,0,0,3,1,4]))