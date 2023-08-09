class Solution:
    def groupAnagrams(self, strs):
        sorted_strs         = ["".join(sorted(item)) for item in strs]
        unique_items_set    = set(sorted_strs)
        group_anagrams_dict = dict()

        for item in unique_items_set:
            group_anagrams_dict[item] = []
        
        for item, sorted_item in zip(strs, sorted_strs):
            group_anagrams_dict[sorted_item].append(item)
        
        return list(group_anagrams_dict.values())


strs = ["eat","tea","tan","ate","nat","bat"]
sol  = Solution()
print(sol.groupAnagrams(strs))