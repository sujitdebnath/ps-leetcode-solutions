class Solution:
    def majorityElement(self, nums):
        frequency_dict = self.frequencyGenerator(nums)
        len_nums       = len(nums)

        return [num for num in frequency_dict.keys() if frequency_dict[num] > (len_nums//3)]

    def frequencyGenerator(self, nums):
        frequency_dict = dict()

        for num in nums:
            if num in frequency_dict.keys():
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1
        
        return frequency_dict


nums = [3,2,3]
sol  = Solution()
print(sol.majorityElement(nums))