class Solution:
    def fizzBuzz(self, n):
        answers = list()
        
        for i in range(1, n+1):
            if i%3 == 0 and i%5 == 0:
                answers.append("FizzBuzz")
            elif i%3 == 0:
                answers.append("Fizz")
            elif i%5 == 0:
                answers.append("Buzz")
            else:
                answers.append(str(i))
        
        return answers


n = 15
sol = Solution()
print(sol.fizzBuzz(n))