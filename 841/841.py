class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        q = rooms[0]

        while(len(q) > 0):
            qLen = len(q)
            for i in range(qLen):
                currKey = q.pop(0)
                if(currKey not in visited):
                    visited.add(currKey)
                    q += rooms[currKey]
        
        for i in range(len(rooms)):
            if(i not in visited):
                return False
        
        return len(visited) == len(rooms)