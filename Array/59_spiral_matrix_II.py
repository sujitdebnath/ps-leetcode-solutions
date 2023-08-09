class Solution:
    def generateMatrix(self, n):
        matrix = [[0]*n for _ in range(n)]
        
        n_down, n_top         = n-1, 0
        n_right, n_left       = n-1, 0
        curr_row, curr_col    = 0, 0
        right, down, left, up = True, False, False, False

        for val in range(1, n*n+1):
            matrix[curr_row][curr_col] = val

            if right:
                if curr_col == n_right:
                    right, down = False, True
                    n_right     = n_right - 1
                    n_top       = n_top + 1
                    curr_row    = curr_row + 1
                else:
                    curr_col = curr_col + 1
            elif down:
                if curr_row == n_down:
                    down, left = False, True
                    n_down     = n_down - 1
                    curr_col   = curr_col - 1
                else:
                    curr_row = curr_row + 1
            elif left:
                if curr_col == n_left:
                    left, up = False, True
                    n_left   = n_left + 1
                    curr_row = curr_row - 1
                else:
                    curr_col = curr_col - 1
            elif up:
                if curr_row == n_top:
                    up, right = False, True
                    curr_col  = curr_col + 1
                else:
                    curr_row = curr_row - 1
        
        return matrix


n   = 3
sol = Solution()
print(sol.generateMatrix(n))