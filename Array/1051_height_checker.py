class Solution:
    def heightChecker(self, heights):
        return len([ind for ind in range(len(heights)) if heights[ind] != sorted(heights)[ind]])


heights = [1,1,4,2,1,3]
sol = Solution()
print(sol.heightChecker(heights))