class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        ps = 0

        for letter in t:
            if(ps < len(s) and letter == s[ps]):
                ps += 1
            
            if(ps >= len(s)):
                return True

        
        return False
