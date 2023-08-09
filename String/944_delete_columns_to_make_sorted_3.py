class Solution:
    def minDeletionSize(self, strs):
        no_col_del = 0

        for ind in range(len(strs[0])):
            col_str = strs[0][ind]

            for temp_str in strs[1:]:
                if col_str[-1] > temp_str[ind]:
                    no_col_del += 1
                    break
                col_str += temp_str[ind]

        return no_col_del


sol = Solution()
print(sol.minDeletionSize(["zyx","wvu","tsr"]))