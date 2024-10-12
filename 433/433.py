class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        visited = set()
        geneChoices = ["A", "C", "T", "G"]
        q = [startGene]
        level = 0
        while len(q) != 0:
            newQ = []
            for curr in q:
                visited.add(curr)
                if curr == endGene:
                    return level
                else:
                    for i in range(len(curr)):
                        for j in range(len(geneChoices)):
                            if geneChoices[j] == curr[i]:
                                continue
                            temp = list(curr)
                            temp[i] = geneChoices[j]
                            temp = "".join(temp)
                            if temp not in visited and temp in bank:
                                newQ.append(temp)

            level += 1
            q = newQ

        return -1
