class Solution:
    def toLowerCase(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            asciiCode = ord(s[i])
            if(asciiCode >= 65 and asciiCode <= 90):
                s[i] = chr(asciiCode + 32)

        
        return "".join(s)

        