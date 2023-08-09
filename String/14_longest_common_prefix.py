class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[0]
        
        common_prefix = self.commonPrefix(strs[0], strs[1])

        if not common_prefix:
            return ""
        
        for str in strs[2:]:
            common_prefix = self.commonPrefix(str, common_prefix)
        
        return common_prefix
    
    def commonPrefix(self, str1, str2):
        common_prefix = ""
        min_len       = min(len(str1), len(str2))

        for ind in range(min_len):
            if str1[ind] == str2[ind]:
                common_prefix = common_prefix + str1[ind]
            else:
                break
        
        return common_prefix


sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))