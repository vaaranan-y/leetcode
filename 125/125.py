class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1
        s = s.lower()

        while(p1 < p2):
            if(not (s[p1].isalpha() or s[p1].isnumeric())):
                p1 += 1
            elif(not (s[p2].isalpha() or s[p2].isnumeric())):
                p2 -= 1
            elif(s[p1] != s[p2]):
                return False
            else:
                p1 += 1
                p2 -= 1
        
        return True