class Solution:
    def myAtoi(self, s):
        if not s:
            return 0
        
        number_str  = s.lstrip()
        is_negative = False
        number      = 0
        
        for ind in range(len(number_str)):
            char = number_str[ind]
            if ind == 0 and char == '-':
                is_negative = True
            elif ind == 0 and char == '+':
                continue
            elif char.isdigit():
                number = number*10 + int(char)
            else:
                break
        
        if is_negative:
            number = -1 * number
        
        if number < -2**31:
            return -2**31
        elif number > (2**31 - 1):
            return 2**31 - 1
        else:
            return number


str_list = ["", "h", "words and 987",
            "+-12", "-+7477", "+7546-645", "--755", "++7477", "--7477",
            ".1", "3.14159   ", "+3.14159   ", "-3.14159   ",
            "   +123456 my love   ", "   -123456 my love   ",
            "2147483647 hello", "2147483648 hello", "+2147483648 hello",
            "-2147483650 hello", "-2147483648 hello"]

sol = Solution()
for s in str_list:
    print("{} => {}".format(s, sol.myAtoi(s)))