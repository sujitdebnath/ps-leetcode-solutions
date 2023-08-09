class Solution:
    def twoSum(self, nums, target):
        for ind1, num1 in enumerate(nums):
            rem = target - num1
            for ind2, num2 in enumerate(nums[ind1+1:], start=ind1+1):
                if num2 == rem:
                    return [ind1, ind2]


input_arr = [2,7,11,15]
target = 9
sol = Solution()
print(sol.twoSum(input_arr, target))