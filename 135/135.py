class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1]*len(ratings)

        for i in range(0, len(ratings) - 1):
            if(ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]):
                candies[i] = candies[i + 1] + 1
    
        for i in range(len(ratings) - 1, 0, -1):
            if(ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]):
                candies[i] = candies[i - 1] + 1
        
        return sum(candies)