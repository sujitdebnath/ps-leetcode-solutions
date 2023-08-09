class Solution:
    def sortedSquares(self, nums):
        neg_head     = 0
        pos_head     = len(nums) - 1
        nums_squared = list()

        while neg_head <= pos_head:
            neg_head_sq = nums[neg_head] ** 2
            pos_head_sq = nums[pos_head] ** 2

            if neg_head_sq <= pos_head_sq:
                nums_squared.append(pos_head_sq)
                pos_head -= 1
            else:
                nums_squared.append(neg_head_sq)
                neg_head += 1
        
        return nums_squared[::-1]


nums = [-4,-1,0,3,10]
sol = Solution()
print(sol.sortedSquares(nums))