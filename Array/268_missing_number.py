class Solution:
    def missingNumber(self, nums):
        nums_exist_list = [-1] * (len(nums)+1)

        for num in nums:
            nums_exist_list[num] = 1
        
        for ind, val in enumerate(nums_exist_list):
            if val == -1:
                return ind


nums = [9,6,4,2,3,5,7,0,1]
sol  = Solution()
print(sol.missingNumber(nums))