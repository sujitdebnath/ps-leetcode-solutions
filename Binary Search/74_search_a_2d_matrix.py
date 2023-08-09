class Solution:
    def searchMatrix(self, matrix, target):
        for row in matrix:
            if self.binary_search(row, target) != -1:
                return True
        
        return False
    
    def binary_search(self, arr, val):
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = (low+high) // 2

            if arr[mid] < val:
                low = mid + 1
            elif arr[mid] > val:
                high = mid - 1
            else:
                return mid
        
        return -1


matrix = [[1,  3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 60]]
target = 3

sol = Solution()
print(sol.searchMatrix(matrix, target))