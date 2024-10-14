class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(openCount, endCount, n, curr):
            if(openCount == n and endCount == n):
                res.append(curr)
            elif(openCount == n):
                backtrack(openCount, endCount + 1, n, curr + ")")
            else:
                if(endCount < openCount):
                    backtrack(openCount, endCount + 1, n, curr + ")")
                backtrack(openCount + 1, endCount, n, curr + "(")
        backtrack(0, 0, n, "")

        return res
        