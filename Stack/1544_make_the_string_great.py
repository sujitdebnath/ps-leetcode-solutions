class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return not self.items
      
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None
          
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return None
          
    def size(self):
        return len(self.items)
      
    def __str__(self):
        return str(self.items)

class Solution:
    def makeGood(self, s):
        str_stack = Stack()

        for letter in s:
            if str_stack.is_empty() or str_stack.peek() == letter:
                str_stack.push(letter)
            else:
                if str_stack.peek().lower() == letter or str_stack.peek() == letter.lower():
                    str_stack.pop()
                else:
                    str_stack.push(letter)

        good_string = ""
        while not str_stack.is_empty():
            good_string += str_stack.pop()
        
        return good_string[::-1]


s   = "leEeetcode"
sol = Solution()
print(sol.makeGood(s))