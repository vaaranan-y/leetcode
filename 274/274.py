class Solution:
    def hIndex(self, citations: List[int]) -> int:
        counts = [0]*(len(citations) + 1)
        for citation in citations:
            if(citation <= len(citations)):
                counts[citation] += 1
            else:
                counts[len(citations)] += 1
        
        totalCitations = 0
        for i in range(len(counts) - 1, -1, -1):
            totalCitations += counts[i]
            if(totalCitations >= i):
                return i
