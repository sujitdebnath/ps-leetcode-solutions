class Solution:
    def strStr(self, haystack, needle):
        len_haystack = len(haystack)
        len_needle   = len(needle)
        
        for ind in range(len_haystack-len_needle+1):
            if ind+len_needle <= len_haystack and haystack[ind:ind+len_needle] == needle:
                return ind
        
        return -1
        # return haystack.find(needle)

haystack = "hello"
needle   = "ll"

sol = Solution()
print(sol.strStr(haystack, needle))