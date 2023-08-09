class Solution:
    def minDeletionSize(self, strs):
        no_col_del = 0

        for ind in range(len(strs[0])):
            col_str = ""

            for temp_str in strs:
                col_str += temp_str[ind]
            
            if not self.isSorted(col_str):
                no_col_del += 1

        return no_col_del

    def isSorted(self, sample_str):
        return sample_str == "".join(sorted(sample_str))


sol = Solution()
print(sol.minDeletionSize(["zyx","wvu","tsr"]))