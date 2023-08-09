class Solution:
    def findDisappearedNumbers(self, nums):
        n                = len(nums)+1
        nums_set         = set(nums)
        disappeared_list = list()
        
        for val in range(1, n):
            if val not in nums_set:
                disappeared_list.append(val)
        
        return disappeared_list


nums = [4,3,2,7,8,2,3,1]
sol = Solution()
print(sol.findDisappearedNumbers(nums))