class Solution:
    def findDisappearedNumbers(self, nums):
        nums_set = set(nums)
        return [val for val in range(1, len(nums)+1) if val not in nums_set]


nums = [4,3,2,7,8,2,3,1]
sol = Solution()
print(sol.findDisappearedNumbers(nums))