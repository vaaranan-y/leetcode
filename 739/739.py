class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] # stores indices
        answer = [0]*len(temperatures)

        for i in range(len(temperatures)):
            # print(stack, temperatures[i])
            while(len(stack) and temperatures[stack[-1]] < temperatures[i]):
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return answer