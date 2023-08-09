class Solution:
    def twoSum(self, nums, target):
        nums_dict = dict()
        
        for ind, num in enumerate(nums):
            if num not in nums_dict.keys():
                nums_dict[num] = [ind]
            else:
                ind_list = nums_dict[num]
                ind_list.append(ind)
                nums_dict[num] = ind_list

        for ind, num in enumerate(nums):
            rem = target - num

            if rem in nums_dict.keys():
                ind_list = nums_dict[rem]
                
                if rem != num:
                    return [ind, ind_list[0]]
                elif rem == num and len(ind_list)>1:
                    return [ind, ind_list[1]]


input_arr = [2,7,11,15]
target = 9
sol = Solution()
print(sol.twoSum(input_arr, target))