class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        max_profit = 0

        while(r!=len(prices)):
            if prices[l]>prices[r]:
                l = r
            best_buy = prices[l]
            best_sell = prices[r]
            if best_sell-best_buy <=0:
                r+=1
            else:
                max_profit = max(max_profit,best_sell-best_buy)
                r+=1
        return max_profit

        