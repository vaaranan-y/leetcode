class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charConversion1 = dict()

        for i in range(len(s)):
            if(s[i] in charConversion1 and charConversion1[s[i]] != t[i]):
                return False
            else:
                charConversion1[s[i]] = t[i]
        
        charConversion2 = dict()

        for i in range(len(t)):
            if(t[i] in charConversion2 and charConversion2[t[i]] != s[i]):
                return False
            else:
                charConversion2[t[i]] = s[i]
        
        return True


        