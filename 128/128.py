class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # elements = set()
        # maxDist = 0

        # for num in nums:
        #     if(not num in elements):
        #         elements.add(num)
        
        # for e in elements:
        #     currDist = 0
        #     while(e + currDist in elements):
        #         maxDist = max(currDist + 1, maxDist)
        #         currDist += 1
                
        #     currDist = 0
        #     while(e - currDist in elements):
        #         maxDist = max(currDist + 1, maxDist)
        #         currDist += 1
        
        # return maxDist

        maxDist = 0
        elements = set()
        for num in nums:
            if(not num in elements):
                elements.add(num)

        for e in elements:
            if(not e - 1 in elements):
                currDist = 1
                while(e + currDist in elements):
                    currDist += 1
                
                maxDist = max(currDist, maxDist)
        
        return maxDist

                    
        