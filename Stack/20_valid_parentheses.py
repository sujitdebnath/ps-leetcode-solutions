class Solution:
    def isValid(self, s):
        parentheses_stack = list()

        for parentheses in s:
            if parentheses in ['(', '{', '[']:
                parentheses_stack.append(parentheses)
            elif parentheses in [')', '}', ']']:
                if not parentheses_stack:
                    return False
                else:
                    top_parentheses = parentheses_stack.pop()
                    if ((top_parentheses == '(' and parentheses != ')') or
                        (top_parentheses == '{' and parentheses != '}') or
                        (top_parentheses == '[' and parentheses != ']')):
                       return False

        if not parentheses_stack:
            return True
        else:
            return False


s   = "[(){[]{}}][]"
sol = Solution()
print(sol.isValid(s))