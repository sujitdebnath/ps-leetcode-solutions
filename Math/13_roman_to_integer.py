class Solution:
    def romanToInt(self, s):
        roman_dict = { 'I'  : 1, 'V'  : 5, 'X'  : 10, 'L'  : 50, 'C'  : 100, 'D'  : 500, 'M'  : 1000,
                       'IV' : 4, 'IX' : 9, 'XL' : 40, 'XC' : 90, 'CD' : 400, 'CM' : 900}

        ind     = 0
        int_num = 0
        str_len = len(s)

        while ind < str_len:
            if ind+1 != str_len and s[ind:ind+2] in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
                roman_char_comp = s[ind:ind+2]
                int_num         = int_num + roman_dict[roman_char_comp]
                ind             = ind + 2
                continue
            
            roman_char = s[ind]
            int_num    = int_num + roman_dict[roman_char]
            ind        = ind + 1
        
        return int_num


s = ["III", "LVIII", "MCMXCIV"]
sol  = Solution()
for roman_char in s:
    print(sol.romanToInt(roman_char))