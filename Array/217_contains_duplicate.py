class Solution:
    def containsDuplicate(self, nums):
        number_set = set()

        for num in nums:
            if num in number_set:
                return True
            number_set.add(num)
        
        return False
        # return len(nums) != len(set(nums))


nums = [1,2,3,1]
sol = Solution()
print(sol.containsDuplicate(nums))