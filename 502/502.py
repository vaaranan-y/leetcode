class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        capHeap = []
        profHeap = []
        for i in range(len(profits)):
            capHeap.append((capital[i], profits[i]))
        
        heapify(capHeap)

        while(k > 0):
            while(capHeap and capHeap[0][0] <= w):
                pair = heappop(capHeap)
                heappush(profHeap, (-1 * pair[1], pair[0]))
            
            if(len(profHeap) == 0):
                break
            currProfPair = heappop(profHeap)
            w += currProfPair[0] * -1
            k -= 1
            
        
        return w

        