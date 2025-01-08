class Solution:
    def reverseWords(self, s: str) -> str:

        # reversedStr = ""
        # currWord = ""
        # notFirstWord = True

        # for char in s:
        #     if(char != ' '):
        #         currWord += char
        #     elif(currWord != ""):
        #         if(notFirstWord):
        #             reversedStr = currWord + reversedStr
        #             notFirstWord = False
        #         else:
        #             reversedStr = currWord + ' ' + reversedStr
        #         currWord = ""
        # if(currWord != "" and not notFirstWord):
        #     reversedStr = currWord + ' ' + reversedStr
        # else:
        #     reversedStr = currWord + reversedStr
        # return reversedStr
        
        words = s.split()
        reversedStr = ""
        for i in range(len(words) - 1, -1, -1):
            if(words[i] != ' '): 
                if(i == len(words) - 1):
                    reversedStr += words[i]
                else:
                    reversedStr = reversedStr + ' ' + words[i]

        return reversedStr