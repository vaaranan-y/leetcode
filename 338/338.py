class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = 0
        highestPower = 1
        ans = [0]*(n + 1)

        for i in range(1, n + 1):
            if(i == highestPower):
                highestPower *= 2
                counter = 0
            ans[i] = ans[counter] + 1
            counter += 1
            
            print(i, highestPower, counter)

        return ans

        