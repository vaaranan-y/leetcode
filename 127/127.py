class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = [beginWord]
        count = 1
        seen = set([beginWord])
        mappings = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = list(word)
                pattern[i] = "*"
                mappings["".join(pattern)].append(word)

        while(len(q) > 0):
            qLen = len(q)
            for i in range(qLen):
                currWord = q.pop(0)
                if(currWord == endWord):
                    return count
                for i in range(len(currWord)):
                    temp = list(currWord)
                    temp[i] = "*"
                    for neighbour in mappings["".join(temp)]:
                        if(neighbour not in seen):
                            q.append(neighbour)
                            seen.add(neighbour)
                        
            count += 1
        
        return 0

                    

            