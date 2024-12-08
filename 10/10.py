class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        cache = dict()

        def helper(i, j):
            if((i,j) in cache):
                return cache[(i, j)]
            if(i >= len(s) and j >= len(p)):
                return True
            elif(j >= len(p)):
                return False
            
            charMatch = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if j + 1 < len(p) and p[j + 1] == '*':
                cache[(i, j)] = helper(i, j + 2) or (charMatch and helper(i + 1, j))
                return cache[(i, j)]
            
            if charMatch:
                cache[(i, j)] = helper(i + 1, j + 1)
                return cache[(i, j)]
            
            cache[(i, j)] = False
            return False

        return helper(0,0)
                