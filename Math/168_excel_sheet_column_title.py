class Solution:
    def convertToTitle(self, columnNumber):
        letter_dict  = {ind:chr(ord('A') + ind) for ind in range(0, 26)}
        column_title = ""

        while columnNumber > 0:
            column_title = letter_dict[(columnNumber-1) % 26] + column_title
            columnNumber = (columnNumber-1) // 26
        
        return column_title


col_num = 701
sol     = Solution()
print(sol.convertToTitle(col_num))