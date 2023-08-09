class Solution:
    def removeElement(self, nums, val):
        length    = len(nums)
        first     = 0
        last      = length - 1
        dup_count = 0

        while first <= last:
            if nums[first] == val:
                if nums[first] != nums[last]:
                    temp        = nums[first]
                    nums[first] = nums[last]
                    nums[last]  = temp
                    first       = first + 1
                
                last      = last - 1
                dup_count = dup_count + 1
            else:
                first = first + 1

        return length - dup_count


nums = [3]
val  = 3
sol  = Solution()
print(sol.removeElement(nums, val))
print(nums)