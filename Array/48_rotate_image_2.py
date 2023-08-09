class Solution:
    def rotate(self, matrix):
        n_rows, n_cols = len(matrix), len(matrix[0])

        # assign four coners of the matrix
        first, second = [0, 0], [0, n_cols-1]
        third, fourth = [n_rows-1, n_cols-1], [n_rows-1, 0]

        for _ in range(n_rows//2):
            for _ in range(n_cols-1):
                # swap - first & second
                matrix[first[0]][first[1]], matrix[second[0]][second[1]] = matrix[second[0]][second[1]], matrix[first[0]][first[1]]
                # swap - first & third
                matrix[first[0]][first[1]], matrix[third[0]][third[1]]   = matrix[third[0]][third[1]], matrix[first[0]][first[1]]
                # swap - first & fourth
                matrix[first[0]][first[1]], matrix[fourth[0]][fourth[1]] = matrix[fourth[0]][fourth[1]], matrix[first[0]][first[1]]

                # rotates - update all the coordinates
                first[1]  += 1
                second[0] += 1
                third[1]  -= 1
                fourth[0] -= 1
            
            # rearrange all the coordinates
            temp_first, temp_second, temp_third, temp_fourth = first, second, third, fourth
            first, second, third, fourth                     = temp_fourth, temp_first, temp_second, temp_third

            # dive in deeper layer
            first[0]  += 1
            first[1]  += 1
            second[0] += 1
            second[1] -= 1
            third[0]  -= 1
            third[1]  -= 1
            fourth[0] -= 1
            fourth[1] += 1

            # update rotates parameters
            n_cols -= 2


matrix = [[5,1,9,11,17],[2,4,8,10,20],[13,3,6,7,22],[15,14,12,16,27],[50,55,60,64,51]]
sol    = Solution()
sol.rotate(matrix)

for row in matrix:
    for col in row:
        print(col, end="\t")
    print()