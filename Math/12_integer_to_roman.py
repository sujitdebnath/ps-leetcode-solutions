class Solution:
    def intToRoman(self, num):
        roman_numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        roman_to_value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        roman_str         = ""
        curr_numerals_ind = 0

        while num > 0:
            number_of_numerals = num // roman_to_value[curr_numerals_ind]

            if number_of_numerals > 0:
                roman_str += roman_numerals[curr_numerals_ind] * number_of_numerals
                num       %= roman_to_value[curr_numerals_ind]
            
            curr_numerals_ind += 1
        
        return roman_str


num = 1994
sol = Solution()
print(sol.intToRoman(num))