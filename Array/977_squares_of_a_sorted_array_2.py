class Solution:
    def sortedSquares(self, nums):
        length_nums = len(nums)
        neg_head    = 0
        pos_head    = length_nums - 1
        
        nums_squared = [0] * length_nums
        ind          = length_nums - 1

        while neg_head <= pos_head:
            neg_head_sq = nums[neg_head] ** 2
            pos_head_sq = nums[pos_head] ** 2

            if neg_head_sq <= pos_head_sq:
                nums_squared[ind] = pos_head_sq
                pos_head         -= 1
            else:
                nums_squared[ind] = neg_head_sq
                neg_head         += 1
            
            ind -= 1
        
        return nums_squared


nums = [-4,-1,0,3,10]
sol = Solution()
print(sol.sortedSquares(nums))