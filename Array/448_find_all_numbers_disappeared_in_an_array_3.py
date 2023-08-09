class Solution:
    def findDisappearedNumbers(self, nums):
        nums.sort()
        n                = len(nums)
        num_counter      = 1
        disappeared_list = list()
        
        for num in nums:
            if num == num_counter:
                num_counter += 1
            elif num > num_counter:
                for val in range(num_counter, num):
                    disappeared_list.append(val)
                num_counter = num + 1
        
        if num_counter <= n:
            for val in range(num_counter, n+1):
                    disappeared_list.append(val)
        
        return disappeared_list


nums = [4,3,2,7,8,2,3,1]
sol  = Solution()
print(sol.findDisappearedNumbers(nums))