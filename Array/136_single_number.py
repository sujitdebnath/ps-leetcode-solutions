class Solution:
    def singleNumber(self, nums):
        nums_counter = dict()

        for num in nums:
            if num in nums_counter.keys():
                nums_counter[num] += 1
            else:
                nums_counter[num] = 1
        
        for num, count in nums_counter.items():
            if count == 1:
                return num


nums = [4,1,2,1,2]
sol  = Solution()
print(sol.singleNumber(nums))