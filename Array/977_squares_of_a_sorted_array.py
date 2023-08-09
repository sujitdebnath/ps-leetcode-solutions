class Solution:
    def sortedSquares(self, nums):
        nums_squared = [num**2 for num in nums]
        nums_squared.sort()
        return nums_squared


nums = [-4,-1,0,3,10]
sol = Solution()
print(sol.sortedSquares(nums))