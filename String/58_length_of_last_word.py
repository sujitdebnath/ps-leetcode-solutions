class Solution:
    def lengthOfLastWord(self, s):
        len_last_word   = 0
        first_char_flag = False

        for char in s[::-1]:
            if char == " " and first_char_flag:
                break
            elif char != " " and not first_char_flag:
                first_char_flag = True
                len_last_word  += 1
            elif char != " " and first_char_flag:
                len_last_word += 1
        
        return len_last_word


s   = "   fly me   to   the moon  "
sol = Solution()
print(sol.lengthOfLastWord(s))