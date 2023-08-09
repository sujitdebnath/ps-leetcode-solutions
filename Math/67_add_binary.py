class Solution:
    def addBinary(self, a, b):
        result_to_bin_carry = {
            0: ['0', '0'],
            1: ['1', '0'],
            2: ['0', '1'],
            3: ['1', '1']
        }

        added_binary_num = list()
        carry            = '0'

        for a_digit, b_digit in zip(a[::-1], b[::-1]):
            res                = int(a_digit) + int(b_digit) + int(carry)
            add_bin, new_carry = result_to_bin_carry[res]
            added_binary_num.append(add_bin)
            carry = new_carry
        
        if len(a) != len(b):
            if len(a) > len(b):
                rem_bin_num = a[:len(a)-len(b)]
            elif len(a) < len(b):
                rem_bin_num = b[:len(b)-len(a)]

            for digit in rem_bin_num[::-1]:
                res                = int(digit) + int(carry)
                add_bin, new_carry = result_to_bin_carry[res]
                added_binary_num.append(add_bin)
                carry = new_carry
        
        if carry == '1':
            added_binary_num.append(carry)
        
        return ("").join(added_binary_num)[::-1]


a_list = ["101011", "10111010", "10111010"]
b_list = ["10011010", "101011", "11101011"]
sol = Solution()

for a, b in zip(a_list, b_list):
    print("{} + {} = {}".format(a, b, sol.addBinary(a, b)))