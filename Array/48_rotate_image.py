class Solution:
    def rotate(self, matrix):
        matrix_dict = dict()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                matrix_dict[str(row)+"+"+str(col)] = matrix[row][col]

        for row in range(len(matrix)):
            for col, rev_ind in zip(range(len(matrix[0])), range(len(matrix[0])-1, -1, -1)):
                matrix[row][col] = matrix_dict[str(rev_ind)+"+"+str(row)]


matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol    = Solution()
sol.rotate(matrix)
print(matrix)