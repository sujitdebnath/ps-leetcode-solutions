class Solution:
    def maximumWealth(self, accounts):
        max_wealth = 0
        
        for customer_money in accounts:
            customer_total_wealth = sum(customer_money)
            if max_wealth < customer_total_wealth:
                max_wealth = customer_total_wealth
        
        return max_wealth


accounts = [[2,8,7],[7,1,3],[1,9,5]]
sol = Solution()
print(sol.maximumWealth(accounts))