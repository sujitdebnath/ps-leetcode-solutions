class Solution:
    def spiralOrder(self, matrix):
        rows, cols      = len(matrix), len(matrix[0])
        m_down, m_top   = rows-1, 0
        n_right, n_left = cols-1, 0

        right, down, left, up = True, False, False, False

        spiral_order_list = list()
        curr_m, curr_n    = 0, 0

        for _ in range(rows*cols):
            spiral_order_list.append(matrix[curr_m][curr_n])

            if right:
                if curr_n == n_right:
                    right, down = False, True
                    n_right     = n_right - 1
                    m_top       = m_top + 1
                    curr_m      = curr_m + 1
                else:
                    curr_n = curr_n + 1
            elif down:
                if curr_m == m_down:
                    down, left = False, True
                    m_down     = m_down - 1
                    curr_n     = curr_n - 1
                else:
                    curr_m = curr_m + 1
            elif left:
                if curr_n == n_left:
                    left, up = False, True
                    n_left   = n_left + 1
                    curr_m   = curr_m - 1
                else:
                    curr_n = curr_n - 1
            elif up:
                if curr_m == m_top:
                    up, right = False, True
                    curr_n    = curr_n + 1
                else:
                    curr_m = curr_m - 1
        
        return spiral_order_list


def matrix_generator(m ,n):
    matrix = [[0]*n for _ in range(m)]
    val    = 1
    
    for row in range(m):
        for col in range(n):
            matrix[row][col] = val
            val = val + 1
    
    return matrix

matrix = matrix_generator(3, 4)
print(matrix)

sol = Solution()
print(sol.spiralOrder(matrix))