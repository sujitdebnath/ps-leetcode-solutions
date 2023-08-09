class Solution:
    def findMiddleIndex(self, nums):
        total_sum = sum(nums)
        left_sum  = 0

        for ind, num in enumerate(nums):
            right_sum = total_sum - left_sum - num

            if left_sum == right_sum:
                return ind
            else:
                left_sum = left_sum + num
        
        return -1


input_arr = [2,5]
sol       = Solution()
print(sol.findMiddleIndex(input_arr))