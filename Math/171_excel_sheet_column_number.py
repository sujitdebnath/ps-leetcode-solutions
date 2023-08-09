class Solution:
    def titleToNumber(self, columnTitle):
        letter_dict   = {chr(ord('A') + ind - 1):ind for ind in range(1, 27)}
        column_number = 0

        for ind, letter in enumerate(columnTitle[::-1]):
            column_number += letter_dict[letter] * (26**ind)
        
        return column_number
        # return sum([(ord(letter)-64) * (26**ind) for ind, letter in enumerate(columnTitle[::-1])])


col_title = "ZY"
sol       = Solution()
print(sol.titleToNumber(col_title))