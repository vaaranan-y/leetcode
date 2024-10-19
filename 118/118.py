class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []
        for i in range(numRows):
            if(i == 0):
                rows.append([1])
            elif(i == 1):
                rows.append([1,1])
            else:
                row = [1]
                for j in range(1, i):
                    row.append(rows[i - 1][j - 1] + rows[i - 1][j])
                row.append(1)
                rows.append(row)
        return rows
        