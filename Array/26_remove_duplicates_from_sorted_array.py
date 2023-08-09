class Solution:
    def removeDuplicates(self, nums):
        length    = len(nums)
        first     = 0
        second    = 1
        dup_count = 0

        while second != length:
            if nums[first] == nums[second]:
                dup_count = dup_count + 1
            else:
                first        = first + 1
                temp         = nums[first]
                nums[first]  = nums[second]
                nums[second] = temp
            
            second = second + 1

        return length - dup_count
    

nums = [0,0,1,1,1,2,2,3,3,4]
sol  = Solution()
print(sol.removeDuplicates(nums))
print(nums)