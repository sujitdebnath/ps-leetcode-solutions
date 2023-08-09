class Solution:
    def maxProfit(self, prices):
        buy_day    = 0
        sell_day   = 1
        max_profit = 0
        total_days = len(prices)

        while sell_day < total_days:
            buy_stock  = prices[buy_day]
            sell_stock = prices[sell_day]
            print("Buy: ({},{}), Sell: ({},{})".format(buy_day, buy_stock, sell_day, sell_stock), end=", ")

            if buy_stock > sell_stock:
                print("Buy Price > Sell Price")
                buy_day = sell_day
            else:
                curr_profit = sell_stock - buy_stock
                if curr_profit > max_profit:
                    max_profit = curr_profit
                print("Curr: {}, Max: {}".format(curr_profit, max_profit))
            
            sell_day = sell_day + 1
        
        return max_profit


prices = [4,7,2,1,5,3,8,6]
sol    = Solution()
print("Max Profit:", sol.maxProfit(prices))
