class Solution:
    def moveZeroes(self, nums):
        first = 0
        last = len(nums) -1

        while first <= last:
            if nums[first] == 0:
                nums.pop(first)
                nums.append(0)
                last = last - 1
            else:
                first = first + 1


nums = [1,2,0,3,5,0,0,9]
sol  = Solution()
sol.moveZeroes(nums)
print(nums)