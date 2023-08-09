class Solution:
    def threeSum(self, nums):
        nums_dict    = dict()
        all_triplets = list()

        for ind, num in enumerate(nums):
            if num not in nums_dict.keys():
                nums_dict[num] = [ind]
            else:
                ind_list = nums_dict[num]
                ind_list.append(ind)
                nums_dict[num] = ind_list
        
        for ind, num in enumerate(nums[:-2]):
            target       = -num
            two_sum_list = self.twoSum(nums[ind+1:], ind+1, target, nums_dict)

            for two_sum in two_sum_list:
                triplet = sorted([num, two_sum[0], two_sum[1]])

                if triplet not in all_triplets:
                    all_triplets.append(triplet)
        
        return all_triplets

    def twoSum(self, nums, starting_ind, target, nums_dict):
        two_sum_list = list()

        for num in nums:
            rem = target - num

            if rem in nums_dict.keys():
                ind_list = nums_dict[rem]
                two_sum  = sorted([num, rem])
                
                for ind in ind_list:
                    if ind>starting_ind and two_sum not in two_sum_list:
                        two_sum_list.append(two_sum)
                        break
            
            starting_ind += 1
        
        return two_sum_list


nums = [-1,0,1,2,-1,-4]
sol  = Solution()
print(sol.threeSum(nums))