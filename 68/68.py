class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        currWidth = 0
        line = []
        i = 0

        while(i < len(words)):
            if(currWidth + len(line) + len(words[i]) > maxWidth):
                extraSpace = maxWidth - currWidth
                equalSpace = extraSpace//max(1, len(line) - 1)
                distributionSpace = extraSpace % max(1, len(line) - 1)

                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * equalSpace
                    if distributionSpace:
                        line[j] += " "
                        distributionSpace -= 1
                
                lines.append("".join(line))
                line = []
                currWidth = 0
            
            line.append(words[i])
            currWidth += len(words[i])
            i += 1
        
        # Last line
        lastLine = " ".join(line)
        lastSpace = " "*(maxWidth - len(lastLine))
        lines.append(lastLine + lastSpace)

        return lines




            
