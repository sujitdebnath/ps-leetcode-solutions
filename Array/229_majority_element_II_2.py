class Solution:
    def majorityElement(self, nums):
        frequency_dict = {num:nums.count(num) for num in set(nums)}
        return [num for num in frequency_dict.keys() if frequency_dict[num] > (len(nums)//3)]


nums = [3,2,3]
sol  = Solution()
print(sol.majorityElement(nums))