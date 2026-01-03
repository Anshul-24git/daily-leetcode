class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index

            stack.append(i)

        return answer
        '''
        Input: temperatures = [73,74,75,71,69,72,76,73]
        Output: [1,1,4,2,1,1,0,0]

        Brute Force : Iterate through for every element

        Optimized : Stack/monotonic stack

        [73,74,75,71,69,72,76,73]
        Stack = []
        Day 0 | Temp = 73 | answer = [0,0,0,0,0,0,0,0]
        Day 1 | Temp = 74, 74>73 | answer[0] = 1 | Stack = [1]
        Day 2 | Temp = 75, 75>74 | answer[1] = 1

        '''
