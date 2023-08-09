class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []
        
        ranges     = list()
        start, end = nums[0], nums[0]

        for num in nums[1:]:
            if num != end + 1:
                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append(str(start) + "->" + str(end))
                start = num
            
            end = num
        
        if start == end:
            ranges.append(str(start))
        else:
            ranges.append(str(start) + "->" + str(end))
        
        return ranges


nums = [0,2,3,4,6,8,9,15,16,17,20]
sol  = Solution()
print(sol.summaryRanges(nums))