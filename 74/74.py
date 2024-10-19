class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1

        while(l <= r):
            mid = (l + r)//2
            coordinates = [mid // n, mid % n]
            val = matrix[coordinates[0]][coordinates[1]]

            if(val == target):
                return True
            elif(val < target):
                l = mid + 1
            else:
                r = mid - 1
        
        return False

