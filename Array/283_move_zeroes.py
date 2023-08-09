class Solution:
    def moveZeroes(self, nums):
        length = len(nums)
        first  = 0
        second = 1

        while second<length:
            if nums[first] == 0 and nums[second] == 0:
                second = second + 1
            elif nums[first] == 0:
                nums[first] = nums[second]
                nums[second] = 0
                first = first + 1
                second = second + 1
            elif nums[second] == 0:
                first = second
                second = second + 1
            else:
                first = second + 1
                second = second + 2


nums = [1,2,0,3,5,0,9]
sol  = Solution()
sol.moveZeroes(nums)
print(nums)